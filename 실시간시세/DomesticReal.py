import json
import requests
import websockets
import asyncio

# 개인정보
from credential import *


# 웹소켓을 이용한 현재 주식 시세 조회
async def get_current_price2(approval_key, ticker):
    URL = WebSocket_url + "/tryitout/H0STCNT0"

    message = {
        "header": {
            "approval_key": approval_key,
            "custtype": "P",
            "tr_type": "1",
            "content-type": "utf-8",
        },
        "body": {"input": {"tr_id": "H0STCNT0", "tr_key": ticker}},
    }

    async with websockets.connect(URL, ping_interval=None) as websocket:
        # convert to JSON str
        json_str = json.dumps(message)
        await websocket.send(message=json_str)
        await asyncio.sleep(1)
        res = await websocket.recv()
        # Dictionary 형식으로 변환
        res = json.loads(res)
        return res

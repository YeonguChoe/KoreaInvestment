import json
import requests
import websockets
import asyncio
from 국내주식시세.Domestic import *


# 개인정보
from credential import *


# 웹소켓을 이용한 현재 주식 시세 조회
async def get_realtime_price(approval_key, ticker_symbol):
    URL = WebSocket_url + "/tryitout/H0STCNT0"

    message = {
        "header": {
            "approval_key": approval_key,
            "custtype": "P",
            "tr_type": "1",
            "content-type": "utf-8",
        },
        "body": {"input": {"tr_id": "H0STCNT0", "tr_key": ticker_symbol}},
    }

    async with websockets.connect(URL, ping_interval=None) as websocket:
        # convert to JSON str
        json_str = json.dumps(message)
        await websocket.send(message=json_str)

        # 무한히 데이터가 오기만 기다린다
        while True:
            res = await websocket.recv()
            res = res.split("|")
            if res[0] == "0":
                res = res[3]
                res = res.split("^")
                res = res[2]
                
                # int로 자료변환
                res = int(res)
                return(res)

# 웹소켓을 이용한 현재 주식 시세 조회
async def print_realtime_price(access_token, approval_key, ticker_symbol):
    URL = WebSocket_url + "/tryitout/H0STCNT0"

    message = {
        "header": {
            "approval_key": approval_key,
            "custtype": "P",
            "tr_type": "1",
            "content-type": "utf-8",
        },
        "body": {"input": {"tr_id": "H0STCNT0", "tr_key": ticker_symbol}},
    }

    # 비교를 위한 array 변수
    coordinate = [0,0]

    async with websockets.connect(URL, ping_interval=None) as websocket:
        # convert to JSON str
        json_str = json.dumps(message)
        await websocket.send(message=json_str)

        # 무한히 데이터가 오기만 기다린다
        while True:
            res = await websocket.recv()
            res = res.split("|")
            if res[0] == "0":
                res = res[3]
                res = res.split("^")
                res = res[2]
                # 새로운 값 대입
                coordinate[0] = coordinate[1]
                coordinate[1]=int(res)
                # 이전값과 비교
                circle = ""
                arrow = ""
                if(coordinate[0]>coordinate[1]):
                    circle = "🔴"
                    arrow = "🔼"
                elif(coordinate[0]<coordinate[1]):
                    circle = "🟢"
                    arrow = "🔽"
                else:
                    circle = "⚪"
                    arrow = ""
                print(f"{circle}{stock_info(access_token, ticker_symbol)["prdt_abrv_name"]} 실시간 현재가: {res} {arrow}")

# 실시간 호가
async def market_depth(approval_key,ticker_symbol):
    URL = WebSocket_url+"/tryitout/H0STASP0"
    message = {
        "header": {
            "approval_key": approval_key,
            "custtype": "P",
            "tr_type": "1",
            "content-type": "utf-8",
        },
        "body": {"input": {"tr_id": "H0STASP0", "tr_key": ticker_symbol}},
    }
    async with websockets.connect(URL,ping_interval=None) as websocket:
        # convert to JSON str
        json_str = json.dumps(message)
        await websocket.send(message=json_str)

        # 무한히 데이터가 오기만 기다린다
        while True:
            res = await websocket.recv()
            print(res)

# 매수/매도 주문 체결 통보 (추가 필요)
async def report_order_status(approval_key,ticker_symbol):
    URL = WebSocket_url + "/tryitout/H0STCNI0"

    message = {
        "header": {
            "approval_key": approval_key,
            "custtype": "P",
            "tr_type": "1",
            "content-type": "utf-8",
        },
        "body": {"input": {"tr_id": "H0STCNI0", "tr_key": ticker_symbol}},
    }

    async with websockets.connect(URL, ping_interval=None) as websocket:
        # convert to JSON str
        json_str = json.dumps(message)
        await websocket.send(message=json_str)

        # 무한히 데이터가 오기만 기다린다
        while True:
            res = await websocket.recv()
            print(res)

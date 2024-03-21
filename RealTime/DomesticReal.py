import json
import requests
import websockets
import asyncio
from DomesticStockInfo.Domestic import *


# 개인정보
from credential import *


# 웹소켓을 이용한 현재 주식 시세 조회
async def print_realtime_price(access_token, approval_key, ticker_symbol):
    # 주식 이름 받기
    stock_name = get_stock_name(access_token=access_token, ticker_symbol=ticker_symbol)
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
    coordinate = [0, 0]

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
                coordinate[1] = int(res)
                # 이전값과 비교
                circle = ""
                arrow = ""
                if coordinate[0] > coordinate[1]:
                    circle = "🔴"
                    arrow = "🔼"
                elif coordinate[0] < coordinate[1]:
                    circle = "🟢"
                    arrow = "🔽"
                else:
                    circle = "⚪"
                    arrow = ""
                print(f"{circle}{stock_name} 실시간 주가: {res} {arrow}")


# 실시간 호가
async def market_depth(access_token, approval_key, ticker_symbol):
    # 주식 이름 받기
    stock_name = get_stock_name(access_token=access_token, ticker_symbol=ticker_symbol)
    URL = WebSocket_url + "/tryitout/H0STASP0"
    message = {
        "header": {
            "approval_key": approval_key,
            "custtype": "P",
            "tr_type": "1",
            "content-type": "utf-8",
        },
        "body": {"input": {"tr_id": "H0STASP0", "tr_key": ticker_symbol}},
    }
    async with websockets.connect(URL, ping_interval=None) as websocket:
        # convert to JSON str
        json_str = json.dumps(message)
        await websocket.send(message=json_str)

        # 무한히 데이터가 오기만 기다린다
        while True:
            res = await websocket.recv()
            # 받은 메세지 처리
            res = res.split("|")
            if res[0] == "0":
                res = res[3]
                res = res.split("^")  # 수신데이터를 split '^'
                print(f"종목: {stock_name}({res[0]})")
                print(
                    f"확인시간: {res[1][:2]}시{res[1][2:4]}분{res[1][4:6]}초 현재상황: {'장중' if res[2]=='0' else '장외'}"
                )
                print("======================================")
                print("매도호가10 [%s]    잔량10 [%s]" % (res[12], res[32]))
                print("매도호가09 [%s]    잔량09 [%s]" % (res[11], res[31]))
                print("매도호가08 [%s]    잔량08 [%s]" % (res[10], res[30]))
                print("매도호가07 [%s]    잔량07 [%s]" % (res[9], res[29]))
                print("매도호가06 [%s]    잔량06 [%s]" % (res[8], res[28]))
                print("매도호가05 [%s]    잔량05 [%s]" % (res[7], res[27]))
                print("매도호가04 [%s]    잔량04 [%s]" % (res[6], res[26]))
                print("매도호가03 [%s]    잔량03 [%s]" % (res[5], res[25]))
                print("매도호가02 [%s]    잔량02 [%s]" % (res[4], res[24]))
                print("매도호가01 [%s]    잔량01 [%s]" % (res[3], res[23]))
                print("--------------------------------------")
                print("매수호가01 [%s]    잔량01 [%s]" % (res[13], res[33]))
                print("매수호가02 [%s]    잔량02 [%s]" % (res[14], res[34]))
                print("매수호가03 [%s]    잔량03 [%s]" % (res[15], res[35]))
                print("매수호가04 [%s]    잔량04 [%s]" % (res[16], res[36]))
                print("매수호가05 [%s]    잔량05 [%s]" % (res[17], res[37]))
                print("매수호가06 [%s]    잔량06 [%s]" % (res[18], res[38]))
                print("매수호가07 [%s]    잔량07 [%s]" % (res[19], res[39]))
                print("매수호가08 [%s]    잔량08 [%s]" % (res[20], res[40]))
                print("매수호가09 [%s]    잔량09 [%s]" % (res[21], res[41]))
                print("매수호가10 [%s]    잔량10 [%s]" % (res[22], res[42]))
                print("======================================")
                print("총매도호가 잔량        [%s]" % (res[43]))
                print("총매도호가 잔량 증감   [%s]" % (res[54]))
                print("총매수호가 잔량        [%s]" % (res[44]))
                print("총매수호가 잔량 증감   [%s]" % (res[55]))
                print("시간외 총매도호가 잔량 [%s]" % (res[45]))
                print("시간외 총매수호가 증감 [%s]" % (res[46]))
                print("시간외 총매도호가 잔량 [%s]" % (res[56]))
                print("시간외 총매수호가 증감 [%s]" % (res[57]))
                print("예상 체결가            [%s]" % (res[47]))
                print("예상 체결량            [%s]" % (res[48]))
                print("예상 거래량            [%s]" % (res[49]))
                print("예상체결 대비          [%s]" % (res[50]))
                print("부호                   [%s]" % (res[51]))
                print("예상체결 전일대비율    [%s]" % (res[52]))
                print("누적거래량             [%s]" % (res[53]))
                print("주식매매 구분코드      [%s]" % (res[58]))
                return

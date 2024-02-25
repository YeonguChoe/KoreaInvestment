import json
from time import sleep
import requests
import datetime

# 개인정보
from credential import *


def buy(access_token, ticker_symbol, price, buy_quantity):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "TTTC0802U",
    }
    body = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": ticker_symbol,
        "ORD_DVSN": "00",
        "ORD_QTY": buy_quantity,
        "ORD_UNPR": price,
    }
    URL = url + "/uapi/domestic-stock/v1/trading/order-cash"
    res = requests.post(url=URL, headers=header, data=json.dumps(body)).text
    # str을 dict로 변환
    res = json.loads(res)
    return res


def sell(access_token, ticker_symbol, price, sell_quantity):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "TTTC0801U",
    }
    body = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": ticker_symbol,
        "ORD_DVSN": "00",
        "ORD_QTY": sell_quantity,
        "ORD_UNPR": price,
    }
    URL = url + "/uapi/domestic-stock/v1/trading/order-cash"
    res = requests.post(url=URL, headers=header, data=json.dumps(body)).text
    # str을 dict로 변환
    res = json.loads(res)
    return res


# 미체결 buy건
def list_buy_order(access_token):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "TTTC8001R",
    }
    query_parameter = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "INQR_STRT_DT": "20240101",
        "INQR_END_DT": datetime.datetime.now().strftime("%Y%m%d"),
        "SLL_BUY_DVSN_CD": "02",
        "INQR_DVSN": "00",
        "PDNO": "",
        "CCLD_DVSN": "02",
        "ORD_GNO_BRNO": "",
        "ODNO": "",
        "INQR_DVSN_3": "00",
        "INQR_DVSN_1": "",
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": "",
    }
    URL = url + "/uapi/domestic-stock/v1/trading/inquire-daily-ccld"
    res = requests.get(URL, headers=header, params=query_parameter).text
    # str을 dict로 변환
    res = json.loads(res)["output1"]
    # 각 주문건에 대해 반복문
    for order in res:
        stock_name = order["prdt_name"]
        date = order["ord_dt"]
        order_number = order["odno"]
        order_price = order["ord_unpr"]
        order_qty = order["ord_qty"]
        print(
            f"종목: {stock_name} 주문가격:{order_price} 주문수량: {order_qty} 주문번호: {order_number} 주문날짜: {date}"
        )


# 미체결 sell건
def list_sell_order(access_token):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "TTTC8001R",
    }
    query_parameter = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "INQR_STRT_DT": "20240101",
        "INQR_END_DT": datetime.datetime.now().strftime("%Y%m%d"),
        "SLL_BUY_DVSN_CD": "01",
        "INQR_DVSN": "00",
        "PDNO": "",
        "CCLD_DVSN": "02",
        "ORD_GNO_BRNO": "",
        "ODNO": "",
        "INQR_DVSN_3": "00",
        "INQR_DVSN_1": "",
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": "",
    }
    URL = url + "/uapi/domestic-stock/v1/trading/inquire-daily-ccld"
    res = requests.get(URL, headers=header, params=query_parameter).text
    # str을 dict로 변환
    res = json.loads(res)["output1"]
    # 각 주문건에 대해 반복문
    for order in res:
        stock_name = order["prdt_name"]
        date = order["ord_dt"]
        order_number = order["odno"]
        order_price = order["ord_unpr"]
        order_qty = order["ord_qty"]
        print(
            f"종목: {stock_name} 주문가격:{order_price} 주문수량: {order_qty} 주문번호: {order_number} 주문날짜: {date}"
        )


# 주문 취소
def cancel_order(access_token, order_number):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "TTTC0803U",
    }
    body = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "KRX_FWDG_ORD_ORGNO": "",
        "ORGN_ODNO": order_number,
        "ORD_DVSN": "00",
        "RVSE_CNCL_DVSN_CD": "02",
        "ORD_QTY": "0",
        "ORD_UNPR": "0",
        "QTY_ALL_ORD_YN": "Y",
    }
    URL = url + "/uapi/domestic-stock/v1/trading/order-rvsecncl"
    res = requests.post(url=URL, headers=header, data=json.dumps(body)).text
    # str을 dict로 변환
    res = json.loads(res)

    return res


# 현금 잔고 조회
def get_remaining_cash(access_token):
    URL = url + "/uapi/domestic-stock/v1/trading/inquire-psbl-order"
    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {access_token}",
        "appKey": APP_Key,
        "appSecret": APP_Secret,
        "tr_id": "TTTC8908R",
    }
    params = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": "005930",
        "ORD_UNPR": "72900",
        "ORD_DVSN": "01",
        "CMA_EVLU_AMT_ICLD_YN": "Y",
        "OVRS_ICLD_YN": "Y",
    }
    res = requests.get(URL, headers=headers, params=params)
    remaining_cash = int(res.json()["output"]["ord_psbl_cash"])
    return remaining_cash


# 주식 잔고 조회
def get_remaining_stock(access_token):
    URL = url + "/uapi/domestic-stock/v1/trading/inquire-balance"
    header = {
        "authorization": "Bearer " + access_token,
        "appKey": APP_Key,
        "appSecret": APP_Secret,
        "tr_id": "TTTC8434R",
    }
    query_parameter = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "AFHR_FLPR_YN": "N",
        "OFL_YN": "",
        "INQR_DVSN": "02",
        "UNPR_DVSN": "01",
        "FUND_STTL_ICLD_YN": "N",
        "FNCG_AMT_AUTO_RDPT_YN": "N",
        "PRCS_DVSN": "01",
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": "",
    }
    res = requests.get(URL, headers=header, params=query_parameter)
    stock_list = res.json()["output1"]
    evaluation = res.json()["output2"]
    stock_dict = {}
    print("==========주식 잔고==========")
    for stock in stock_list:
        if int(stock["hldg_qty"]) > 0:
            stock_dict[stock["pdno"]] = stock["hldg_qty"]
            print(f"{stock['prdt_name']}({stock['pdno']}): {stock['hldg_qty']}주")
            sleep(0.1)
    print("============요약=============")
    print(f"주식 평가 금액: {evaluation[0]['scts_evlu_amt']}원")
    sleep(0.1)
    print(f"평가 손익 합계: {evaluation[0]['evlu_pfls_smtl_amt']}원")
    sleep(0.1)
    print(f"총 평가 금액: {evaluation[0]['tot_evlu_amt']}원")
    sleep(0.1)
    print(f"=============================")
    return stock_dict

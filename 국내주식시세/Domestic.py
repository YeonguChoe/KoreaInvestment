import requests
import json
from datetime import *

# 개인정보
from credential import *


# 주식현재가 시세
def get_current_price1(access_token, ticker):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "FHKST01010100",
    }
    query_parameter = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": ticker}
    URL = url + "/uapi/domestic-stock/v1/quotations/inquire-price"
    res = requests.get(url=URL, params=query_parameter, headers=header)
    # text 형식으로 변환
    res = res.text
    # dictionary 형식으로 변환
    res = json.loads(res)["output"]
    return res["stck_hgpr"]


# 주식현재가 회원사
def get_stock_member(access_token, ticker_symbol):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "FHKST01010600",
    }
    query_parameter = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": ticker_symbol}
    URL = url + "/uapi/domestic-stock/v1/quotations/inquire-member"
    res = requests.get(url=URL, params=query_parameter, headers=header).text
    # dictionary 형식으로 변환
    res = json.loads(res)["output"]
    return res


# 특정 주식 정보
def stock_info(access_token, ticker_symbol):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "CTPF1604R",
    }
    query_parameter = {"PDNO": ticker_symbol, "PRDT_TYPE_CD": "300"}
    URL = url + "/uapi/domestic-stock/v1/quotations/search-info"
    res = requests.get(url=URL, params=query_parameter, headers=header).text
    # dictionary 형식으로 변환
    res = json.loads(res)["output"]
    return res


# 업종 분봉조회
def get_candlestick(access_token, ticker_symbol):
    header = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "FHKST03010200",
        "custtype": "P",
    }
    query_parameter = {
        "FID_ETC_CLS_CODE": "",
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": ticker_symbol,
        "FID_INPUT_HOUR_1": get_current_time(),
        "fid_pw_data_incu_yn": "Y",
    }
    URL = url + "/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"
    res = requests.get(url=URL, params=query_parameter, headers=header)

    # # 테스트를 위해 저장하기
    json_data = json.loads(res.text)
    return json_data["output2"][0]["cntg_vol"]


# 추가 함수
def get_current_time():
    current_time = datetime.now()
    hour = current_time.hour
    if hour < 10:
        hour = f"0{hour}"
    minute = current_time.minute
    if minute < 10:
        minute = f"0{minute}"
    second = current_time.second
    if second < 10:
        second = f"0{second}"

    return f"{hour}{minute}{second}"

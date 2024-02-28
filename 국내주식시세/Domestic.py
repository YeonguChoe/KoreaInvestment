import requests
import json
from datetime import *

# 개인정보
from credential import *


# 주식현재가 시세
# 실시간 시세가 아니라 대체적인 가격
# 장외에도 검색할 수 있다는 장점이 있다
def get_price(access_token, ticker_symbol):
    header = {
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "FHKST01010100",
    }
    query_parameter = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": ticker_symbol}
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


# 주식 이름 받기
def get_stock_name(access_token, ticker_symbol):
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
    # 주식 이름만 추출하기
    res = res["prdt_abrv_name"]

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


# 특정 날짜의 매수 매도 거래량 출력
def daily_exchange_volume(
    access_token, ticker_symbol, date=datetime.now().strftime("%Y%m%d")
):

    header = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + access_token,
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "FHKST03010800",
        "custtype": "P",
    }
    query_parameter = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": ticker_symbol,
        "FID_INPUT_DATE_1": date,
        "FID_INPUT_DATE_2": date,
        "FID_PERIOD_DIV_CODE": "D",
    }

    URL = url + "/uapi/domestic-stock/v1/quotations/inquire-daily-trade-volume"
    res = requests.get(url=URL, params=query_parameter, headers=header)
    # HTTP 응답에서 text를 추출
    res = res.text
    # str을 dict로 변환
    res = json.loads(res)
    daily_buy_volume = res["output2"][0]["total_shnu_qty"]
    daily_sell_volume = res["output2"][0]["total_seln_qty"]
    # 날짜 문자열을 연,월,일로 분해하기
    parsed_date = datetime.strptime(date, "%Y%m%d")
    year = parsed_date.year
    month = parsed_date.month
    day = parsed_date.day
    # 문자열 만들기
    text = f"""
==================================================
{stock_info(access_token, ticker_symbol)["prdt_abrv_name"]} {year}년 {month}월 {day}일 체결량
==================================================
총 매수량(buy): {daily_buy_volume}
총 매도량(sell): {daily_sell_volume}
==================================================
    """
    return text


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

from time import sleep
from OAuth.OAuth import *
from 실시간시세.DomesticReal import *
from 국내주식시세.Domestic import *
from 국내주식주문.Order import *
import asyncio


async def main():
    # get_access_token()
    # get_approval_key()
    t = read_access_token()
    k = read_approval_key()

    await get_realtime_price(t, k, "005930")
    # await market_depth(t, k, "005930")
    get_price(t, "035420")


if __name__ == "__main__":
    asyncio.run(main())

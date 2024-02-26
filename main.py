from time import sleep
from OAuth인증.OAuth import *
from 실시간시세.DomesticReal import *
from 국내주식시세.Domestic import *
from 국내주식주문.Order import *
import asyncio


async def main():
    k = read_approval_key()
    await get_current_price2(k, "005930")


if __name__ == "__main__":
    asyncio.run(main())

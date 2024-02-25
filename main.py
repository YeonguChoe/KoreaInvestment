from time import sleep
from OAuth인증.OAuth import *
from 실시간시세.DomesticReal import *
from 국내주식시세.Domestic import *
from 국내주식주문.Order import *
import asyncio


async def main():
    t = read_access_token()
    print(get_remaining_stock(t))


if __name__ == "__main__":
    asyncio.run(main())

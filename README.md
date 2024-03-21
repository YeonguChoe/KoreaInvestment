# Korea Investment & Securities Algorithm trading
In Korean stock market, every home trading software runs on only Windows.
Some people have great trading knowledge but don't have coding experience.
I made this python OOP script for the people who only have Mac or have great trading knowledge but little to no coding experience to be able to do system trading.

## Setting up
1. Create an Korea Investment & Securities account and generate the API key.
2. Download the zip file from GitHub.

<img src="./readme-resource/1.png" width = 500/>

3. Unzip the file and open **KOREAINVEST** directory with your favorite code editor.

4. In `credential.py`, input generated credentials: CANO, APP_Key, APP_SECRET

<img src="./readme-resource/2.png" width = 500/>

5. In `main.py`, `run get_access_token` and `get_approval_key`

```python
async def main():
    get_access_token()
    get_approval_key()
```

6. Once, access token and approval key are generated, you can start trading.

## Information of the stock
### Basic Information
- daily_exchange_volume
- get_candlestick
- get_stock_name
- get_price
### Realtime Information
> For realtime information, you can only use theses method when the Korea stock market is opened (**PST 5:00 PM - 11:30 PM**)
- get_realtime_price
- market_depth

## Order
### Buy stock
- buy
- list_buy_order

### Sell stock
- sell
- list_sell_order

### Modifying order
- cancel_order

### Current Account status
- get_remaining_cash
- get_remaining_stock
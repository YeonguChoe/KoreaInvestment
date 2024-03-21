# Korea Investment & Securities Algorithm trading
In Korean stock market, every home trading software runs on only Windows.
Some people have great trading knowledge but don't have coding experience.
I made this python OOP script for the people who only have Mac or have great trading knowledge but little to no coding experience to be able to do system trading.

## Disclaimer
- **Any loss of money is the responsibility of trader, even if it occurred by technical reason.**
- **Any kind of loss of personal data (e.g, using public wifi) is responsibility of trader.**

## Setting up
1. Create an Korea Investment & Securities account and generate the API key.
2. Download the zip file from GitHub.

<img src="./readme-resource/1.png" width = 500/>

3. Unzip the file and open **KOREAINVEST** directory with your favorite code editor.

4. In `credential.py`, input generated credentials: `CANO`, `APP_Key`, `APP_SECRET`

<img src="./readme-resource/2.png" width = 500/>

5. In `main.py`, `run get_access_token` and `get_approval_key`

```python
async def main():
    get_access_token()
    get_approval_key()
```

6. Once, access token and approval key are generated, you can start trading.

## Information of the stock
### Code you must keep in the main script
- This code reads token and key for server connection.
```python
async def main():
    t = read_access_token()
    k = read_approval_key()
```

### Basic Information
- daily_exchange_volume
    > If you don't put the date, it is set to today's date as default.
    - example
    ```python
    daily_exchange_volume(t, "035420","20240101")
    ```
    - result
    ```bash
    ==================================================
    Trade Quantity
    ==================================================
    Company name: NAVER
    Date: 2024-March-21
    ==================================================
    Total buy quantity: 429405
    Total sell quantity: 545601
    ==================================================
    ```
- get_candlestick
    - It prints out height of the most recent 1 minute candle stick.
    - example
    ```python
    get_candlestick(t, "035420")
    ```
    - result
    ```bash
    1 minute traded quantity: 43129
    ```
- get_price
    > This is not the real time price. It is a quote price.
    If you are looking for real time price, use `print_realtime_price` at the bottom.

    - example
    ```python
    get_price(t,"035420")
    ```
    - result
    ```bash
    Market price of NAVER: 187800 won
    ```

### Realtime Information
> For realtime information, you can only use theses method when the Korea stock market is opened (**PST 5:00 PM - 11:30 PM**)
- print_realtime_price
    - example
    ```python
    await print_realtime_price(t,k,"035420")
    ```
    - result
    ```bash
    🟢 Real-time stock price of Naver: 183900 won 🔽
    🔴 Real-time stock price of Naver: 184100 won 🔼
    🟢 Real-time stock price of Naver: 184000 won 🔽
    ```

- market_depth
    - example
    ```python
    await market_depth(t,k,"035420")
    ```

## Order
> Order can only be used during Korea market opening time (**PST 5:00 PM - 11:30 PM**)
### Buy stock
- buy
    - example
    ```python
    buy(t, "035420", 3000, 1)
    ```
- list_buy_order
    - example
    ```python
    list_buy_order(t)
    ```

### Sell stock
- sell
    - example
    ```python
    sell(t, "035420", 300, 1)
    ```
- list_sell_order
    - example
    ```python
    list_sell_order(t)
    ```
### Modifying order
- cancel_order
    - example
    ```python
    cancel_order(t,"12345")
    ```


### Current Account status
- get_remaining_cash
    - example
    ```python
    cancel_order(t,"12345")
    ```

- get_remaining_stock
    - example
    ```python
    get_remaining_stock(t, k)
    ```

## Bug Report
If you find any bug or anything to improve, please send it to **yeongu.choe@icloud.com**.


import pywinmacro as pw
import time

location1 = (398, 66)  # addr
location2 = (442, 125)  # search
location3 = (351, 620)  #historical
location4 = (591,851)   #download

#조회 대상 티커코드
stocks = ["MSTF", "FB", "TSLA", "AAPL", "AMXZN","RIOT","MARA"]

# 역대 주가 정보를 다운받는 함수
def price(ticker):
    # 검색창 클릭
    pw.click(location2)
    time.sleep(3)
    # 티커코드 입력
    pw.type_in(ticker)
    time.sleep(3)
    # 엔터
    pw.key_press_once("enter")
    time.sleep(3)
    # Historical Data 클릭
    pw.click(location3)
    time.sleep(3)
    # Download 클릭
    pw.click(location4)
    time.sleep(3)

#stock 리스트
def get_price_data(stocks):
    for stock in stocks:
        #개별 종목 주가 조회
        price(stock)
        time.sleep(3)

#야후 파이낸스 접속
def go_to_yfinance():
    # 주소창 클릭
    pw.click(location1)
    time.sleep(1)
    # 야후 파이낸스 주소 입력
    pw.type_in("https://finance.yahoo.com")
    time.sleep(1)
    # 엔터키 입력
    pw.key_press_once("enter")
    time.sleep(1)

#야후 파이낸스 접속
go_to_yfinance()

#주가 검색 작업
get_price_data(stocks)




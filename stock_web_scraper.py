from bs4 import BeautifulSoup
import requests 
import time

def priceTracker(): 

    soup = BeautifulSoup(response.text, 'html.parser')

    price = soup.find_all('div', {'class':'D(ib) Va(m) Maw(65%) Ov(h)'})[0].find('span').text

    print(stock + ' price: ' + price)


if __name__ == '__main__':
    choice = input("Live tracker (l) or just display current price (c)? ")

    stock_url = "https://au.finance.yahoo.com/quote/{}?p={}"

    stock = input("Enter stock name (e.g. TSLA): ")

    response = requests.get(stock_url.format(stock, stock))

    if choice == 'l':

        print("Press ctrl+c to stop program")
        
        while True:
            priceTracker()
            time.sleep(1)
            
    elif choice == 'c':
        priceTracker()

    else:
        print("Invalid input")
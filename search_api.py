from wsgiref import headers
import cloudscraper
# import requests
# import cfscrape

scraper = cloudscraper.create_scraper() 

def searchApi():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    url = "https://rocket-trade.shop/giveaway/twoctane-take"
    response = scraper.get(url)
    print(response)
    
    # session = requests.Session()
    # session.headers = headers
    # scraper = cfscrape.create_scraper(sess=session)
    # s = scraper.post(url)
    # print(s)

searchApi()
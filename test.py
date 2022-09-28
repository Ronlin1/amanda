from pycoingecko import CoinGeckoAPI
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

cg = CoinGeckoAPI()
import requests

"""GET COIN PRICE"""
id= "bitcoin"
c_p = cg.get_price(ids='bitcoin', vs_currencies='usd')
c_p = c_p.get(id).get("usd")
# print(c_p)

"""GET COIN LIST"""
c_l = cg.get_coins_list()
for i in range(20):
    # print(c_l[i]['name'])
    # print(c_l[i])
    pass
    

"""COIN INFO FROM COIN M"""
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
api = "7a08b482-9d34-4681-9c9b-688e9f866e3f"

parameters = {
  'start':'1',
  'limit':'200',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api,
}

session = Session()
session.headers.update(headers)



try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    
    top_200_coins = list()
    for i in range(200):
        d = data["data"][i]["name"]
        # d = f'{i} {d[i]["name"]} {d[i]["symbol"]}'
        # print(d)
    
    for i in range(10):
        d = data["data"]
        # d = f'{i} {d[i]["name"]} {d[i]["symbol"]}'
        # print(d)
        # pass
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
    


"""20 nfts"""
top_nfts = "https://api.coingecko.com/api/v3/nfts/list"

r = requests.request("GET", top_nfts)
for i in range(20):
    if r.status_code == 200:
        data = r.json()
        # print(i, data[i]["name"], ':', data[i]["asset_platform_id"])
        nft = f'{i} {data[i]["name"]} : {data[i]["asset_platform_id"]}'
        # print(nft)

"""LEARN --"""
learn = cg.get_coin_by_id(id="bitcoin")
learn = learn["description"]["en"].split()[:100]
learn_d = " ".join(learn)
# print(learn_d)


"""" whales"""
w = cg.get_companies_public_treasury_by_coin_id(coin_id="ethereum")

w = w["companies"]
for i in range(10):
    pass
    print(w[i]["name"], "has", w[i]["total_holdings"], "coins")
# "companies" ["name"]["total_holdings"]
# print(w)


"""Global"""
stats = cg.get_global()
data_stats = f"""There are currently {stats["active_cryptocurrencies"]} active crypto currencies
                and {stats["ongoing_icos"]} ongoing ICOs with around {stats["markets"]} markets!"""
# print(data_stats)


"""TRENDS"""
# print()
t = cg.get_search_trending()
for i in range(5):
    t_data = f""" {i} {t["coins"][i]["item"]["name"]} with a market cap rank of {t["coins"][i]["item"]["market_cap_rank"]}"""
    # print(t_data)
    

"""EXCHANGES""" 
e = cg.get_exchanges_list() 
# print(e)
for i in range(10):
    e_data = f""" {i} :{e[i]["name"]} : Since {e[i]["year_established"]}: Origin:{e[i]["country"]} """
    # print(e_data)


"""PING"""
ping = cg.ping()
if ping["gecko_says"]:
    print("Server is Up!")



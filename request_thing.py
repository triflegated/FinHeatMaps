import requests, bs4
res = requests.get('https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch')
res.raise_for_status()
exampleSoup = bs4.BeautifulSoup(res.text, "html.parser")
elems = exampleSoup.select('span[class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"]')
for i in elems:
    print i 

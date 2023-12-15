import asyncio 
import httpx 
import json 
from prywatne import API_KEY

async def pobierz_wartosc_waluty(waluta):
    async with httpx.AsyncClient() as client:
        url = "http://api.nbp.pl/api/exchangerates/rates/c/" + waluta 
        response = await client.get(url)
        data_dict = json.loads(response.text)
        wartosc = data_dict['rates'][0]['ask']
        return wartosc
    
async def pobierz_wartosc_aktywa(nazwa_aktywa):
    async with httpx.AsyncClient() as client:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + nazwa_aktywa + '&interval=5min&apikey=' + API_KEY
        response = await client.get(url)
        data_dict = json.loads(response.text)
        latest_date = list(data_dict['Time Series (5min)'].keys())[0]
        return data_dict['Time Series (5min)'][latest_date]['4. close']

async def przewalutuj_aktywa(w, a):
    '''Przewalutowanie aktywów z tablicy "a" na podane waluty w tablicy "w"'''
    waluty = w
    aktywa = a
    tasks = [asyncio.create_task(pobierz_wartosc_waluty(waluta)) for waluta in waluty]
    tasks2 = [asyncio.create_task(pobierz_wartosc_aktywa(aktywa)) for aktywa in aktywa]
    wartosci = await asyncio.gather(*tasks)
    wartosci2 = await asyncio.gather(*tasks2)
    dolar_wartosc = await pobierz_wartosc_waluty("USD")
    for i in range(len(aktywa)):
        in_pln = float(wartosci2[i]) * float(dolar_wartosc)
        print("Aktywo: %s" % aktywa[i], end = " ")
        for j in range(len(waluty)):
            print("Wartość w %s: %.2f" % (waluty[j], in_pln / wartosci[j]), end = " ")
        print()
    
async def main():
    await przewalutuj_aktywa(["EUR", "CHF", "GBP"], ["IBM", "AAPL", "MSFT", "NATURAL_GAS", "WHEAT"])

asyncio.run(main())

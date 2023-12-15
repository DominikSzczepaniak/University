import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def get_inflation_data(url):
    response = requests.get(url)    
    soup = BeautifulSoup(response.text, 'html.parser')
    dane = soup.find_all("tr")
    lata = []
    for row in dane[4:27]:
        row_data = [i.replace('\xa0', '').replace(',', '.') if i.replace(',', '.').replace('.', '').isdigit() else i.strip() for i in row.text.split('\n')]               
        wynik = []
        for k in row_data:
            try:
                wynik.append(float(k))
            except:
                pass
        for i in range(1, len(wynik)):
            wynik[i] = wynik[i]-100
        lata.append(wynik)
    for i in range(len(lata)):
        lata[i][0] = int(lata[i][0])
    kolumny= ["Rok", "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    df = pd.DataFrame(lata, columns=kolumny)
    return df

def get_gold_prices():
    rok_2021 = requests.get("https://api.nbp.pl/api/cenyzlota/2021-01-01/2021-12-31/").json()
    rok_2022 = requests.get("https://api.nbp.pl/api/cenyzlota/2022-01-01/2022-12-31/").json()
    cena_2021 = []
    cena_2022 = []
    for i in rok_2021:
        data = i["data"].split("-")
        if(len(cena_2021) > 0 and cena_2021[-1][0] == data[1]):
            continue
        cena_2021.append((data[1], i["cena"]))
    for i in rok_2022:
        data = i["data"].split("-")
        if(len(cena_2022) > 0 and cena_2022[-1][0] == data[1]):
            continue
        cena_2022.append((data[1], i["cena"]))
    kolumny = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    df = pd.DataFrame(None, columns=kolumny)
    df = df._append(pd.Series([i[1] for i in cena_2021], index=kolumny), ignore_index=True)
    df = df._append(pd.Series([i[1] for i in cena_2022], index=kolumny), ignore_index=True)
    index_names = ["2021", "2022"]
    df.index = index_names
    return df



def predict_future_values(df):
    X = np.arange(len(df)).reshape(-1, 1)
    y = df.iloc[:, 1:].mean(axis=1)
    
    model = LinearRegression()
    model.fit(X, y)
    future_months = np.arange(1, 13).reshape(-1, 1)
    future_values = model.predict(future_months)
    return future_months, future_values

url = 'https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-pot-inflacja-/miesieczne-wskazniki-cen-towarow-i-uslug-konsumpcyjnych-od-1982-roku/'



df = get_inflation_data(url)
df["Rok"] = df["Rok"].astype(int)
years = df[df["Rok"].isin([2021, 2022])]
fig, axes= plt.subplots(nrows=3, ncols=1, figsize=(14, 8))
# inflacja
for i in range(0, len(years)):
    years.iloc[i, 1:].astype(float).plot(ax=axes[0], label=years.iloc[i, 0])

axes[0].set_xticks(range(len(years.columns[1:])))
axes[0].set_xticklabels(years.columns[1:], rotation=45, ha='right')
axes[0].set_title('Miesięczne wskaźniki dla poszczególnych lat')
axes[0].set_xlabel('Miesiące')
axes[0].set_ylabel('Wskaźniki')
axes[0].legend()

#złoto
gold_df = get_gold_prices()
for i in range(0, len(gold_df)):
    gold_df.iloc[i, :].astype(float).plot(ax=axes[1], label=gold_df.index[i])

axes[1].set_xticks(range(len(gold_df.columns)))
axes[1].set_xticklabels(gold_df.columns, rotation=45, ha='right')
axes[1].set_title('Miesięczne ceny złota')
axes[1].set_xlabel('Miesiące')
axes[1].set_ylabel('Cena złota')
axes[1].legend()

#przewidywana wartość inflacji
miesiace, wartosci = predict_future_values(df)
axes[2].plot(miesiace, wartosci, label="Przewidywane wartości")
axes[2].set_xticks(range(1, 13))
axes[2].set_xticklabels(df.columns[1:], rotation=45, ha='right')
axes[2].set_title('Przewidywane wartości inflacji w kolejnych miesiącach 2023 roku')
axes[2].set_xlabel('Miesiące')
axes[2].set_ylabel('Wskaźniki')
axes[2].legend()


plt.tight_layout()
plt.show()
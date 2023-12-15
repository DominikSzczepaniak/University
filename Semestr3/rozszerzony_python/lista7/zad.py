import time
import os
import sys
from urllib.request import urlopen, Request
import threading

def sledz_strone(website_url):
    for i in range(ilosc):
        odczytana = urlopen(urls[i]).read().decode('utf-8').split()
        for j in range(len(odczytana)):
            try:
                if odczytana[j] != czytane[i][j]:
                    print("Zmiana na stronie ", websites[i], " z ", czytane[i][j], " na ", odczytana[j])
            except:
                pass
        czytane[i] = odczytana

websites = []
ilosc = int(input("Ile stron chcesz monitorowac: "))
for i in range(ilosc):
    website = input("Strona nr " + str(i+1) + ": ")
    websites.append(website)
try:
    urls = [Request(i, headers={'User-Agent': 'Mozilla/5.0'}) for i in websites]
except:
    print("Jedna ze stron nie istnieje")
    exit()
czytane = [urlopen(i).read().decode('utf-8').split() for i in urls]

while(True):
    if(sys.platform == 'win32'): os.system('cls')
    if(sys.platform == 'linux' or sys.platform == 'darwin'): os.system('clear')
    for i in czytane:
        threading.Thread(target=sledz_strone, args=(i,)).start()
    time.sleep(60)

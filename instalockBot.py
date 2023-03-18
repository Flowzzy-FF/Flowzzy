import json
from requests import session
from valclient.client import Client
import colorama
import webbrowser
from colorama import Fore, Back, Style
colorama.init()
import random,time, sys
from colorama import *
from Pydate import pydate
pd = pydate.PyDate()

raw_link = "https://raw.githubusercontent.com/Flowzzy-FF/Flowzzy/main/version.json"
klasörüm = f"C:\\Users\\...\\Desktop\\Yeni klasör"
pd = pydate.PyDate(path=klasörüm,rawlink=raw_link)

if pd.create_version_file(0.1):
    print("oluşturuldu")
else:
    print("zaten vardı")

if pd.isUpdate:
    print("güncel")
else:
    print("güncel değil")
    pd.downloadLink(url="https://raw.githubusercontent.com/Flowzzy-FF/Flowzzy/main/instalockBot.py",extension="..py")
    pd.writeNewVersion()

init(autoreset=True)
fr = Fore.RED
fb = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
 
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
 
    x = """
  ______ _                               _ _ 
 |  ____| |                             | | |
 | |__  | | _____      ___________   _  | | |
 |  __| | |/ _ \ \ /\ / /_  /_  / | | | | | |
 | |    | | (_) \ V  V / / / / /| |_| | |_|_|
 |_|    |_|\___/ \_/\_/ /___/___|\__, | (_|_)
                                  __/ |      
                                 |___/       

       Discord Adresi - https://discord.gg/QghW942Va9 -
 
                                          """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.06)
logo()




print(Fore.YELLOW)
playerRegion = input('Oynadığın Server Ör.( EU ): ').lower()
client = Client(region=playerRegion)
client.activate()
valid = False
agents = {}
seenMatches = []

with open('data.json', 'r') as f:
    agents = json.load(f)

while valid == False:
    try: 
        preferredAgent = input("Ajan Seç Ör. ( Jett ): ").lower()
        if (preferredAgent in agents['agents'].keys()):
            valid = True
        else:
            print("Geçersiz Ajan")
    except:
        print("Veri Hatası")

print("Ajan Seçimi Başarılı,Bekleniyor...")
while True:
    try:
        sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
        if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
            print('Ajan Seçimi Bulundu')
            client.pregame_select_character(agents['agents'][preferredAgent])
            client.pregame_lock_character(agents['agents'][preferredAgent])
            seenMatches.append(client.pregame_fetch_match()['ID'])
            print('Ajan kitlendi ' + preferredAgent.capitalize())
    except Exception as e:
        print('', end='') 
        print("CMD Ekranını Kapatıp Tekrardan Seçim Yapınız")
        print('', end='') #By Flowzzy

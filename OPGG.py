import requests,json


def requestDatos(region,NombreInvocador):
   URL="https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+NombreInvocador+"?api_key=RGAPI-21ba34f0-bead-4557-b44c-c42a21921409"
   peticion= requests.get(URL)
   return peticion.json()

def requestDatosRanked(region,ID):
    URL="https://"+region+".api.riotgames.com/lol/league/v4/positions/by-summoner/"+ID+"?api_key=RGAPI-21ba34f0-bead-4557-b44c-c42a21921409"
    peticion2=requests.get(URL)
    return peticion2.json()

def main():
    print("Que pasa manin")
    print("Mete las siguente regiones: ")
    print("RU,KR,BR1,OC1,JP1,NA1,EUN1,EUW1,TR1,LA1,LA2")
    region=""
    while(region!="RU" and region!="KR" and region!="BR1" and region!="OC1" and region!="JP1" and region!="NA1" and region!="EUN1" and region!="EUW1" and region!="TR1" and region!="LA1" and region!="LA2"):
        region=(str)(input("Mete la region de tu cuenta: "))
    NombreInvocador=(str)(input("Mete el nombre de tu cuenta: "))
    petionJSON=requestDatos(region,NombreInvocador)
    ID=petionJSON['id']
    ID2=str(ID)
    petionJSON2=requestDatosRanked(region,ID2)
    for x in petionJSON2:
        print (x['tier'],(x['rank']))
        print ("LP: ",(x['leaguePoints']))
        print ("Wins: ",(x['wins']))
        print ("Lost: ",(x['losses']))
        print ("Cola: ",(x['queueType']))
if __name__=="__main__":
    main()



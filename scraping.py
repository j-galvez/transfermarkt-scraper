import csv
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

#-----------
#EDITA URL DE RESPUESTA AQUÍ PARA HACER SCRAPING
#EDIT URL RESPONSE HERE TO SCRAPE
#----------
#response = requests.get('https://www.transfermarkt.com/fifa-klub-wm/teilnehmer/pokalwettbewerb/KLUB/saison_id/2024', headers=headers) #fifa club world cup
#response = requests.get('https://www.transfermarkt.com/liga-de-primera/startseite/wettbewerb/CLPD', headers=headers) #chilean premier league
response = requests.get('https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1', headers=headers) #english premier league


#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

#----------
#limitar el número de filas a scrapear, por defecto 3. al quitar limit se scrapearán todas las filas
#limit the number of rows to scrape, by default 3. removing limit will scrape all
filtro = soup.find_all("tr" ,class_=["odd", "even"], limit = 3)  # NUMERO DE CLUBES A SCRAPEAR / NUMBER OF TEAMS TO SCRAPE


listaEquipos = []
links = []
#----------
#get all teams names and their urls
#Conseguir nombre de los clubes y sus urls

for i in filtro:
    tdTag = i.find("td", class_="zentriert no-border-rechts")
    if tdTag:
        aTag = tdTag.find("a")
        if aTag and "title" in aTag.attrs and "href" in aTag.attrs:
            nombreEquipo = aTag["title"]
            linkEquipo = aTag["href"]
            listaEquipos.append(nombreEquipo)
            links.append(linkEquipo)
hora = datetime.now().strftime("%H:%M:%S")
#print(listaEquipos)
todosLosJugadores=[]
#--------
#convert relative URLs to absolute URLs
#convertir URLs relativos a URLs completas 
urlBase = "https://www.transfermarkt.com"
for equipo, link in zip(listaEquipos,links):
    hora = datetime.now().strftime("%H:%M:%S")
    print(f"--Scraping players from: {equipo}-- |{hora}")
    url = urlBase + link
    #print(url)
    
    equipoResponse = requests.get(url, headers=headers)
    if equipoResponse.status_code != 200:
        print(f"error {equipoResponse.status_code} al acceder a {url}")
        continue
    equipoSoup = BeautifulSoup(equipoResponse.text, 'html.parser')
    time.sleep(10) #esperar 10 segundos entre requests / wait 10 seconds between requests
    
    
    #se limita el número de jugadores a scrapear, por defecto 2. al quitar limit se scrapearán todos los jugadores
    #the number of players to scrape is limited, by default 2. removing limit will
    filtro = equipoSoup.find_all("tr", class_=["odd", "even"], limit = 2) #NUMERO DE JUGADORES A SCRAPEAR / NUMBER OF PLAYERS TO SCRAPE
    
    
    for i in filtro:
        tdTag = i.find("td", class_="hauptlink")
        aTag = tdTag.find("a") if tdTag else None
        tdTag2 = i.find("td", attrs={"title": True})
        tdTag3 = i.find("td", class_="zentriert")
        
        if aTag and tdTag2 and tdTag3:
            nombre = aTag.get_text(strip=True)
            posicion = tdTag2["title"]
            nCamiseta = tdTag3.get_text(strip=True)
            print(f"-> {nombre} - {posicion}")
            todosLosJugadores.append({
                "team": equipo,
                "name": nombre,
                "shirt": nCamiseta,
                "position": posicion
                
            })
            
            
            #nombreJugador = aTag.get_text(strip=True)
            #nombreJugadores.append(nombreJugador)

    
    
  
#print(todosLosJugadores)




#------
#guardar jugadores en archivo csv
#save players to a csv file
with open ("players.csv", mode="w", newline='', encoding="utf-8") as archivo: 
    campos = ["team", "name", "shirt", "position"]
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    
    for jugador in todosLosJugadores:
        writer.writerow(jugador)
print("--All PLAYERS EXPORTED--", hora)
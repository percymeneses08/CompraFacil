from bs4 import BeautifulSoup
import requests
import urllib.request
import re

url2 = "https://www.metro.pe/lacteos"
response2 = requests.get(url2) #conexion
soup2 = BeautifulSoup(response2.text, "html.parser") #Haciendo el soup Object
div_principal = soup2.find('div', {'class':'main'}) #Busco en la clase main

#Según el tutorial en stackoverflow
#Lo meteremos a una lista
links_leche = []
for div in div_principal.find_all("div", {"class":"product-item__info"}): #Encuentra todas las clases de info de producto
    for link in div.select("a.product-item__name"): #Seleccioname los links
        print(link['href'])
        links_leche.append(link['href'])
        
def scrapeando_ando(url): #Generalizamos la funcion
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    nombre_ = soup.find('div', {'class': 'name-mobile mobile'})
    nombre3 = nombre_.div(string=True)
    precio_ = soup.find('div', {'class':'plugin-preco'})
    precio_2 = precio_.find('strong', {'class':'skuBestPrice'}).text
    return nombre3[0], precio_2

list_nombres = []
list_precios = []
for links in links_leche:
    nombre, precio = scrapeando_ando(links)
    list_nombres.append(nombre)
    list_precios.append(precio)

#Para convertir a JSON, instalando pandas.
import pandas as pd

data = {'Producto': list_nombres, 
        'Price': list_precios}

df = pd.DataFrame(data)
df['Supermercado'] = 'Metro'
df['Precio_float'] = df.Price.str.extract('(\d+\.\d+)')

export = df.to_json('export_dataframe.json')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

import re
#import pyrebase
import pandas as pd

# with open('simple.html') as html_file:
#	soup=BeutifulSoup(html_file,'lxml')
#firebaseConfig = {
   # "apiKey": "AIzaSyDLEJwEAUgaoLWeRGI4HNe5FXq9H2A_3sg",
    #"authDomain": "scrap-python.firebaseapp.com",
    #"databaseURL": "https://scrap-python.firebaseio.com",
    #"projectId": "scrap-python",
   # "storageBucket": "",
  #  "messagingSenderId": "543438125290",
 #   "appId": "1:543438125290:web:735b428ae64747c8"
#};
#firebase = pyrebase.initialize_app(firebaseConfig)
#datos = firebase.database()
#datos.child().update({"bola": "teste"})
#datos.child().update({"variable": "12345"})

# source = requests.get('https://www.wong.pe/busca/?ft=leche')
# soup = BeautifulSoup(source.text,'xml')
url2 = "https://www.wong.pe/busca/?ft=leche"
response2 = requests.get(url2)  # conexion
soup2 = BeautifulSoup(response2.text, "html.parser")  #
div_principal = soup2.find('div', {'class': 'main'})  # Busco en la clase main

# nombre=soup.findAll("div",{"class":"fn productName  Leche-Evaporada-Gloria-Azul-Pack-6-Unid-x-400-g "})
# precio=soup.findAll("strong",{"class":"skuBestPrice"})

links_leche = []
for div in div_principal.find_all("div", {"class": "product-item__bottom"}):
    for link in div.select("a.product-item__name"):  # Seleccioname los links
        # links_leche.append(link['href'])
        print(link['href'])
        links_leche.append(link['href'])


# precio=soup.span(string=True)

# print(span.prettify())

# ID DE CADA PRODUCTO LACTEO
# id=8507
# num1=soup.find("div",{"class":"product-item product-item--8507 gotten-product-item-data" , type:'data-id'})

def scrapeando_ando(url):  # generalizamos el jalado de data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    nombre = soup.find('div', {'class': 'name-mobile mobile'})
    nombre1 = nombre.div(string=True)

    # for j in nombre:
    #	array2=j.contents[0]
    precio = soup.find('div', {'class': 'plugin-preco'})
    precio1 = precio.find('strong', {'class': 'skuBestPrice'}).text
    return (nombre1[0], precio1)


list_nombre = []
list_precio = []

for links in links_leche:
    nuevo_nombre, nuevo_precio = scrapeando_ando(links)
    list_nombre.append(nuevo_nombre)
    list_precio.append(nuevo_precio)

data = {'Nombre': list_nombre,
        'Precio': list_precio}

df = pd.DataFrame(data)
df['Supermercado'] = 'Wong'
df['Precio_float'] = df.Precio.str.extract('(\d+\.\d+)')

export = df.to_json('export_dataframe.json')


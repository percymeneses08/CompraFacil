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

print('-------------------------------Otra Alternativa------------------------------------------------')

def agrega_x_num(num):
    x = 1
    lista_de_urls = []
    for i in range(1,num):
        x = str(x)
        url_conjunto = 'https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber='+x+'&&fq=C%3a%2f1001436%2f'
        lista_de_urls.append(url_conjunto)
        x = int(x)
        x+=1
    return lista_de_urls

lista_de_25 = agrega_x_num(26)

#Tengo que ubicar dónde está la info: los datos que busco son nombre, precio regular, marca, codigo de producto, precio online.
#Buscaremos primero el nombre y la marca. Lo formalizaremos en una función para luego aplicarle un for loop a los links
lista_nombres = []
lista_marcas = []
def get_names_and_brands(lista_links):
    global lista_nombres
    global lista_marcas
    for link in lista_links:
        response = requests.get(link) #Conecto el link
        soup = BeautifulSoup(response.text,"html.parser") #Hago el objeto
        nombres_del_link = [div_prods.find('a',{'class':'product-item__name'}).text #Esto me botará una lista con los nombres
                  for div_prods in soup.find_all('div',{"class":"product-item__info"})] 
        marcas_del_link = [div_prods.find('div',{'class':'product-item__brand'}).text #Esto me botará una lista con las marcas
                for div_prods in soup.find_all('div',{"class":"product-item__info"})]
        lista_nombres = lista_nombres + nombres_del_link
        lista_marcas = lista_marcas + marcas_del_link


##EJECUTO LA FUNCION

get_names_and_brands(lista_de_25)        
        
## Las variables están en dos columnas, lista_nombres y lista_marcas


## AUN FALTA SACAR LOS PRECIOS
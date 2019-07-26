# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:19:59 2019

@author: PBenavides
"""

from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

#Definamos la primera función para generar links.
def hazme_los_links(num, x1 = 'https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=', 
                 x2 = '&&fq=C%3a%2f1001436%2f'):
    x = 1
    lista_de_urls = []
    for i in range(1,num):
        x = str(x) #en string para que se sume
        url_conjunto = x1 + x + x2
        lista_de_urls.append(url_conjunto)
        x = int(x) #En integer para que itere
        x+=1
    return lista_de_urls
"Ahora vamos a generar todos los links que queramos"

links_de_lacteos = hazme_los_links(26)
links_de_leche = hazme_los_links(3,x1 = 'https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                              x2 = '&&fq=C%3a%2f1700%2f1001282%2f')
links_de_azucar = hazme_los_links(5, x1 = 'https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                               x2 = '&&fq=C%3a%2f1001253%2f1001258%2f')
links_de_aceites = hazme_los_links(4, x1 = 'https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                x2='&&fq=C%3a%2f1700%2f1709%2f')
links_de_arroz = hazme_los_links(3, x1='https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                 x2='&&fq=C%3a%2f1700%2f1001282%2f')


#Tengo que ubicar dónde está la info: los datos que busco son nombre, precio regular, marca, codigo de producto, precio online.
#Buscaremos primero el nombre y la marca. Lo formalizaremos en una función para luego aplicarle un for loop a los links
def get_names_brands_prices(lista_links, categoria = 'Lacteos'):
    lista_nombres = []
    lista_marcas = []
    lista_precios = []
    for link in lista_links:
        response = requests.get(link) #Conecto el link
        time.sleep(5)
        soup = BeautifulSoup(response.text,"html.parser") #Hago el objeto
        nombres_del_link = [div_prods.find('a',{'class':'product-item__name'}).text #Esto me botará una lista con los nombres
                  for div_prods in soup.find_all('div',{"class":"product-item__info"})] 
        marcas_del_link = [div_prods.find('div',{'class':'product-item__brand'}).text #Esto me botará una lista con las marcas
                for div_prods in soup.find_all('div',{"class":"product-item__info"})]
        precios_del_link_online = [div1.find('span',{'class':"product-prices__value product-prices__value--best-price"}).text 
                                   for div1 in soup.find_all('div',{'class':['product-prices__price product-prices__price--better-price',
                                                             'product-prices__price product-prices__price--regular-price']})]
        lista_nombres = lista_nombres + nombres_del_link
        lista_marcas = lista_marcas + marcas_del_link
        lista_precios = lista_precios + precios_del_link_online
    #Tendremos las listas llenas de datos, las pondremos en un dataframe.
    dicc = {'Producto':lista_nombres,'Marca':lista_marcas,'Categoría':categoria,
            'Supermercado':'Metro','Precio':lista_precios}
    df1 = pd.DataFrame(dicc)
    df1['Precio_float'] = df1.Precio.str.extract('(\d+\.\d+)')
    return df1

"Ahora viene el SCRAPING"
df_lacteos = get_names_brands_prices(links_de_lacteos)
df_arroz = get_names_brands_prices(links_de_arroz,categoria = 'Arroces')
df_azucar = get_names_brands_prices(links_de_azucar, categoria = 'Azucar')
df_aceites = get_names_brands_prices(links_de_aceites, categoria = 'Aceites')

df_metro_final = df_lacteos.append([df_arroz,df_azucar,df_aceites], ignore_index=True)
export = df_metro_final.to_json('df_final_metro.json')
        
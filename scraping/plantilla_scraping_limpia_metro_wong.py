# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:19:59 2019

@author: PBenavides
"""

from bs4 import BeautifulSoup
import requests
import time

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
"Acá va la función"
#Tengo que ubicar dónde está la info: los datos que busco son nombre, precio regular, marca, codigo de producto, precio online.
#Buscaremos primero el nombre y la marca. Lo formalizaremos en una función para luego aplicarle un for loop a los links
lista_nombres = []
lista_marcas = []
lista_precios = []
def get_names_brands_prices(lista_links):
    global lista_nombres
    global lista_marcas
    global lista_precios
    for link in lista_links:
        response = requests.get(link) #Conecto el link
        time.sleep(5)
        soup = BeautifulSoup(response.text,"html.parser") #Hago el objeto
        nombres_del_link = [div_prods.find('a',{'class':'product-item__name'}).text #Esto me botará una lista con los nombres
                  for div_prods in soup.find_all('div',{"class":"product-item__info"})] 
        marcas_del_link = [div_prods.find('div',{'class':'product-item__brand'}).text #Esto me botará una lista con las marcas
                for div_prods in soup.find_all('div',{"class":"product-item__info"})] 
        precios_del_link_online = [div1.find('span',{'class':"product-prices__value product-prices__value--best-price"}).text 
                                   for div1 in soup_prueba.find_all('div',{'class':['product-prices__price product-prices__price--better-price',
                                                             'product-prices__price product-prices__price--regular-price']})]
        lista_nombres = lista_nombres + nombres_del_link
        lista_marcas = lista_marcas + marcas_del_link
        lista_precios = lista_precios + precios_del_link_online
        
get_names_brands_prices(lista_de_25)

        
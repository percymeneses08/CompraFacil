# -*- coding: utf-8 -*-
import requests;
import bs4;
import re;
from bs4 import BeautifulSoup;
import pandas as pd;

import json;

diccionario_final={};

def Tottus():

    # --------------------#
    # DEFINIENDO VARIABLES#
    # --------------------#

    ids = [];

    producto1 = [];
    producto1_2 = [];

    producto_sub = [];
    producto_precio = [];
    prod_prec2 = [];
    prod_prec = [];

    div_url = [];

    # ------------------------#
    # OBTENIENDO TODOS LOS URL#
    # ------------------------#

    def all_url():

        url2 = "https://www.tottus.com.pe/tottus/browse/";
        response2 = requests.get(url2);
        soup2 = BeautifulSoup(response2.text, "html.parser");  # Haciendo el soup Object
        div_principal = soup2.findAll('div', {'data-level': '3'})

        for i in div_principal:

            for j in i.findAll('a'):

                temp = j.attrs['href'];

                if (temp != '#'):
                    div_url.append(temp);

        return div_url;

    def get_Scroll_URLS(lista,x1="https://www.tottus.com.pe/tottus/productListFragment/Aceites/1.01?No=",x2="&Nrpp=&currentCatId=1.01"):

        lista_de_urls = []

        for i in lista:

            url_conjunto = x1 + str(i) + x2

            lista_de_urls.append(url_conjunto)

        return lista_de_urls;

    #------------------------------#
    #OBTENIENDO CONTENIDO DE LA URL#
    #------------------------------#

    def get_content_url(varurl):

        r = requests.get(varurl);

        soup = bs4.BeautifulSoup(r.text, 'lxml');

        return soup;

    #------------------------------------#
    #OBTENIENDO LISTA DE IDS DE PRODUCTOS#
    #------------------------------------#

    def get_id(soup):

        ids=[];

        form=soup.findAll('form',{"name":"addToCart"});

        total_ids=0;

        for i in form:

            total_ids+=1;

            temp=i.attrs['id'];

            ids.append(temp[9:]);

        return ids;

    #---------------------------------------#
    #OBTENIENDO TODOS LOS DATOS DEL PRODUCTO#
    #---------------------------------------#

    def get_all(lista_url,categoriaParam='Lacteos'):

        producto1 = [];
        prod_prec2 = [];
        producto1_2 = []

        var = "";

        for url in lista_url:

            soup = get_content_url(url);
            ids = get_id(soup);

            for i in ids:

                var = "item-product-caption_" + i;

                prod = soup.find('div', {"id": var});

                producto = prod.find('h5');

                prod_prec1 = prod.find('span', {'class': 'active-price'});

                prod_prec2.append(prod_prec1.find('span', {'class': ['red', '']}).text[12:]);  # PRECIO

                producto1.append(producto.find('div').text[13:] + " " +prod.find('div', {"class": "statement"}).text);  # TITULO

                producto1_2.append(producto.find('span').text);  # MARCA

            print("Scrapping..."+ url);

        data = {'Producto': producto1, 'Marca': producto1_2, 'Categoria': categoriaParam,'Supermercado':'Tottus', 'Precio': prod_prec2};

        df = pd.DataFrame(data);
        df['Precio_float'] = df.Precio.str.extract('(\d+\.\d+)' );

        print(df)

        return df; #RETORNO EL DATAFRAME DE LA CATEGORIA ESPECIFICADA

    # -----------------------------------------------#
    #       OBTENIENDO LA LISTA DE LOS URL SCROLL    #
    # -----------------------------------------------#

    listas_urls_aceites=get_Scroll_URLS([0,15,30,45,60,75]);
    listas_urls_arroz = get_Scroll_URLS([0, 15, 30, 45],"https://www.tottus.com.pe/tottus/productListFragment/Arroz/1.02?No=","&Nrpp=&currentCatId=1.02");
    listas_urls_lacteos = get_Scroll_URLS([0, 15],"https://www.tottus.com.pe/tottus/productListFragment/Leche-Evaporada/13.01?No=","&Nrpp=&currentCatId=13.01");
    listas_urls_azucar = get_Scroll_URLS([0,15,30],"https://www.tottus.com.pe/tottus/productListFragment/Azúcar-Sustitutos/1.09.01?No=","&Nrpp=&currentCatId=1.09.01");

    #-----------------------------------------------#
    #COLOCANDO EL LINK DE LOS PRODUCTOS QUE DESEEMOS#
    #-----------------------------------------------#

    df_lacteos=get_all(listas_urls_lacteos,'Lacteos');
    df_arroz=get_all(listas_urls_arroz,'Arroces');
    df_aceites=get_all(listas_urls_aceites,'Aceites');
    df_azucar=get_all(listas_urls_azucar,'Azucar');

    #-----------------------------------------------#
    #       AGREGANDO CADA CATEGORIA A UNA LISTA    #
    #-----------------------------------------------#

    df_totus_final=df_lacteos.append([df_arroz,df_azucar,df_aceites],ignore_index=True);

    #-----------------------------------------------------#
    #       TRANSFORMANDO AL FORMATO JSON QUE QUEREMOS    #
    #-----------------------------------------------------#

    results = {}

    for key, df_gb in df_totus_final.groupby('Categoria'):

        temp = df_gb.to_dict('records')

        results[str(key)] = {(key + str(idx)): ele for idx, ele in enumerate(temp)}

    #--------------------------------#
    #   AGREGANDO EL DICC A TOTTUS   #
    #--------------------------------#

    return results

def Metro():

    # -----------------------------------------------#
    #           FUNCION PARA GENERAR LINKS           #
    # -----------------------------------------------#

    def hazme_los_links(num,
                        x1='https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                        x2='&&fq=C%3a%2f1001436%2f'):
        x = 1
        lista_de_urls = []

        for i in range(1, num):

            x = str(x)  # en string para que se sume

            url_conjunto = x1 + x + x2

            lista_de_urls.append(url_conjunto)

            x = int(x)  # En integer para que itere

            x += 1

        return lista_de_urls

    # -----------------------------------------------#
    #      OBTENIENDO TODOS LOS DATOS DEL PRODUCTO   #
    # -----------------------------------------------#

    def get_names_brands_prices(lista_links, categoria='Lacteos'):

        lista_nombres = []
        lista_marcas = []
        lista_precios = []

        for link in lista_links:

            response = requests.get(link)  # Conecto el link

            soup = BeautifulSoup(response.text, "html.parser")  # Hago el

            nombres_del_link = [div_prods.find('a', {'class': 'product-item__name'}).text
                                # Esto me botará una lista con los nombres
                                for div_prods in soup.find_all('div', {"class": "product-item__info"})]

            marcas_del_link = [div_prods.find('div', {'class': 'product-item__brand'}).text
                               # Esto me botará una lista con las marcas
                               for div_prods in soup.find_all('div', {"class": "product-item__info"})]

            precios_del_link_online = [
                div1.find('span', {'class': "product-prices__value product-prices__value--best-price"}).text
                for div1 in soup.find_all('div', {'class': ['product-prices__price product-prices__price--better-price',
                                                            'product-prices__price product-prices__price--regular-price']})]

            lista_nombres = lista_nombres + nombres_del_link
            lista_marcas = lista_marcas + marcas_del_link
            lista_precios = lista_precios + precios_del_link_online

            print("Scrapping..." + link);

        #-----------------------------------------------------------#
        #TENDREMOS LAS LISTAS LLENAS PARA COLOCARLAS EN UN DATAFRAME#
        # -----------------------------------------------------------#

        dicc = {'Producto': lista_nombres, 'Marca': lista_marcas, 'Categoria': categoria,
                'Supermercado': 'Metro', 'Precio': lista_precios}

        df1 = pd.DataFrame(dicc)

        df1['Precio_float'] = df1.Precio.str.extract('(\d+\.\d+)')

        print(df1)

        return df1

    # -----------------------------------------------#
    #       OBTENIENDO LA LISTA DE LOS URL SCROLL    #
    # -----------------------------------------------#

    links_de_lacteos = hazme_los_links(26)
    links_de_leche = hazme_los_links(3,
                                     x1='https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                     x2='&&fq=C%3a%2f1700%2f1001282%2f')
    links_de_azucar = hazme_los_links(5,
                                      x1='https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                      x2='&&fq=C%3a%2f1001253%2f1001258%2f')
    links_de_aceites = hazme_los_links(4,
                                       x1='https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                       x2='&&fq=C%3a%2f1700%2f1709%2f')
    links_de_arroz = hazme_los_links(3,
                                     x1='https://www.metro.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                     x2='&&fq=C%3a%2f1700%2f1001282%2f')

    # -----------------------------------------------#
    #           COLOCANDO LOS LINKW QUE DESEEMOS     #
    # -----------------------------------------------#

    df_lacteos = get_names_brands_prices(links_de_lacteos)
    df_arroz = get_names_brands_prices(links_de_arroz, categoria='Arroces')
    df_azucar = get_names_brands_prices(links_de_azucar, categoria='Azucar')
    df_aceites = get_names_brands_prices(links_de_aceites, categoria='Aceites')

    df_metro_final = df_lacteos.append([df_arroz, df_azucar, df_aceites], ignore_index=True)

    results = {}

    for key, df_gb in df_metro_final.groupby('Categoria'):
        temp = df_gb.to_dict('records')
        results[str(key)] = {(key + str(idx)): ele for idx, ele in enumerate(temp)}

    return results

    #--------------------------------#
    #   AGREGANDO EL DICC A WONG   #
    #--------------------------------#

def Wong():

    # -----------------------------------------------#
    #           FUNCION PARA GENERAR LINKS           #
    # -----------------------------------------------#

    def hazme_los_links(num,
                        x1='https://www.wong.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                        x2='&&fq=C%3a%2f1001436%2f'):
        x = 1
        lista_de_urls = []

        for i in range(1, num):

            x = str(x)  # en string para que se sume

            url_conjunto = x1 + x + x2

            lista_de_urls.append(url_conjunto)

            x = int(x)  # En integer para que itere

            x += 1

        return lista_de_urls

    # -----------------------------------------------#
    #      OBTENIENDO TODOS LOS DATOS DEL PRODUCTO   #
    # -----------------------------------------------#

    def get_names_brands_prices(lista_links, categoria='Lacteos'):

        lista_nombres = []
        lista_marcas = []
        lista_precios = []

        for link in lista_links:

            response = requests.get(link)  # Conecto el link

            soup = BeautifulSoup(response.text, "html.parser")  # Hago el

            nombres_del_link = [div_prods.find('a', {'class': 'product-item__name'}).text
                                # Esto me botará una lista con los nombres
                                for div_prods in soup.find_all('div', {"class": "product-item__info"})]

            marcas_del_link = [div_prods.find('div', {'class': 'product-item__brand'}).text
                               # Esto me botará una lista con las marcas
                               for div_prods in soup.find_all('div', {"class": "product-item__info"})]

            precios_del_link_online = [
                div1.find('span', {'class': "product-prices__value product-prices__value--best-price"}).text
                for div1 in soup.find_all('div', {'class': ['product-prices__price product-prices__price--better-price',
                                                            'product-prices__price product-prices__price--regular-price']})]

            lista_nombres = lista_nombres + nombres_del_link
            lista_marcas = lista_marcas + marcas_del_link
            lista_precios = lista_precios + precios_del_link_online

            print("Scrapping..." + link);

        #-----------------------------------------------------------#
        #TENDREMOS LAS LISTAS LLENAS PARA COLOCARLAS EN UN DATAFRAME#
        # -----------------------------------------------------------#

        dicc = {'Producto': lista_nombres, 'Marca': lista_marcas, 'Categoria': categoria,
                'Supermercado': 'Wong', 'Precio': lista_precios}

        df1 = pd.DataFrame(dicc)

        df1['Precio_float'] = df1.Precio.str.extract('(\d+\.\d+)')

        print(df1)

        return df1
    # -----------------------------------------------#
    #       OBTENIENDO LA LISTA DE LOS URL SCROLL    #
    # -----------------------------------------------#

    links_de_lacteos = hazme_los_links(40)
    links_de_leche = hazme_los_links(8,
                                     x1='https://www.wong.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                     x2='&&fq=C%3a%2f1001436%2f1001437%2f')
    links_de_azucar = hazme_los_links(5,
                                      x1='https://www.wong.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                      x2='&&fq=C%3a%2f1001253%2f1001258%2f')
    links_de_aceites = hazme_los_links(6,
                                       x1='https://www.wong.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                       x2='&&fq=C%3a%2f1700%2f1709%2f')
    links_de_arroz = hazme_los_links(3,
                                     x1='https://www.wong.pe/buscapagina?sl=19ccd66b-b568-43cb-a106-b52f9796f5cd&PS=18&cc=18&sm=0&PageNumber=',
                                     x2='&&fq=C%3a%2f1700%2f1001282%2f')

    # -----------------------------------------------#
    #           COLOCANDO LOS LINKW QUE DESEEMOS     #
    # -----------------------------------------------#

    df_lacteos = get_names_brands_prices(links_de_lacteos)
    df_arroz = get_names_brands_prices(links_de_arroz, categoria='Arroces')
    df_azucar = get_names_brands_prices(links_de_azucar, categoria='Azucar')
    df_aceites = get_names_brands_prices(links_de_aceites, categoria='Aceites')

    df_wong_final = df_lacteos.append([df_arroz, df_azucar, df_aceites], ignore_index=True)

    results = {}

    for key, df_gb in df_wong_final.groupby('Categoria'):
        temp = df_gb.to_dict('records')
        results[str(key)] = {(key + str(idx)): ele for idx, ele in enumerate(temp)}

    return results

#--------------------------------#
# AGREGANDO TODOA UN DICCIONARIO #
#--------------------------------#

Tottus2=Tottus();

Metro2=Metro();

Wong2=Wong();


diccionario_final={'Supermercados':{'Metro':Metro2,'Tottus':Tottus2,'Wong':Wong2 }};

#--------------------------------#
#       TRANSFORMANDO A JSON     #
#--------------------------------#


with open('Supermercados.json', 'w') as outfile:

    json.dump(diccionario_final, outfile)


print("FIN DEL SCRAPPING!!!")
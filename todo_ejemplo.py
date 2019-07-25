import requests;
import bs4;

import re;
from bs4 import BeautifulSoup;
import pandas as pd;

#DEFINIENDO VARIABLES#

ids=[];

producto1=[];
producto1_2=[];

array1_2=[];
array2_1=[];
array4=[];
array6=[];

producto_sub=[];
producto_precio=[];
prod_prec2=[];
prod_prec=[];

div_url=[];


#OBTENIENDO TODOS LOS URL#

def all_url():

    url2="https://www.tottus.com.pe/tottus/browse/";
    response2 = requests.get(url2);
    soup2 = BeautifulSoup(response2.text, "html.parser");  # Haciendo el soup Object
    div_principal = soup2.findAll('div',{'data-level':'3'})

    for i in div_principal:

        for j in i.findAll('a'):

            temp = j.attrs['href'];

            if (temp !='#'):
                div_url.append(temp);

    return div_url;

def get_content_url(varurl):

    r = requests.get('https://www.tottus.com.pe'+varurl);

    soup = bs4.BeautifulSoup(r.text, 'lxml');

    return soup;

#OBTENIENDO LISTA DE LOS ID DE LOS PRODUCTOS#

def get_id(soup):

    form=soup.findAll('form',{"name":"addToCart"});

    total_ids=0;

    for i in form:

        total_ids+=1;

        temp=i.attrs['id'];

        ids.append(temp[9:]);

    return ids;


# OBTENIENDO TITULO#

def get_title(producto1):

    total_productos = 0;

    for producto in producto1:

        total_productos += 1;

        for p in producto:
            array1 = p.contents[0];

        array1_2.append(array1[13:]);

    return array1_2;

# OBTENIENDO MARCA#

def get_mark(producto1_2):

    total_marcas = 0;

    for producto in producto1_2:

        total_marcas += 1;

        for p in producto:
            array2 = p.contents[0];

        array2_1.append(array2);

    return array2_1;


# OBTENIENDO SUBTITULO#

def get_sutitulo(producto_sub):

    total_subtitulos = 0;

    for producto in producto_sub:

        total_subtitulos += 1;

        for p in producto:
            array3 = p.contents[0];

        array4.append(array3);

    return array4;


# OBTENIENDO PRECIO#

def get_price(prod_prec2):

    total_precio = 0;

    for producto in prod_prec2:

        total_precio += 1;

        if producto != None:

            for p in producto:
                array5 = p;

            array6.append(array5[12:]);

    return array6;


#OBTENIENDO NOMBRE Y PRECIO DE CADA PRODUCTO#

div_url=all_url();

for url in div_url:

    prod_prec2=[];
    producto_sub=[];
    producto1=[]
    producto1_2=[];

    ids=[];

    soup = get_content_url(url);
    ids = get_id(soup);

    for i in ids:

        var = "item-product-caption_" + i;

        prod = soup.find('div', {"id": var});

        producto = prod.find('h5');

        prod_prec1 = prod.find('span', {'class': 'active-price'});

        prod_prec2.append(prod_prec1.find('span', {'class': ['red', '']}));  # PRECIO

        producto_sub.append(prod.findAll('div', {"class": "statement"}));  # SUBTITULO

        producto1.append(producto.findAll('div'));  # TITULO

        producto1_2.append(producto.findAll('span'));  # MARCA

    titulo = get_title(producto1);
    marcas = get_mark(producto1_2);
    subtitulo = get_sutitulo(producto_sub);
    precio = get_price(prod_prec2);

    # Para convertir a JSON, instalando pandas

    data = {'Producto': titulo, 'Subtitulo': subtitulo, 'Price': precio, 'Marca': marcas}

    df = pd.DataFrame(data);

    df['Supermercado'] = 'Tottus'
    df['Precio_float'] = df.Price.str.extract('(\d+\.\d+)')

    print(df);

    export = df.to_json('tottus_todos_productos.json')

    # MOSTRANDO DATOS

    print(titulo);
    print(marcas);
    print(subtitulo);
    print(precio);

print("FIN DEL SCRAPPING!!!")











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

#OBTENIENDO NOMBRE Y PRECIO DE CADA PRODUCTO#

producto_dic = {};

supermarket_dic = {};

categoria_dic = {};

diccionario = {};

categorias=[];

data={};

div_url=all_url();

for url in div_url:

    prod_prec2=[];
    producto_sub=[];
    producto1=[]
    producto1_2=[];

    total_productos=[];
    total_marcas=[];
    total_subtitulos=[];
    total_precio=[]

    producto_dic = {};

    ids=[]

    categoria = "";

    var = url[15:];

    contador=0;

    for i in var:

        if (i != '/'):

            categoria = categoria + i;


        else:

            break

    soup = get_content_url(url);
    ids = get_id(soup)

    supermarket_dic = {};
    categoria_dic = {categoria:supermarket_dic};


    for i in ids:

        contador+=1;

        var = "item-product-caption_" + i;

        prod = soup.find('div', {"id": var});

        producto = prod.find('h5');

        prod_prec1 = prod.find('span', {'class': 'active-price'});

        prod_prec2.append(prod_prec1.find('span', {'class': ['red', '']}));  # PRECIO

        producto_sub.append(prod.findAll('div', {"class": "statement"}));  # SUBTITULO

        producto1.append(producto.findAll('div'));  # TITULO

        producto1_2.append(producto.findAll('span'));  # MARCA

        categorias.append(categoria);   #CATEGORIAS

        #AGREGADO#

        for p in producto.findAll('div'):
            array1 = p.contents[0];

        for p in producto.findAll('span'):
            array2 = p.contents[0];

        for p in prod.findAll('div', {"class": "statement"}):
            array3 = p.contents[0];

        if prod_prec1.find('span', {'class': ['red', '']}) != None:

            for p in prod_prec1.find('span', {'class': ['red', '']}):
                array5 = p;

        titulos=array1[13:]+" "+array2;
        marcas=array2;
        subtitulo=array3;
        precio=array5[12:];

        precio_float=float(precio);

        #AGREGANDO A LOS DICCIONARIO#

        producto_dic={'Producto': titulos, 'Precio': precio, 'Marca': marcas,'Precio_float': precio_float};

        supermarket_dic.setdefault(categoria+str(contador), producto_dic);

        print(categoria_dic);

        diccionario.setdefault('Tottus', categoria_dic);

        #print(diccionario);

        df = pd.DataFrame(diccionario);

        export = df.to_json('tottus_todos_productos.json')


print("FIN DEL SCRAPPING!!!")
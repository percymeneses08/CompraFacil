import requests;
import bs4;
import re;
from bs4 import BeautifulSoup

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

r=requests.get('https://www.tottus.com.pe/tottus/browse/Danbo/cat1500018');

soup=bs4.BeautifulSoup(r.text,'lxml');

#OBTENIENDO LISTA DE LOS ID DE LOS PRODUCTOS#

form=soup.findAll('form',{"name":"addToCart"});

for i in form:

    temp=i.attrs['id'];

    ids.append(temp[9:]);

#OBTENIENDO NOMBRE Y PRECIO DE CADA PRODUCTO#

for i in ids:

    var="item-product-caption_"+i;

    prod = soup.find('div', {"id": var});

    producto = prod.find('h5');

    prod_prec1=prod.find('span',{'class': 'active-price'});

    prod_prec2.append(prod_prec1.findAll('span',{'class':''}));#PRECIO

    producto_sub.append(prod.findAll('div' , {"class": "statement"}));#SUBTITULO

    producto1.append(producto.findAll('div'));#TITULO

    producto1_2.append(producto.findAll('span'));#MARCA

#OBTENIENDO TITULO#

for producto in producto1:

    for p in producto:

        array1=p.contents[0];

    array1_2.append(array1[13:]);

#OBTENIENDO MARCA#

for producto in producto1_2:

    for p in producto:

        array2 = p.contents[0];

    array2_1.append(array2);

#OBTENIENDO SUBTITULO#

for producto in producto_sub:

    for p in producto:

        array3 = p.contents[0];

    array4.append(array3);

#OBTENIENDO PRECIO#

for producto in prod_prec2:

    for p in producto:

        array5 = p.contents[0];

    array6.append(array5[12:]);

print("IDS:");
print(ids);

print("SUBTITULO:");
print(array4);

print("TITULO:");
print(array1_2);

print("MARCA:");
print(array2_1);

print("PRECIO:")
print(array6);








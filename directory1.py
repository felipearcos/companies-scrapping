#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import libraries
import requests
from bs4 import BeautifulSoup
import csv


#Request URL
page = requests.get("URL Directorio 1")

#Fetch webpage
soup = BeautifulSoup(page.content,"html.parser")
#print(soup.prettify())

empresa = {}

# Creación y escritura CSV
file = open('file.csv', 'wb')
writer = csv.writer(file)

# write title row
writer.writerow(['Nombre', 'URL', 'Imagen', 'Subtitulo', 'Categorias', 'Descripcion', 'Direccion', 'Caracteristicas'])

#Scraping Data
rows = soup.find_all("div", attrs={"class": "item-container"})
row = rows[0]

# DATOS
for row in rows:

    name = row.find("h3")
    if name is not None:
        name = name.getText().encode('utf-8')
    else:
        name = '-'

    link = row.find("a", attrs={"class": "main-link"})['href']
    if link is not None:
        link = link.encode('utf-8')
    else:
        link = '-'

    image_url = row.find("img")['src']
    if image_url is not None:
        image_url = image_url.encode('utf-8')
    else:
        image_url = '-'

    subtitle = row.find("span", attrs={"class": "subtitle"}).getText()
    if subtitle is not None:
        subtitle = subtitle.encode('utf-8')
    else:
        subtitle = '-'

    categories = row.find("div", attrs={"class": "item-categories"}).find_all("span", attrs={"class": "item-category"})
    category_list = []
    category_string = ''
    for category in categories:
        category_list.append(category.getText())
        category_string = category_string + ',' + category.getText()

    category_string = category_string.encode('utf-8')

    description = row.find("div", attrs={"class": "item-body"}).getText()
    if description is not None:
        description = description.encode('utf-8')
    else:
        description = '-'

    address = row.find("div", attrs={"class": "item-address"})
    if address is not None:
        print address
        address = address.encode('utf-8')
        print address
    else:
        address = '-'

    features = row.find("div", attrs={"class": "item-features"})
    feature_list = []
    feature_string = ''
    if features is not None:
        features = features.find_all("span", attrs={"class": "filter-hover"})

    for feature in features or []:
        feature.append(feature.getText())
        feature_string = feature_string + ',' + feature.getText()

    feature_string = feature_string.encode('utf-8')

    writer.writerow([name, link, image_url, subtitle, category_string, description, address, feature_string])

file.close()



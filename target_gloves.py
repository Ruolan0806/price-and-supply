import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup
import openpyxl
from pandas import ExcelWriter
name=[]
price=[]
stock = []

def parse(url):
    header = {
        'authority': 'redsky.target.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',

        'origin': 'https: // www.target.com',
    'referer': 'https: // www.target.com / s?searchTerm = hand + gloves',

    }
    response = requests.get(url, headers=header)

    text = response.content.decode('utf-8')
    data = response.json()
    # if response.status_code == 200:
    #     with open('target.html', 'w') as file:
    #         file.write(text)
    title=data['data']['product_summaries']
    # print(title)
    for i in title:
        item = i['item']['product_description']['title']
        p = i['price']['formatted_current_price']
        # print(p)
        name.append(item)
        price.append(p)
    # print(len(price))
    # print(price)


def parse2(url):
    header = {
        'authority': 'redsky.target.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',

        'origin': 'https: // www.target.com',
    'referer': 'https: // www.target.com / s?searchTerm = hand + gloves',

    }
    response = requests.get(url, headers=header)

    text = response.content.decode('utf-8')
    data = response.json()
    # if response.status_code == 200:
    #     with open('target2.html', 'w') as file:
    #         file.write(text)
    title = data['data']['product_summaries']
    for i in title:
        item = i['fulfillment']['store_options'][-1]['in_store_only']['availability_status']
        # print(item)
        stock.append(item)
    # print(len(stock))

def main():
    url = 'https://redsky.target.com/redsky_aggregations/v1/web/plp_client_v1' \
          '?key=eb2551e4accc14f38cc42d32fbc2b2ea&tcins=78362272%2C76150032%2C78362277%2C76150034%2' \
          'C11145990%2C78362269%2C76150033%2C78049834%2C76150031%2C78049835%2C76150030%2C79366526%2C79366525%' \
          '2C75490702%2C78644236%2C79179811%2C79' \
          '179815%2C79179822%2C78644126%2C78644061%2C78644092%2C79179818%2C79179823%2C79179849&pricing_store_id=214'
    parse(url)

    urls ='https://redsky.target.com/redsky_aggregations/' \
          'v1/web/plp_fulfillment_v1?key=eb2551e4accc14f38cc42d32' \
          'fbc2b2ea&tcins=11145990%2C75490702%2C76150030%2C76150031%2C76150032%2C76150033%2C76150034%2C7' \
          '8049834%2C78049835%2C78362269%2C78362272%2C78362277%2C78644061%2C78644092%2C78644126%2C78644236%2C7917981' \
          '1%2C79179815%2C79179818%2C79179822%2C79179823%2C79179849%2C79366525%2C79366526&store_id=2146&zip=33063' \
          '&state=FL&latitude=26.260&longitude=-80.190&scheduled_delivery_store_id=2146&fulfillment_test' \
          '_mode=grocery_opu_team_member_test'
    parse2(urls)
    # form = pd.DataFrame(list(zip(name, price, stock)),columns=['name','price','stock'])
    # print(form)
    # form.to_excel('ppe.xlsx',sheet_name='target_gloves')
    writer= ExcelWriter('ppe.xlsx')
    form = pd.DataFrame(list(zip(name, price,stock)), columns=['name', 'price','stock'])
    form.to_excel(excel_writer= writer, sheet_name='target_gloves',index=False)
    writer.save()

if __name__=='__main__':
    main()
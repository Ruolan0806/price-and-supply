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
    # print(title.keys())
    for i in title:
        item = i['item']['product_description']['title']
        # print(item)
        p = i['price']['formatted_current_price']
        name.append(item)
        price.append(p)
    print(len(name))
    print(len(price))
    print(name)
    return name,price


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
    # print(data)
    # if response.status_code == 200:
    #     with open('detergent.html', 'w') as file:
    #         file.write(text)
    title = data['data']['product_summaries']
    # print(title)
    for i in title:
        item = i['fulfillment']['store_options'][-1]['in_store_only']['availability_status']
        # print(item)
        stock.append(item)
    print(stock)
    print(len(stock))
    return stock





def main():
    url = 'https://redsky.target.com/redsky_aggregations/v1/web/plp_' \
          'client_v1?key=eb2551e4accc14f38cc42d32fbc2b2ea&tcins=12969915%2C12992354%2C1' \
          '3972122%2C13028043%2C13025049%2C11212538%2C75666311%2C13219649%2C14062784%2C5' \
          '2239347%2C13249005%2C14694500%2C13923950%2C15804793%2C52947829%2C52947634%2C545363' \
          '26%2C53398623%2C76078868%2C14710160%2C13028422%2C13025566%2C1' \
          '4710162%2C52947797&pricing_store_id=2146'
    parse(url)
    urls='https://redsky.target.com/redsky_aggregations/v1/web/plp_fulfill' \
         'ment_v1?key=eb2551e4accc14f38cc42d32fbc2b2ea&tcins=11212538%2C12969915%2C129923' \
         '54%2C13025049%2C13025566%2C13028043%2C13028422%2C13219649%2C13249005%2C13923950%2C1397212' \
         '2%2C14062784%2C14694500%2C14710160%2C14710162%2C15804793%2C52239347%2C52947634%2C52947797%2C52947' \
         '829%2C53398623%2C75666311%2C76078868&store_id=2146&zip=33063&state=FL&latitude=26.260&' \
         'longitude=-80.190&scheduled_delivery_store_id=2146&fulfillment_test_mode' \
         '=grocery_opu_team_member_test'
    parse2(urls)
    writer= pd.ExcelWriter('ppe.xlsx')
    form = pd.DataFrame(list(zip(name, price,stock)), columns=['name', 'price','stock'])
    # print(form.head())
    form.to_excel(excel_writer= writer, sheet_name='target_wipe',index=False)
    writer.save()


if __name__=='__main__':
    main()
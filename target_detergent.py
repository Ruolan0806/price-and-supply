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
    title=data['search_response']['items']['Item']
    # print(title.keys())
    # print(title)
    for i in title:
        item = i['title']
        # print(item)
        p = i['price']['formatted_current_price']
        # print(p)
        name.append(item)
        price.append(p)
    print(len(name))
    # print(name)


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
        print(item)
        stock.append(item)
    print(len(stock))





def main():
    url = 'https://redsky.target.com/v2/pl' \
      'p/search/?channel=web&count=24&default_purchasabi' \
      'lity_filter=true&facet_recovery=false&fulfillment_test_mode=g' \
      'rocery_opu_team_member_test&isDLP=false&keyword=Detergent&offset=0&pag' \
      'eId=%2Fs%2FDetergent&pricing_store_id=2146&scheduled_delivery_store_id=2146' \
      '&store_ids=2146%2C2092%2C638%2C2265%2C1337&visitorId=017271EC9A6C0201AAA96DE6' \
      'AC1A9BEF&include_sponsored_search_v2=true&ppatok=AOxT33a&platform=desktop&u' \
      'seragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit' \
      '%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F81.0.4044.129+Safari%2F53' \
      '7.36&excludes=available_to_promise_qualitative%2Cavailable_to_promis' \
      'e_location_qualitative&key=eb2551e4accc14f38cc42d32fbc2b2ea'
    parse(url)
    urls='https://redsky.target.com/redsky_aggregations/v1/' \
         'web/plp_fulfillment_v1?key=eb2551e4accc14f38cc42d32fbc2b2ea&tcins=12856578%2C13' \
         '055119%2C13055136%2C13908716%2C13954262%2C13954262%2C14711304%2C15071687%2C16271069%2C167597' \
         '36%2C16966890%2C17079386%2C17079386%2C17079650%2C17079680%2C17206874%2C17264558%2C21516452%2C21' \
         '516453%2C47776688%2C48637582%2C48638781%2C48638959%2C50715505%2C51848513%2C75663806%2C75663967&st' \
         'ore_id=2146&zip=33063&state=F' \
         'L&latitude=26.260&longitude=-80.190&scheduled_delivery_store_id=2146&fulfillment_test_mode' \
         '=grocery_opu_team_member_test'
    parse2(urls)
    writer= pd.ExcelWriter('ppe.xlsx')
    form = pd.DataFrame(list(zip(name, price,stock)), columns=['name', 'price','stock'])
    # print(form.head())
    form.to_excel(excel_writer= writer, sheet_name='target_detergent',index=False)
    writer.save()


if __name__=='__main__':
    main()
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
        # print(item.keys())
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
    print(len(stock))





def main():
    url = 'https://redsky.target.com/v2/plp/search/?channel=web&count=24&default_purc' \
          'hasability_filter=true&facet_recovery=false&fulfillment_test_mode=' \
          'grocery_opu_team_member_test&isDLP=false&keyword=Hand+Sanitizer&offset=0&pageId=%' \
          '2Fs%2FHand+Sanitizer&pricing_store_id=2146&scheduled_delivery_store_id=2146&store_ids=' \
          '2146%2C2092%2C638%2C2265%2C1337&visitorId=017271EC9A6C0201AAA96DE6AC1A9BEF&include_spon' \
          'sored_search_v2=true&ppatok=AOxT33a&platform=desktop&useragent=Mozilla%2F5.0+%28Windows' \
          '+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F81' \
          '.0.4044.129+Safari%2F537.36&excludes=available_to_promise_qualitative%2Cavailable_to_p' \
          'romise_location_qualitative&key=eb2551e4accc14f38cc42d32fbc2b2ea'
    parse(url)
    urls='https://redsky.target.com/redsky_aggregations/v1/web/plp_fulfillment_v1?key=eb2' \
         '551e4accc14f38cc42d32fbc2b2ea&tcins=11633443%2C12969915%2C13162354%2C14710162%2C15649424%2C16' \
         '792187%2C75456353%2C75566823%2C75662527%2C76500149%2C76513773%2C76565304%2C79692424%2C79701168%' \
         '2C79706514%2C79756617%2C79763849%2C79764641%2C79764642%2C79786607%2C79797653%2C79797654%2C79801' \
         '047%2C79801048&store_id=2146&' \
         'zip=33063&state=FL&latitude=26.260&longitude=-80.190&sche' \
         'duled_delivery_store_id=2146&fulfillment_test_mode=grocery_opu_team_member_test'
    parse2(urls)
    writer= pd.ExcelWriter('ppe.xlsx')
    form = pd.DataFrame(list(zip(name, price,stock)), columns=['name', 'price','stock'])
    print(form.head())
    form.to_excel(excel_writer= writer, sheet_name='target_sanitizer',index=False)
    writer.save()


if __name__=='__main__':
    main()
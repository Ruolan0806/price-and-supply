import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup
import openpyxl
from pandas import ExcelWriter
import re
name=[]
price=[]
stock = []
flat_price=[]

def parse(url):
    header = {
        'authority': 'www.cvs.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'cookie': 'adh_ps_pickup=on; bbcart=on; sab_newfse=on; sab_displayads=on; echome_lean6=on; getcust_elastic=on; mc_rio_locator3=on; mc_videovisit=on; pivotal_forgot_password=off-p0; pivotal_sso=off-p0; ps=on; refill_chkbox_remove=off-p0; rxhp=on; rxhp-two-step=off-p0; rxm=on; rxm_phone_dob=off-p0; sab_deals=on; s2c_akamaidigitizecoupon=off-p0; s2c_all_lean6=on; s2c_digitizecoupon=off-p0; s2c_herotimer=off-p0; s2c_prodshelf=on; setcust_elastic=on; show_exception_status=on; acctdel_v1=on; adh_new_ps=off; adh_ps_refill=on; buynow=off; dblistview=on; db-show-allrx=on; disable-app-dynamics=on; disable-sac=on; gbi_cvs_coupons=true; ice-phr-offer=off; v3redirecton=false; mc_hl7=on; mc_rio_locator2=on; mc_ui_ssr=off-p0; mdpguest=on; memberlite=on; pbmplaceorder=off; pbmrxhistory=on; rxd_bnr=on; rxdpromo=on; rxduan=on; rxlite=on; rxlitelob=off; sft_mfr_new=off; v2-dash-redirection=on; dfl=on; ak_bmsc=9D3CA7BD3FE6EB3272AD720AF1C7D0E3B854F4CD26470000A84DD65E4CD3D51C~plGUibCQBAw93zo/K/kFutuU0ZUtc/fSoXdk1ixOWWVOfQ/zAD//qmysRcOgyiBoS/7ylf5XrBfYv6dIS0gTfR4tl5RrVURnn0rAVBLdZszWys5egMe6UYVgqlwzk1dKntsWy6Bs0kDmZn8h80zCO1I1mwMVXSPkM8zjrWwZpUAqsWZPwf04qXIZd+huDrtgrNKAS1mMEDn5fndAjXXYCkub0DWNYTvPCEI/fpYah7pdQ=; mt.v=2.1119512562.1591102887270; gbi_visitorId=ckaxxku5f00013b81b8gk8ynu; AMCVS_06660D1556E030D17F000101%40AdobeOrg=1; mt.cem=BLTest-CEM-integration-1 - A; s_cc=true; BVImplall_route=3006_3_0; BVBRANDID=2f11e310-257c-4795-96c8-6d89ec9e1dc7; DG_IID=4F4FCEFA-6DED-363C-A9E1-60CB5F69773F; DG_UID=9D3DB03B-17BF-3792-8385-4FDCD8A9BBA0; DG_ZID=27C97E7D-8FB5-3B0F-B41E-1187C693A592; DG_ZUID=FBAC851F-0BE3-3B08-916D-EC5FB9D67FEC; DG_HID=673CE9FE-50A2-3988-A246-3218FC087ACE; DG_SID=71.196.121.205:C6hYkRwbIkDeBIxLilf9F7h4DZlg1UfDe2k0EvgAD4M; utag_main=v_id:0172751f5726001e8dc7996deef303073001406b00978$_sn:1$_ss:0$_pn:2%3Bexp-session$_st:1591104704173$ses_id:1591102887718%3Bexp-session$vapi_domain:cvs.com$_se:1; mp_cvs_mixpanel=%7B%22distinct_id%22%3A%20%22172751f886693-003e32ab1ec122-c373667-144000-172751f88673c6%22%2C%22bc_persist_updated%22%3A%201591102900331%7D; JSESSIONID=trZbGIVLgrmr7Jpj2FY0TWQKKhJ4InxfsKrvsY0M.commerce_1306; AMCV_06660D1556E030D17F000101%40AdobeOrg=1994364360%7CMCIDTS%7C18416%7CMCMID%7C34841266123233961831639432850468768726%7CMCAAMLH-1591707706%7C7%7CMCAAMB-1591707706%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1591110106s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.4.0; bm_sv=97904F81743DBD870E7382E1A099E01F~3YYYfVpbYyDYGD7ibiauwWABzmDCT35IvPxv0s3w0Sf5ym0oOHz5+7s93K/bmye8+o+x4oPN7QHxt3H58dPxupWazSfhkBZkSeifIEax8Zn26LzYpC55abxdXyozy3Pwb1slveZxDaMUGz/OnupTvg==; akavpau_www_cvs_com_general=1591106643~id=3cd21c0c2930d718aa4474f7be977406; RT="sl=0&ss=kaxxl17s&tt=0&bcn=%2F%2F17d09917.akstat.io%2F&z=1&dm=cvs.com&si=716f082e-3011-409f-bf9d-04d1b8fe1690&ul=24uiq"; _4c_=jVRhT%2BM4EP0rKNLtJ9LGjpPYSGgFBa04LZQFxN23yHEmjbVpEtluC7viv984aQnsotNWVRI%2Fvxm%2Fefb4Z7CroQ1OSCIIiVLGY5aS4%2BA7PNvg5Gegev%2Fc%2BsfGNMFJUDvX25P5fLfbzdTWzlS3nluQRtWfx9cDmPVpbzoHyukt%2FEWjWrYlvlZNtwUbHAeqKwEzETEjZBYh4H7gMKTMf2NkuVEud8%2B9J%2B2gOLLld5woYasV5DtdutpHJ3E6oTXoVe0Q5inzaG88ZUYTHOx0W3a7XwP36GtgRqlfXW87J32dXVXh%2BGzj0B2nlXRQIurV9%2B2jtrrQjXbPCFWysYD4VL13CUs%2BGgs%2Bnrw4egNjBDw5I5U08KAPye%2F%2BzVvY5VXT7RC4GZGuKd8iTz3GeMntpmlwfFt3rsu%2FdqsVlPlVO02sCk2jaVgWjbZuq8En6lpE6sGmtmu9%2FsdF%2FqiN28gmX6Cm%2FWIDWkKXb7FmN4HLttEtvEObUYH2Cm6WCFRSQaMrl9ve6NbRscS6W0MvVzCtPDp3WxtpYeT0Bqwyune6a%2B9VDeWmgYPo8%2FPcysKBdSO3KPZ2DLPF5rkdnBr3z5P7pp%2FYCKh3AObyllf2dQHzVPfT9%2Frw%2BeX%2B6mIMub1ZLi%2B%2BXo6DL3dXF4eJa6zH4Ul5lM0Gd%2FgkOP%2F6gAuFi8vrEA2AlZG%2BopAchUdnXqzpdhb8Hixqg7YccYJo5yP%2FGY6nPyUGKjBmYHm52nmh%2B87bA9isI4bj5fXDXX5%2BebZY3rzp1jU4o5X1HVuDbFw99G0xt3b%2BChnUrhvff3My%2F%2Fs%2BpLN0Fs0tEzTNoowmSSoE%2F3z27fyUfFrr8jRmnBGapoTGNI5FSnhM0liwmPIkYinP8E%2FTT2ffLk99WT1eIkE8nBMlh%2B2EwWHoG%2Fmca98AaylVFVWCsLRkQnIpCNA0YSLLIkKkmOgWrEUn92FEJGVCKRSsZFEiChWTCGRaEKlIFfGDK9eLYaP%2BTHfwgp22vxa5iEkWpRRvKod3A94xkf8hw3gBw%2F0YRCyhQlEScswZMqA8LARnYeaNSzKBAv2JHHNynnHORUY4JtnqQ46UK1oJnoaCZRAynmWhjKgKhcTlBY%2BjMiLBpCtiGUkFifa6CD%2FI6pt9RjKRSUZxwSw%2BkNlrEf12z47fl5wKxn4veTy0IbT%2FE5Z84JQ6FOnMBn4zggvPcXvOcKf%2BShEEKevJ8D84LR8kWJnqsMroIRW4t1H6Afnl5T8%3D',
    'referer': 'https://www.cvs.com/search?searchTerm=gloves',

    }

    response = requests.get(url, headers=header)

    text = response.content.decode('utf-8')
    # print(text)

    if response.status_code == 200:
        with open('cvs.text', 'w',encoding='utf-8') as file:
            file.write(text)
    html = etree.parse('cvs.text', etree.HTMLParser())
    price_ = html.xpath('//div[@class = "css-1dbjc4n"]//div//text()')
    title_ = html.xpath('//div[@class = "css-901oao css-cens5h r-1khnkhu r-1jn44m2 '
                        'r-ubezar r-29m4ib r-rjixqe r-kc8jnq r-fdjqy7 r-13qz1uu"]//text()')

    for i in title_:
        # if i.contains('Disinfecting'):
        if ('Soap') in i:
            name.append(i)
    print(name)
    print(len(name))
    stock = html.xpath('//div[@class = "css-901oao r-v857uc r-1jn44m2 r-1i10wst r-b88u0q"]//text()')
    # print(type(stock))
    # stock.insert(1,'Online')
    # stock.insert(5,'Online')
    print(stock)
    print(len(stock))
    for i in price_:
        p = re.findall('^\$\d+\.\d*$',i)
        if len(p)>0:
            price.append(p)
    flat_price = [item for sublist in price for item in sublist]
    # print(flat_price)
    print(flat_price)
    print(len(flat_price))
    return name,flat_price,stock


def main():

    # url for gloves
    # url='https://www.cvs.com/search?search' \
    # 'Term=gloves&refinements%5B0%5D%5Bnavigation' \
    # 'Name%5D=variants.subVariant.ProductBrand_Brand&refinements%5B0%5D%5Bvalue%5D=CVS%20Health'

    # url for detergent
    url2 ='https://www.cvs.com/search?searchTerm=detergent&refinements%5B0%5D' \
          '%5BnavigationName%5D=variants.subVariant.ProductBrand_Brand&refinements%5B0%5D%5Bvalue%5D=Tide'

    # url for hand sanitizer
    url3= 'https://www.cvs.com/search?searchTerm=ha' \
          'nd%20sanitizer&refinements%5B0%5D%5BnavigationName%5D=' \
          'variants.subVariant.ProductBrand_Brand&refinements%5B0%5D%5Bvalue%5D=CVS%20Health'

    # url for disinfecting wipes
    url4='https://www.cvs.com/search?searchTerm=Disinf' \
         'ecting%20Towelettes&refinements%5B0%5D%' \
         '5BnavigationName%5D=categories.1&refinements%5B0%5D%5Bvalue%5D=Household%20%26%20Grocery'
    #url for tissue rolls
    url5='https://www.cvs.com/search?searchTerm=tissue%20roll'

    # url for spray
    url6='https://www.cvs.com/search?searchTerm=Disinfecting%20Spray%20with%20Bleach'

    #url for soap
    url7='https://www.cvs.com/search?searchTerm=soap&refinements' \
         '%5B0%5D%5BnavigationName%5D=categories.1&refinements%5B0%5D%5Bvalue%5D=Household' \
         '%20%26%20Grocery&refinements%5B1%5D%5BnavigationName%5D=ca' \
         'tegories.2&refinements%5B1%5D%5Bvalue%5D=Cleaning%20Supplies'

    name,flat_price,stock = parse(url7)

    form = pd.DataFrame(list(zip(name, flat_price,stock)), columns=['name', 'price','stock'])
    print(form.head())
    form.to_excel('cvs.xlsx', sheet_name='cvs',index=False)



if __name__ == '__main__':
    main()
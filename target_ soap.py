import target_wipes as t
import pandas as pd
from pandas import ExcelWriter
urls='https://redsky.target.com/redsky_aggregations/v1/web' \
     '/plp_fulfillment_v1?key=eb2551e4accc14f38cc42d32fbc2b2ea&tci' \
     'ns=10770140%2C11007066%2C11007067%2C11695273%2C12067287%2C12067288' \
     '%2C12067289%2C13359350%2C13376678%2C13689989%2C13951811%2C13969442%2C142' \
     '80513%2C15044590%2C16678879%2C16679238%2C17014118%2C26393163%2C51324842%2C5271' \
     '4294%2C75566322%2C75566323%2C75567412%2C76559124%2C76559127%2C77592715%2C79392715%2C' \
     '79392716&store_id=2146&zip=33063&state=FL&latitude=26.260&longitude=-80.1' \
     '90&scheduled_delivery_store_id=2146&fulfillment_test_mode=grocery_opu_team_member_test'
stock =list(t.parse2(urls))

url= 'https://redsky.target.com/redsky_aggregations/' \
     'v1/web/plp_client_v1?key=eb2551e4accc14f38cc42d32fbc2b2ea&tci' \
     'ns=15044590%2C16679238%2C75566322%2C11695273%2C13951811%2C75566323%2C14' \
     '280513%2C11007066%2C12067287%2C13969442%2C13359350%2C12067288%2C12067289%2C17' \
     '014118%2C79392715%2C26393163%2C79392716%2C7' \
     '5567412%2C16678879%2C52714294%2C10770140%2C13376678%2C11007067%2C13689989%2C5132' \
     '4842%2C77592715%2C76559124%2C76559127&pricing_store_id=2146'
name, price =(t.parse(url))
writer= pd.ExcelWriter('ppe.xlsx')
form = pd.DataFrame(list(zip(name, price,stock)), columns=['name', 'price','stock'])
# print(form.head())
form.to_excel(excel_writer= writer, sheet_name='target_soap',index=False)
writer.save()
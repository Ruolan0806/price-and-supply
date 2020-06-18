import target_wipes as t
import pandas as pd
from pandas import ExcelWriter
urls='https://redsky.target.com/redsky_aggregations/' \
     'v1/web/plp_fulfillment_v1?key=eb2551e4accc14f38cc4' \
     'd32fbc2b2ea&tcins=12969915%2C12992354%2C13025566%2C13028422%2C132' \
     '19649%2C13315426%2C13315436%2C13762640%2C13923950%2C13960390%2C14228749%2C142' \
     '29959%2C14710160%2C14710162%2C14710716%2C15804793%2C16448168%2C51039862%2C52' \
     '305473%2C52947634%2C52947797%2C52947829%2C53161909%2C53398623&store_id=2146&zip=33063&state' \
     '=FL&latitude=26.260&longitude=-80.190&scheduled_delivery_store_id=2146&fulfil' \
     'lment_test_mode=grocery_opu_team_member_test'
stock =list(t.parse2(urls))

url= 'https://redsky.target.com/redsky_aggregations/v1/w' \
     'eb/plp_client_v1?key=eb2551e4accc14f38cc42d32fbc2b2ea&tci' \
     'ns=14710160%2C52947797%2C13028422%2C52947634%2C14229959%2C5316190' \
     '9%2C16448168%2C14710716%2C53398623%2C13219649%2C12969915%2C14710162%2C13923950%2C129' \
     '92354%2C15804793%2C52947829%2C13025566%2C52305473%2C13315426%2C14228749' \
     '%2C13315436%2C13762640%2C13960390%2C51039862&pricing_store_id=2146'
name, price =(t.parse(url))
writer= pd.ExcelWriter('ppe.xlsx')
form = pd.DataFrame(list(zip(name, price,stock)), columns=['name', 'price','stock'])
# print(form.head())
form.to_excel(excel_writer= writer, sheet_name='target_bleach',index=False)
writer.save()
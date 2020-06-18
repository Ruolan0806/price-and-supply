import target_wipes as t
import pandas as pd
from pandas import ExcelWriter
urls='https://redsky.target.com/redsky_aggregations/v1/web/plp_fulf' \
     'illment_v1?key=eb2551e4accc14f38cc42d32fbc2b2ea&tcins=15819046%2C50' \
     '658427%2C50658473%2C52238984%2C53128506%2C53128898%2C53128942%2C53128956' \
     '%2C53129157%2C53276358%2C75558489%2C75663300%2C75665830%2C75665832%2C75665846' \
     '%2C75665975%2C76596557%2C77568840%2C79762475%2C79768115%2C79769192%2C79803863%2' \
     'C80183988%2C80183989&store_id=2146&zip=33063&state=FL' \
     '&latitude=26.260&longitude=-80.190&scheduled_delivery_store_id=2146&fulfill' \
     'ment_test_mode=grocery_opu_team_member_test'
stock =list(t.parse2(urls))

url= 'https://redsky.target.com/redsky_aggregations/v1/web/plp_client_' \
     'v1?key=eb2551e4accc14f38cc42d32fbc2b2ea&tcins=75663300%2C7566583' \
     '0%2C75665975%2C76596557%2C79768115%2C75665846%2C79762475%2C52238984%2C' \
     '15819046%2C75558489%2C79769192%2C75665832%2C53276358%2C5065' \
     '8473%2C50658427%2C80183988%2C80183989%2C79803863%2C77568840%2C53129157' \
     '%2C53128956%2C53128942%2C53128506%2C53128898&pricing_store_id=2146'
name, price =(t.parse(url))
writer= pd.ExcelWriter('ppe.xlsx')
form = pd.DataFrame(list(zip(name, price,stock)), columns=['name', 'price','stock'])
# print(form.head())
form.to_excel(excel_writer= writer, sheet_name='target_wipe',index=False)
writer.save()
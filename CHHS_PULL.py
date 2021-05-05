import pandas as pd, numpy as np, requests, json

resource_id = "130d7ba2-b6eb-438d-a412-741bde207e1c"
runs = int(json.loads(requests.get("https://data.chhs.ca.gov/api/3/action/datastore_search_sql?sql=SELECT%20max(_id)%20from%20\""+resource_id+"\"").content)['result']['records'][0]['max']/500)
CHHS_VAX_DATA = pd.DataFrame()
for iter_pull in range(runs+1):
	CHHS_VAX_DATA = CHHS_VAX_DATA.append([ pd.DataFrame(json.loads(requests.get("https://data.chhs.ca.gov/datastore/odata3.0/{resource_id}?$skip={iter_num}".format(resource_id = resource_id, iter_num=iter_pull*500)+"&$format=json").content)['value']) ])

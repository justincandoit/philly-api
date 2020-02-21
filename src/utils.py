from carto.sql import SQLClient
from carto.auth import APIKeyAuthClient


USR_BASE_URL = "https://phl.carto.com/"
auth_client = APIKeyAuthClient(USR_BASE_URL,api_key=None)
sql = SQLClient(auth_client)




data = sql.send('select * from real_estate_tax_delinquencies where zip_code=19125 and num_years_owed > 3 order by total_due', format='csv')

print(data)

# print(data['total_rows'])
#
# for row in data['rows']:
#     print(row['num_years_owed'])
#     print(row['street_address'])
#     print(row['total_due'])

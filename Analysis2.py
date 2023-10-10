import requests
import matplotlib.pyplot as plt

api_key = open("api_key.txt", "r").read()

company = "AAPL"
years = 4

balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?period=quarterly&limit={years}&apikey={api_key}')
balance_sheet_json = balance_sheet.json()

assts_q1 = balance_sheet[4]['totalAssets']
assts_q2 = balance_sheet[3]['totalAssets']
assts_q3 = balance_sheet[2]['totalAssets']
assts_q4 = balance_sheet[1]['totalAssets']

assets_data = [assts_q1, assts_q2, assts_q3, assts_q4]
assets_data = [x/100000000 for x in assets_data]

plt.bar([1,2,3,4], assets_data)
plt.title(f"Quarterly Assets of {company}")
plt.xlabel("Quarter")
plt.ylabel("Total Assets (in billions)")
plt.xticks([1,2,3,4], ["Q1", "Q2", "Q3", "Q4"])
plt.show()

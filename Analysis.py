import requests
import matplotlib.pyplot as plt

api_key = open("api_key.txt", "r").read()

company = "AAPL"
years = 2

balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={api_key}')
balance_sheet_json = balance_sheet.json()

totral_current_assets = balance_sheet_json[0]['totalCurrentAssets']
print(f"Total Current Assets O  f {company}: {totral_current_assets:,}")

totral_current_liabilities = balance_sheet_json[0]['totalCurrentLiabilities'] 
print(f"Total Current Liabilities Of {company}: {totral_current_liabilities:,}")

total_debt = balance_sheet_json[0]['totalDebt']
cash_end_equivalents = balance_sheet_json[0]['cashAndCashEquivalents']
cash_debt_difference = cash_end_equivalents - total_debt
print(f"Cash Debt Difference Of {company}: {cash_debt_difference:,}")

goodwill_and_intangibles = balance_sheet_json[0]['goodwillAndIntangibleAssets']
total_assets = balance_sheet_json[0]['totalAssets']
pct_intangibles = goodwill_and_intangibles / total_assets * 100 

print(f"Percentage of Intangibles Of {company}: {pct_intangibles:,.2f}%")

import requests

base_url = "https://api.fixer.io/latest?base="

baseCurrency = input("Please enter a base currency code to retrieve rates: ")

try:
    response = requests.get(base_url+baseCurrency)
    print(response.json())
    response.raise_for_status()

except requests.exceptions.HTTPError as e:
    print(e)

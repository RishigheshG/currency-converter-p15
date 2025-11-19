from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com"
API_KEY = "fca_live_RpMTgS58rV9jAgyS5OFdJimXd863RLUhEnVCBS2Q"

printer = PrettyPrinter()


def get_currencies():
  endpoint = f"/v1/currencies?apikey={API_KEY}"
  url = BASE_URL + endpoint
  data = get(url).json().get("data")
  data = list(data.items())
  data.sort()
  return data


def print_currencies(currencies):
  for name, currency in currencies:
    name = currency["name"]
    symbol = currency.get("symbol", "")
    symbol_native = currency.get("symbol_native", "")
    print(f"{name} : {symbol} : {symbol_native}")


def exchange_rate(curr1, curr2):
  endpoint = f"/v1/latest?apikey={API_KEY}&base_currency={curr1}&currencies={curr2}"
  url = BASE_URL + endpoint
  data = get(url).json().get("data")
  rate = data.get(curr2)
  return rate


def convert(curr1, curr2, amount):
  rate = exchange_rate(curr1, curr2)
  converted_amount = rate * amount
  return converted_amount


def main():
  print("Welcome to Currency Converter!")
  curr1 = input("Enter first currency code: ").upper()
  curr2 = input("Enter second currency code: ").upper()
  want_convert = input(
    "Do you want to convert an amount? (yes/no): ").lower()
  if want_convert == "yes":
    amount = float(input(f"Enter amount in {curr1}: "))
    converted_amount = convert(curr1, curr2, amount)
    print(f"{amount} {curr1} is equal to {converted_amount} {curr2}")
  else:
    rate = exchange_rate(curr1, curr2)
    print(f"Exchange Rate {curr1} to {curr2}: {rate}")

main()

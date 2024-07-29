import requests
import json

# API key for the exchange rate API
api_key = 'Api_key here (infor is in the README.md file)'

# Base URL for the exchange rate API
base_url = "https://v6.exchangerate-api.com/v6/"

# List of available currency codes
currency_codes = 'AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYR, BZD, CAD, CDF, CHF, CLF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, STD, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VEF, VND, VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPF, YER, ZAR, ZMK, ZMW, ZWL.'

# Get user input for the base currency and target currency
base_currency = input(f"What currency do you want to compare [1] (enter short form)? Here's the menu: {currency_codes}\n: ")
target_currency = input("What currency do you want to compare [2] to: ")

# Construct the endpoint URL
endpoint = f'{base_url}{api_key}/pair/{base_currency}/{target_currency}'

# Make the request to the API
response = requests.get(endpoint)

# Initialize conversion rate
conversion_rate = ""

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract the conversion rate
    conversion_rate = data['conversion_rate']
else:
    print("Failed to retrieve data:", response.status_code, response.text)

# Convert the conversion rate to a float
conversion_rate = float(conversion_rate)

# Get user input for the quantity to convert
quantity = int(input(f"How many {base_currency} do you need to convert: "))

# Calculate the converted amount
converted_amount = quantity * conversion_rate

# Print the result
print(f"{quantity} {base_currency} is equal to {converted_amount} {target_currency}")

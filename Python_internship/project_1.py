def currency_converter(amount,from_currency,to_currency):
    rates={
         "USD": 1.0,
        "INR": 89.71,
        "EUR": 0.85,
        "GBP": 0.74,
        "JPY": 157.0
    }
    if from_currency not in rates or to_currency not in rates:
        return "Invalid currency code"
    converted_currency=amount*  (rates[to_currency] / rates[from_currency])
    return round(converted_currency, 2)
amount=float(int(input("Enter amount: ")))
from_currency=input("From currency (USD/INR/EUR/GBP/JPY): ").upper()
to_currency=input("To currency (USD/INR/EUR/GBP/JPY): ").upper()
result=currency_converter(amount,from_currency,to_currency)
print("converted amount: ",result)
# Part I

import osa
import os


file = os.path.join(*[os.path.dirname(os.path.abspath(__file__)), "currencies", "currencies.txt"])

def extract_money_and_currency(file):
    all_trips = []
    with open(file) as f:
        trips = f.readlines()
        for trip in trips:
            all_trips.append(trip.strip())
    return all_trips


def convertation(trips):
    total_sum = []
    for trip in trips:
        money = trip.split()[1]
        currency = trip.split()[2]
        if currency != 'RUB':
            url = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
            client = osa.client.Client(url)
            response = client.service.ConvertToNum(fromCurrency=currency,
                                                   toCurrency='RUB',
                                                   amount=float(money),
                                                   rounding=False)
            total_sum.append(response)
        else:
            total_sum.append(float(money))
    return int(sum(total_sum))

print(convertation(extract_money_and_currency(file)))
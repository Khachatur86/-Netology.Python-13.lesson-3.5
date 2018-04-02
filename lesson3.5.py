# Part I

import osa
import os

file = os.path.join(*[os.path.dirname(os.path.abspath(__file__)), "currencies", "currencies.txt"])

def extract(file):
    list_of_trips = []
    with open(file) as f:
        trips = f.readlines()
        for trip in trips:
            list_of_trips.append(trip.strip())
    return list_of_trips


def convertation(list_of_trips):
    total_sum = []
    for trip in list_of_trips:
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

print(convertation(extract(file)))

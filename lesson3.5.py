# Part I

import osa
import os


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

# Part 2


def extract_temperatures(file):
    list_of_temps = []
    with open(file) as f:
        temps = f.readlines()
        for temp in temps:
            list_of_temps.append(int(temp.split()[0]))
    return list_of_temps


def temp_convertation(list_of_temps):
    list_of_converted_temps = []

    for temp in list_of_temps:
        url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL' 
        client = osa.client.Client(url)
        response = client.service.ConvertTemp(Temperature=float(temp),
                                              FromUnit='degreeFahrenheit',
                                              ToUnit='degreeCelsius')
        list_of_converted_temps.append(response)
    return list_of_converted_temps


def calculation_of_average(list_of_converted_temps):
    average = sum(list_of_converted_temps) / len(list_of_converted_temps)
    return average
# Part 3


if __name__ == "__main__":
    files = [os.path.join(*[os.path.dirname(os.path.abspath(__file__)), "currencies", "currencies.txt"]),
             os.path.join(*[os.path.dirname(os.path.abspath(__file__)), "currencies", "temps.txt"]),
             os.path.join(*[os.path.dirname(os.path.abspath(__file__)), "currencies", "travel.txt"])]

    print(f"{convertation(extract(files[0]))} рублей")
    print(f"{round(calculation_of_average(temp_convertation(extract_temperatures(files[1])))), 1}")
    # print(round(calculation_of_average, 2)))

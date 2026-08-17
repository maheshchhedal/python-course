cities_in_f= {
    'New York':32,
    'Boston':75,
    'Lost Angeles':100,
    'Chicago':50
    }

cities_in_c={ key:round((value-32)*(5/9)) for(key,value) in cities_in_f.items()}
print(cities_in_c)


weather={
    'Kathmandu':"Snowing",
    'Dhangadhi':'sunny',
    'Pokhara':"sunny",
    'Butwal':'coudy'
}

sunny_weather={key:value for (key,value) in weather.items() if value=='sunny'}
print(sunny_weather)

def check_weather(values):
    if values>=70:
        return 'Hot'
    elif values >= 69:
        return 'warm'
    else:
        return 'cloudy'

cities= {
    'New York':32,
    'Boston':75,
    'Lost Angeles':100,
    'Chicago':50
    }

check_temp={key:check_weather(value) for (key,value) in cities.items()} 
print(check_temp)
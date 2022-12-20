import json
import requests

listOfCities = ['Лондон', 'Шереметьево', 'Череповец']
listResponse = []

for city in listOfCities:
    listResponse.append( requests.get('https://ru.wttr.in/' + city + '?M&n&q&T') )

for response in listResponse:
    print(response.text)
    print('//////////////////////////////////////////////////////////////////////')

import requests


def main():
    cities = ['Лондон', 'Шереметьево', 'Череповец']
    settings = {'M':'',
                'n':'',
                'q':'',
                'T':'',
                'lang':'ru'}

    for city in cities:

        request = requests.get('https://wttr.in/{}'.format(city), params=settings)

        try:
            request.raise_for_status()
            print(request.text)

        except requests.exceptions.HTTPError as error:
            print(error)


if __name__ == '__main__':
    main()

from django.shortcuts import render
import requests
from weather.models import City
from weather.forms import CityForm


def index(request):
    url = "https://api.exchangeratesapi.io/latest?base=TRY"
    response = requests.get(url)
    data = response.json()
    context = data
    dollar = 1/(context['rates']['USD'])
    euro = 1/(context['rates']['EUR'])
    canada_dollar = 1/(context['rates']['CAD'])
    hongkonk_dollar = 1/(context['rates']['HKD'])
    japanese_yen = 1/(context['rates']['JPY'])
    russian_ruble = 1/(context['rates']['RUB'])
    denmark_kron = 1/(context['rates']['DKK'])
    israil_shekel = 1/(context['rates']['ILS'])
    dollar = str(dollar)
    euro = str(euro)
    canada_dollar = str(canada_dollar)
    hongkonk_dollar = str(hongkonk_dollar)
    japanese_yen = str(japanese_yen)
    russian_ruble = str(russian_ruble)
    denmark_kron = str(denmark_kron)
    israil_shekel = str(israil_shekel)
    dollar = dollar[:5]
    euro = euro[:5]
    canada_dollar = canada_dollar[:5]
    hongkonk_dollar = hongkonk_dollar[:5]
    japanese_yen = japanese_yen[:5]
    russian_ruble = russian_ruble[:5]
    denmark_kron = denmark_kron[:5]
    israil_shekel = israil_shekel[:5]
    url2 = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOURAPİKEY'
    cities = City.objects.all()  # return all the cities in the database
    if request.method == 'POST':  # only true if form is submitted
        # add actual request data to form for processing
        form = CityForm(request.POST)
        form.save()  # will validate and save if validate
    # request the API data and convert the JSON to Python data types
    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url2.format(city.name)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'wind': city_weather['wind']['speed'],
            'icon': city_weather['weather'][0]['icon']
        }  # returns the index.html template
        # add the data for the current city into our list
        weather_data.append(weather)
    url3 = "https://apiv2.apifootball.com/?action=get_players&player_name=ronaldo cristiano&APIkey=<YOUR_APİ_KEY>"
    response3 = requests.get(url3)
    data3 = response3.json()
    context3 = data3[0]
    playername = context3['player_name']
    playerkey = context3['player_key']
    playernumber = context3['player_number']
    playercountry = context3['player_country']
    playerage = context3['player_age']
    return render(request, 'index.html', {
        'dollar': dollar,
        'euro': euro,
        'canada_dollar': canada_dollar,
        'hongkonk_dollar': hongkonk_dollar,
        'japanese_yen': japanese_yen,
        'denmark_kron': denmark_kron,
        'russian_ruble': russian_ruble,
        'israil_shekel': israil_shekel,
        'weather_data' : weather_data,
        'form':form,
        'playername':playername,
        'playerkey':playerkey,
        'playernumber':playernumber,
        'playercountry':playercountry,
        'playerage':playerage        
    })

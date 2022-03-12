#Module file for extracting data from APIs
import requests
import datetime
#from newsapi import NewsApiClient

#Weather API

def get_weather():
    try:

        keys = 'ENTER API KEY'
        r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat=33.4936&lon=-117.1484&appid={keys}')
        data = r.json()

        daily_forcast = {
            'city' : data['city']['name'],
            'country' : data['city']['country'],
            'periods' : list()
        }    

        for period in data['list'][0:9]:
            daily_forcast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                              'temp' : round(period['main']['temp']),
                                              'description' : period['weather'][0]['description'].title(),
                                              'icon' : f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
        
        return daily_forcast
        
    except Exception as e:
        print(e)
    
def get_scores():
    try:
        date = datetime.date.today() - datetime.timedelta(days=1)
        querystring = {"date": f"{date}"}
        headers = {
           'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
           'x-rapidapi-key': "ENTER API KEY"}
        
        r = requests.get("https://api-nba-v1.p.rapidapi.com/games",headers=headers, params=querystring)

        data = r.json()
        scores = list()
        
        for i in range(len(data['response'])):
            scores.append({
            'Home Team' : data["response"][i]['teams']['home']['name'],
            'Home Score' : data['response'][i]['scores']['home']['points'],
            'Away Team' : data["response"][i]['teams']['visitors']['name'],
            'Away Score' : data['response'][i]['scores']['visitors']['points'],
        })

        return scores

    except Exception as e:
        print(e) 
   

def get_headlines():
    try:
        r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=ENTER API KEY')
        data = r.json()
        headlines = list()

        for i in range(len(data['articles'][0:9])):
            headlines.append({
                "Source" : data['articles'][i]['source']['name'],
                "Headline" : data['articles'][i]['title'],
                'Description' : data['articles'][i]['description'],
                'Link' : data['articles'][i]['url']
            })

        return headlines
    
    except Exception as e:
        print(e)

def get_word_of_day():
    try:
        querystring = {"random":"true"}

        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': "ENTER API KEY"
            }
        
        r = requests.get('https://wordsapiv1.p.rapidapi.com/words/', headers=headers,params=querystring)
        data = r.json()
        word = data['word']
        r2 = requests.get(f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions", headers=headers)

        definition = r2.json()
        return definition

    except Exception as e:
        print(e)

        
    
from flask import Flask,request,jsonify
import requests
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    if(len(data['queryResult']['parameters'])==2):
      source_currency = data['queryResult']['parameters']['unit-currency']['currency']
      amount = data['queryResult']['parameters']['unit-currency']['amount']
      target_currency = data['queryResult']['parameters']['currency-name']

      print(target_currency,source_currency,amount)

      url = "https://api.apilayer.com/fixer/convert?to={}&from={}&amount={}".format(target_currency,source_currency,amount)

      payload = {}
      headers= {
        "apikey": "pa0lhhXDtk3eujeEqZt7rrlY2RUSxLvW"
      }

      response = requests.request("GET", url, headers=headers, data = payload)

      status_code = response.status_code
      result = response.text
      print(result)

      res = json.loads(result)
      final_amount = res['result']
      final_amount = round(final_amount,2)
      output = {
          'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
      }
      return jsonify(output)
    else:
        city = data['queryResult']['parameters']['geo-city']
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=386617448263377540e5e4979cdd4474".format(city)

        response = requests.get(url)
        response = response.json()
        temperature = response['main']['temp']
        humidity = response['main']['humidity']
        windspeed = response['wind']['speed']
        climate = response['weather'][0]['description']

        output = {
          'fulfillmentText':"Today's temperatue is {} °C & feels like {} where as humidity is {}% and wind speed is {}km/hr".format(temperature,climate,humidity,windspeed)
        }
        return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

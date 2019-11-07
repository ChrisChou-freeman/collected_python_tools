import json
import sys
import importlib
if sys.version_info[0]==2:
    urllib = importlib.import_module("urllib")
else:
    urllib = importlib.import_module("urllib.request")


city_code = {
    "beijing": 101010100,
    "shenzhen":101280601,
    "ganzhou": 101240701,
    "guangzhou": 101280101,
}

def request_weather(city_name):
    if city_code.get(city_name.lower()):
        the_china_weather_url = "http://www.weather.com.cn/data/cityinfo/{}.html"
        code = city_code[city_name.lower()]
        url = the_china_weather_url.format(code)
        respond = urllib.urlopen(url)
        data = respond.read()
        data = json.loads(data)
        data = data["weatherinfo"]
        print """
        city: {}
        the low will be {}, the high will be {}
        currently {}
        """.format(
            data['city'].encode("utf-8"),
            data['temp1'].encode("utf-8"),
            data['temp2'].encode("utf-8"),
            data['weather'].encode("utf-8")
        )
    else:
        print("the city name, note find...")

request_weather("shenzhen")
import json
import sys
import importlib

if sys.version_info[0]==2:
    urllib = importlib.import_module("urllib")
    input = raw_input
else:
    urllib = importlib.import_module("urllib.request")


city_codes = {
    "beijing": 101010100,
    "shenzhen":101280601,
    "ganzhou": 101240701,
    "guangzhou": 101280101,
}

city_list = [
    "beijing",
    "shenzhen",
    "ganzhou",
    "guangzhou"
]

def request_weather(city_name):
    if city_codes.get(city_name.lower()):
        the_china_weather_url = "http://www.weather.com.cn/data/cityinfo/{}.html"
        code = city_codes[city_name.lower()]
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

def main():
    while True:
        print("choice your city")
        print("--------------")
        for index, item in enumerate(city_list):
            print("number:{}--{}".format(index, item))
        print("")
        print("--------------")
        number = input("input the city number>>")
        if number:
            city_name = city_list[int(number)]
            request_weather(city_name)
            input("press anykey continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
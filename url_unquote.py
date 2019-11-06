import sys
import importlib

if sys.version_info[0]==2:
    urllib = importlib.import_module("urllib")
else:
    urllib = importlib.import_module("urllib.parse")


def my_url_unquote(url):
    return urllib.unquote(url)


if __name__ == "__main__":
    try:
        quote_url = input(">>input url in here:")
        print(my_url_unquote(quote_url))
    except Exception as e:
        print("something wrong, check your url string")

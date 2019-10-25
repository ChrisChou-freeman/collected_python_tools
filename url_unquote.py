import urllib
import sys



def my_url_unquote(url):
    return urllib.unquote(url)


if __name__ == "__main__":
    try:
        quote_url = raw_input(">>input url in here:")
        print my_url_unquote(quote_url)
    except Exception as e:
        print("something wrong, check your url string")

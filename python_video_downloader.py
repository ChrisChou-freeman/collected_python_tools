import os
import sys

import requests
from bs4 import BeautifulSoup

'''
URL of the archive web-page which provides link to
all video lectures. It would have been tiring to
download each video manually.
In this example, we first crawl the webpage to extract
all the links and then download videos.
'''


def get_video_links(the_url):
    # create response object
    r = requests.get(the_url)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'xml')

    # find all links on web-page
    links = soup.findAll('video')

    # filter the link sending with .mp4
    video_links = [the_url + link['src'] for link in links if link['src'].split('?')[0].endswith('mp4')]
    print(video_links)
    return video_links


def download_video_series(video_links):
    for link in video_links:

        '''iterate through all links in video_links
        and download them one by one'''

        # obtain filename by splitting url and getting 
        # last string
        file_name = link.split('?')[0].split('/')[-1]
        video_folder = "./videos"
        if not os.path.exists(video_folder):
            os.mkdir(video_folder)
        print("Downloading the file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True)

        # download started
        with open(os.path.join(video_folder, file_name), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All videos are downloaded!")
    return


def main():
    the_url = ""
    while True:
        the_url = input("input include videos url in here:")
        if the_url.startswith("http"):
            break
        else:
            print("url incorrect")
    if not the_url:
        raise "no url input here, try again"
    # getting all video links
    video_links = get_video_links(the_url)
    # download all videos
    download_video_series(video_links)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nbye~")
        input()

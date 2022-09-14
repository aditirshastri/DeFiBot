'''

import bs4
import requests, re
import urllib

from bs4 import BeautifulSoup
import urllib.request,sys,time
import pandas as pd

def parse_page(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        text = soup.text
        text_list = text.strip().split("\n")
        text_list2 = []

        for i in text_list:
            if i != "":
                text_list2 += i.split(".")

        for i in text_list2:
            print(i)

    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)


def gitbook():
    url = 'https://opyn.gitbook.io/squeeth/squeeth/contracts-documentation'
    links = [url]
    while links:
        page = requests.get(links[0])
        soup = BeautifulSoup(page.text, "html.parser")
        parse_page(links[0])
        print("\n\n\n NEXT PAGE: \n\n\n")
        temp_links = []
        for link in soup.find_all('a', attrs={'href': re.compile("")}):
            temp_links += [link.get('href')]

        next_page = "https://opyn.gitbook.io" + temp_links[-1]
        print(next_page)
        if (next_page == links[0]):
            links = False
        else:
            links = [next_page]


if __name__ == '__main__':
    gitbook()'''

'''
import bs4
import requests, re
import urllib

from bs4 import BeautifulSoup
import urllib.request,sys,time
import pandas as pd

url = "https://opyn.gitbook.io/squeeth/squeeth/contracts-documentation"

page = requests.get(url)
#print(page.text)
soup = BeautifulSoup(page.text, "html.parser")
temp_links = []

for link in soup.find_all('a', attrs={'href': re.compile("/squeeth")}):
    temp_links += [link.get('href')]

for i in temp_links:
    print(i)
'''


import bs4
import requests, re
import urllib
from bs4 import BeautifulSoup
import urllib.request,sys,time
import pandas as pd

def parse_page(url):
    url = "https://opyn.gitbook.io" + url
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        text = soup.text
        text_list = text.strip().split("\n")
        text_list2 = []

        for i in text_list:
            if i != "":
                text_list2 += i.split(".")

        for i in text_list2:
            print(i)

    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)

def get_links(url):
    links = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    for link in soup.find_all('a', attrs={'href': re.compile("/squeeth")}):
        links += [link.get('href')]
    links = links[2:]

    links_total = []
    for link in links:
        links_total.append(link)

    for i in links:
        temp_url = "https://opyn.gitbook.io" + i
        try:
            temp_page = requests.get(temp_url)
            soup2 = BeautifulSoup(temp_page.text, "html.parser")

            temp_links = []
            for link in soup2.find_all('a', attrs={'href': re.compile(i)}):
                #print("second loop")
                temp_links += [link.get('href')]

            for link in temp_links:
                #print("third loop")
                if link is not links:
                    links_total.append(link)

        except Exception as e:
            print()

    return links_total


def clean_links(links):
    temp = []
    for link in links:
        if link not in temp:
            temp.append(link)
    return temp


def parse_from_links(links):
    for link in links:
        parse_page(link)
        print("\n\n\n NEXT PAGE \n\n\n")


def main():
    url = 'https://opyn.gitbook.io/squeeth/squeeth/contracts-documentation'
    links = get_links(url)
    links = clean_links(links)
    parse_from_links(links)

main()
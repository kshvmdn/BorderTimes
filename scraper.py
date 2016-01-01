import requests, json
import pprint
from bs4 import BeautifulSoup as BS

URL = 'http://travel.gc.ca/travelling/border-times-us'


def scrape():
    return parse(request())


def request():
    return requests.get(URL)


def parse(response):
    soup = BS(response.text, 'html.parser')
    borders = {}
    if soup.find('table'):
        for tr in soup.find('table').find_all('tr', class_='font-small'):
            border = tr.find_all('td')
            port_name = border[0].find('strong').string
            port_info = [br.next_sibling for br in border[0].find_all('br')]
            port_cities, update_time = port_info[0].split('/'), port_info[1].strip('Last updated : ')
            borders[port_name] = {
                'port_info': {
                    'port_name': port_name,
                    'from': port_cities[0],
                    'to': port_cities[1]
                },
                'last_updated': update_time
            }
            # for time in border[1:]:
            #     print(time)
            # print('---')

    # pprint.pprint(borders)


if __name__ == '__main__':
    scrape()
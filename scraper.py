import requests

from bs4 import BeautifulSoup
from collections import OrderedDict

URL = 'http://travel.gc.ca/travelling/border-times-us'


def scrape(port=None):
    return parse(port)


def request(url):
    return requests.get(url)


def parse(response, requested_port=None):
    response = request(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    wait_times = OrderedDict()
    if not soup.find('table'):
        return None

    for tr in soup.find('table').find_all('tr', class_='font-small'):
        port = tr.find_all('td')

        port_name = port[0].find('strong').string
        port_info = [br.next_sibling for br in port[0].find_all('br')]
        port_cities = port_info[0].split('/')

        update_time = port_info[1].strip('Last updated : ')
        commercial_wait, noncommercial_wait = [w.string for w in port[1:]]

        wait_times[port_name] = OrderedDict([
            ('port_info', OrderedDict([
                ('name', port_name),
                ('from', port_cities[0]),
                ('to', port_cities[1])
            ])),
            ('wait_times', OrderedDict([
                ('commercial', commercial_wait),
                ('non_commercial', noncommercial_wait)
            ])),
            ('last_updated', update_time)
        ])

    return wait_times[requested_port] if requested_port else wait_times

if __name__ == '__main__':
    import json
    times = scrape('Rainbow Bridge')
    print(json.dumps(times, indent=2))

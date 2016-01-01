import requests, json
from bs4 import BeautifulSoup as BS

URL = 'http://travel.gc.ca/travelling/border-times-us'


def scrape(port=None):
    return parse(request(), port)


def request():
    return requests.get(URL)


def parse(response, requested_port=None):
    soup = BS(response.text, 'html.parser')
    wait_times = {}
    if soup.find('table'):
        for tr in soup.find('table').find_all('tr', class_='font-small'):
            port = tr.find_all('td')
            port_name = port[0].find('strong').string
            port_info = [br.next_sibling for br in port[0].find_all('br')]
            port_cities, update_time = port_info[0].split('/'), port_info[1].strip('Last updated : ')
            commercial_wait, noncommercial_wait = [wait.string for wait in port[1:]]
            wait_times[port_name] = {
                'port_info': {
                    'port_name': port_name,
                    'from': port_cities[0],
                    'to': port_cities[1]
                },
                'last_updated': update_time,
                'wait_times': {
                    'commercial': commercial_wait,
                    'non_commercial': noncommercial_wait
                }
            }
    return wait_times if requested_port is None else wait_times[requested_port]

if __name__ == '__main__':
    times = scrape('Rainbow Bridge')
    print(json.dumps(times, indent=2))

# Canadian BorderTimes
Web API for wait times for entering the US from Canadian borders.

All data is scraped from the official [Government of Canada](http://travel.gc.ca/travelling/border-times-us) website. Wait times are updated *at least once an hour* (per GC).

## Setup

Fork/clone project, install Python 3 requirements (`pip3 install -r ./requirements.txt`).

Run `border_times.py`. 

## Endpoints

Access the full data set at `127.0.0.1:8000/api`. 

Or retrieve data for a single border at `127.0.0.1:8000//api?port_name={port_name}`. Find a list of port names on the official GC [site](http://travel.gc.ca/travelling/border-times-us).

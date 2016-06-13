## border-times
A web API for interfacing with Canadian border waiting times. All data is scraped from the official [Government of Canada](http://travel.gc.ca/travelling/border-times-us) website. Wait times are updated _at least once an hour_ (per GC).

### Setup

- Clone repo, install requirements.
  
  ```sh
  $ git clone https://github.com/kshvmdn/border-times.git && cd border-times
  ```
  
  ```sh
  $ pip install -r ./requirements.txt
  ```
  
- Run app, should be listening at `localhost:8000`.
  
  ```sh
  $ python ./bordertimes.py
  ```

### Usage

##### Output Format

```js
{
  "meta": {
    "status": Number,
    "message": String
  },
  "data": {
    "port_info": {
      "name": String,
      "from": String,
      "to": String
    },
    "wait_times": {
      "commercial": String,
      "non_commercial": String
    },
    "last_updated": String
  }
}
```

##### Endpoints

| Endpoint      | Description
|---            | ---
| `/api`        | Retrieve the datasets for all ports.
| `/api/list`   | List all available ports.
| `/api/<port>` | Retrieve the dataset for a single port.

##### Examples

```
/api/Rainbow%20Bridge
```


```json
{
  "meta": {
    "status": 200,
    "message": "OK"
  },
  "data": {
    "port_info": {
      "name": "Rainbow Bridge",
      "from": "Niagara Falls, ON",
      "to": "Niagara Falls, NY"
    },
    "wait_times": {
      "commercial": "Not applicable",
      "non_commercial": "no delay 7 lane(s) open"
    },
    "last_updated": "2016-06-13 17:52"
  }
}
```

```
/api/list
```


```json
{
  "meta": {
    "status": 200,
    "message": "OK"
  },
  "data": [
    "Abbotsford-Huntingdon",
    "Aldergrove",
    "Ambassador Bridge",
    "Blue Water Bridge",
    "Boundary Bay",
    "Cornwall",
    "Coutts",
    "Douglas (Peace Arch)",
    "Edmundston",
    "Emerson",
    "Fort Frances Bridge",
    "North Portal",
    "Pacific Highway",
    "Peace Bridge",
    "Prescott",
    "Queenston-Lewiston Bridge",
    "Rainbow Bridge",
    "Sault Ste. Marie",
    "St-Armand/Philipsburg",
    "St-Bernard-de-Lacolle",
    "St. Stephen",
    "St. Stephen 3rd Bridge",
    "Stanstead",
    "Thousand Islands Bridge",
    "Windsor and Detroit Tunnel",
    "Woodstock Road"
  ]
}
```

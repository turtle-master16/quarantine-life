init python:
    import requests
    import json

    access_url = 'https://api.jsonbin.io/v3/b/61a0951f62ed886f9154e4a5'
    master_key = '$2b$10$zxcdZxYcJjoiLzjPPRQKDeBNULrV4/P1Y.J4XRHdn2MGPEkpBvA6u'

    def getJSONBin():
        url = access_url + '/latest'
        headers = {
            'X-Master-Key': master_key,
            'X-Bin-Meta': 'false'
        }

        req = requests.get(url, json=None, headers=headers)
        return req.text

    def updateTraversedRouteRecords(username, password, traversed_routes):
        url = access_url
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': master_key
        }

        jsonBin = json.loads(getJSONBin().encode('ascii','ignore'))
        for index, record in enumerate(jsonBin['traversed_route_records']):
            if record["username"] == username and record["password"] == password:
                if record["traversed_routes"] == traversed_routes:
                    break

                jsonBin['traversed_route_records'].pop(index)
                jsonBin['traversed_route_records'].append({
                    "username": username,
                    "password": password,
                    "traversed_routes": traversed_routes
                })
                break

        else:
            jsonBin['traversed_route_records'].append({
                "username": username,
                "password": password,
                "traversed_routes": traversed_routes
            })

        req = requests.put(url, json=jsonBin, headers=headers)


    # updateTraversedRouteRecords(username="testuser3", password="testuserpassword3", traversed_routes=["mainstart", "test1", "test2"])

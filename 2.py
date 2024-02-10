2. Write a Python script which will do the following:-
   1.List the names of all breweries present in the states of Alaska,Maine and NewYork.
   2.What is the count of breweries in each of the states mentioned above?
   3.Count the number of types of breweries present in individual cities of the state mentioned above.
   4.Count and list how many breweries have websites in the states of Alaska,Maine and New York.


import requests

def get_breweries_in_states(states):
    api_key = 'YOUR_API_KEY'
    base_url = 'https://api.openbrewerydb.org/breweries'
    
    breweries = []
    for state in states:
        params = {'by_state': state}
        response = requests.get(base_url, params=params)
        breweries.extend(response.json())
    
    return breweries

def list_breweries(states):
    breweries = get_breweries_in_states(states)
    brewery_names = [brewery['name'] for brewery in breweries]
    return brewery_names

def count_breweries(states):
    breweries = get_breweries_in_states(states)
    brewery_count = {}
    for brewery in breweries:
        state = brewery['state']
        if state not in brewery_count:
            brewery_count[state] = 0
        brewery_count[state] += 1
    return brewery_count

def count_brewery_types_in_cities(states):
    breweries = get_breweries_in_states(states)
    brewery_types_count = {}
    for brewery in breweries:
        city = brewery['city']
        brewery_type = brewery['brewery_type']
        if city not in brewery_types_count:
            brewery_types_count[city] = {}
        if brewery_type not in brewery_types_count[city]:
            brewery_types_count[city][brewery_type] = 0
        brewery_types_count[city][brewery_type] += 1
    return brewery_types_count

def count_breweries_with_websites(states):
    breweries = get_breweries_in_states(states)
    website_count = {}
    for brewery in breweries:
        state = brewery['state']
        website = brewery['website_url']
        if website:
            if state not in website_count:
                website_count[state] = 0
            website_count[state] += 1
    return website_count

if __name__ == "__main__":
    states = ['Alaska', 'Maine', 'New York']
    
    print("1. List of breweries in Alaska, Maine, and New York:")
    print(list_breweries(states))
    
    print("\n2. Count of breweries in each state:")
    print(count_breweries(states))
    
    print("\n3. Count of brewery types in cities of specified states:")
    print(count_brewery_types_in_cities(states))
    
    print("\n4. Count of breweries with websites in each state:")
    print(count_breweries_with_websites(states))



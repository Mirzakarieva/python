travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},

{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
}
]

def add_new_country(counry_name, times_visited, cities_visited):
    new={
    "country": counry_name,
    "visits": times_visited,
    "cities": cities_visited
}
    travel_log.append(new)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print (travel_log)
import csv 


def load_routes(filename="routes.csv") -> dict:

    """Возвращает {route_id: {"name": str, "stops": list}}"""

    with open(filename, newline="", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:
            route_id = row["route_id"]

            cities = [city.strip() for city in row["stops"].split(",")]
            city_names = [city.strip() for city in row["route_name"].split(",")]

            names = ",".join(city_names)
            stops = ",".join(cities)

            print(f"{route_id} | {names} | {stops}")

def find_route(routes: dict, route_id: int) -> dict | None:

    """O(1) поиск. None если не найден."""

    return routes.get(route_id, None)

def build_stop_index(routes: dict) -> dict:

    """Индекс: {"Алматы": [1, 2, 5], "Астана": [1, 3], ...}"""

    stop_index = {}

    for route_id, route_data in routes.items():
        for stop in route_data:

            if stop not in stop_index:
                stop_index[stop] = []

            stop_index[stop].append(route_id)

    return stop_index


def find_routes_by_stop(stop_index: dict, stop_name: str) -> list:

    """O(1) поиск. Пустой список если не найдено."""

    return stop_index.get(stop_name, [])


routes_dict = {}

print(find_route(routes_dict, 13))
print(load_routes())

stop_index = build_stop_index(routes_dict)
print(stop_index)

specific_routes = find_routes_by_stop(stop_index, "Алматы")
print(specific_routes) 

with open("routes.csv", newline="", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:
        route_id = int(row["route_id"])
        
        cities = [city.strip() for city in row["stops"].split(",")]
        routes_dict[route_id] = cities
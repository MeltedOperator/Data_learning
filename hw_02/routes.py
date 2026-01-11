import csv 

def load_routes(filename="routes.csv") -> dict:
    """Возвращает {route_id: {"name": str, "stops": list}}"""
    routes = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            route_id = row["route_id"]
            cities = [city.strip() for city in row["stops"].split(",")]
            city_names = [city.strip() for city in row["route_name"].split(",")]
            names = ",".join(city_names)
            # route_name = "-".join(cities)
            stops = ",".join(cities)
            cities_info = f"{route_id} | {names} | {stops}"
            routes.append(cities_info)
            print(f"{route_id} | {names} | {stops}")

def find_route(routes: dict, route_id: int) -> dict | None:
    """O(1) поиск. None если не найден."""
    pass

def build_stop_index(routes: dict) -> dict:
    """Индекс: {"Алматы": [1, 2, 5], "Астана": [1, 3], ...}"""
    pass

def find_routes_by_stop(stop_index: dict, stop_name: str) -> list:
    """O(1) поиск. Пустой список если не найдено."""
    pass

print(load_routes())
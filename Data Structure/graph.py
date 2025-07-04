from collections import deque

class FlightGraph:
    def __init__(self):
        self.routes = {}

    def add_country(self, country):
        if country not in self.routes:
            self.routes[country] = []

    def add_flight(self, from_country, to_country):
        self.add_country(from_country)
        self.add_country(to_country)
        self.routes[from_country].append(to_country)
        self.routes[to_country].append(from_country)  # assuming bidirectional flight

    def show_routes(self):
        print("🌍 Available Flight Routes:")
        for country, connections in self.routes.items():
            print(f"{country} ➝ {', '.join(connections)}")

    def is_connected(self, start, destination):
        visited = set()
        queue = deque([start])

        while queue:
            current = queue.popleft()
            if current == destination:
                return True
            visited.add(current)
            for neighbor in self.routes.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)
        return False

# -------------------------------
# ✈️ Example usage

graph = FlightGraph()

# Add flight connections
graph.add_flight("Pakistan", "UAE")
graph.add_flight("UAE", "UK")
graph.add_flight("Pakistan", "Turkey")
graph.add_flight("Turkey", "Germany")
graph.add_flight("Germany", "France")
graph.add_flight("India", "USA")

graph.show_routes()

# Check connectivity
print("\n🔎 Can you fly from Pakistan to France?")
print("Yes!" if graph.is_connected("Pakistan", "France") else "No!")

print("\n🔎 Can you fly from India to UK?")
print("Yes!" if graph.is_connected("India", "UK") else "No!")







Here is the complete Python code that generates a geospatial path of a small fast boat traveling from **Oceanside, CA** to **Catalina Island** with a position every 5 seconds at 35 knots:

```python
import math
import pandas as pd
from datetime import datetime, timedelta

# Coordinates (latitude, longitude)
start = (33.1959, -117.3795)  # Oceanside, CA
end = (33.3879, -118.4163)    # Catalina Island

# Compute great-circle distance (Haversine formula)
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth radius in meters
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# Calculate bearing
def bearing(lat1, lon1, lat2, lon2):
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dlambda = math.radians(lon2 - lon1)
    y = math.sin(dlambda) * math.cos(phi2)
    x = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(dlambda)
    return (math.degrees(math.atan2(y, x)) + 360) % 360

# Compute destination point given start, bearing, and distance
def destination_point(lat, lon, bearing_deg, distance_m):
    R = 6371000
    brng = math.radians(bearing_deg)
    phi1 = math.radians(lat)
    lambda1 = math.radians(lon)
    phi2 = math.asin(math.sin(phi1) * math.cos(distance_m / R) + math.cos(phi1) * math.sin(distance_m / R) * math.cos(brng))
    lambda2 = lambda1 + math.atan2(math.sin(brng) * math.sin(distance_m / R) * math.cos(phi1), math.cos(distance_m / R) - math.sin(phi1) * math.sin(phi2))
    return math.degrees(phi2), math.degrees(lambda2)

# Parameters
distance = haversine_distance(*start, *end)
brg = bearing(*start, *end)
speed_knots = 35  # Boat speed
speed_mps = speed_knots * 0.514444  # Convert knots to m/s
interval = 5  # seconds
step_distance = speed_mps * interval

# Generate points
total_points = int(distance / step_distance)
start_time = datetime(2025, 10, 17, 12, 0, 0)

path = []
for i in range(total_points + 1):
    t = start_time + timedelta(seconds=i * interval)
    lat, lon = destination_point(*start, brg, i * step_distance)
    path.append({'timestamp': t.isoformat(), 'latitude': lat, 'longitude': lon})

# Create DataFrame
df = pd.DataFrame(path)
print(df.head())
print(df.tail())
print(f"Generated {len(df)} points.")
```

This script calculates the great‑circle path, outputs intermediate coordinates with timestamps, and displays the first and last few rows from the resulting trajectory.

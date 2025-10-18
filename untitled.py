# spatial functions


def destination_point(lat1, lon1, bearing, distance, radius=6371):
    """Returns destination lat/lon given origin, bearing, and distance."""
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    bearing = math.radians(bearing)
    
    lat2 = math.asin(math.sin(lat1) * math.cos(distance / radius) +
                     math.cos(lat1) * math.sin(distance / radius) * math.cos(bearing))
    lon2 = lon1 + math.atan2(math.sin(bearing) * math.sin(distance / radius) * math.cos(lat1),
                             math.cos(distance / radius) - math.sin(lat1) * math.sin(lat2))
    
    return math.degrees(lat2), math.degrees(lon2)



def destination_point_with_drift(lat1, lon1, bearing, distance,
                                 current_bearing, current_strength,
                                 wind_bearing, wind_speed,
                                 radius=6371):
    """
    Returns destination lat/lon given origin, bearing, distance,
    and additional effects of current and wind.
    """
    
    # Convert all angles to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    bearing = math.radians(bearing)
    current_bearing = math.radians(current_bearing)
    wind_bearing = math.radians(wind_bearing)

    # Convert each vector to east/north components (magnitude, direction)
    v_vehicle_x = math.sin(bearing)
    v_vehicle_y = math.cos(bearing)

    v_current_x = current_strength * math.sin(current_bearing)
    v_current_y = current_strength * math.cos(current_bearing)

    v_wind_x = wind_speed * math.sin(wind_bearing)
    v_wind_y = wind_speed * math.cos(wind_bearing)

    # Combine velocity vectors
    v_total_x = v_vehicle_x + v_current_x + v_wind_x
    v_total_y = v_vehicle_y + v_current_y + v_wind_y

    # Compute resultant bearing and scale distance accordingly
    resultant_bearing = math.atan2(v_total_x, v_total_y)
    resultant_speed_ratio = math.hypot(v_total_x, v_total_y)
    adj_distance = distance * resultant_speed_ratio

    # Great-circle destination formula
    lat2 = math.asin(math.sin(lat1) * math.cos(adj_distance / radius) +
                     math.cos(lat1) * math.sin(adj_distance / radius) * math.cos(resultant_bearing))
    lon2 = lon1 + math.atan2(math.sin(resultant_bearing) * math.sin(adj_distance / radius) * math.cos(lat1),
                             math.cos(adj_distance / radius) - math.sin(lat1) * math.sin(lat2))

    return math.degrees(lat2), math.degrees(lon2)


def adjust_bearing(lat1, lon1, dest_lat, dest_lon):
    





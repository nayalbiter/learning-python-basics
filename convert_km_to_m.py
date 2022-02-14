print("Insert distance in km")
distance_km_string = input ()
distance_km_number = int(distance_km_string)
distance_m_number = distance_km_number * 0.62137
distance_m_string = str(distance_m_number)
print(distance_km_string + " km are equivalent to " + distance_m_string + " m")

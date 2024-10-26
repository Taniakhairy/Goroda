from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"


key = 'caa0c4f70c3448c5b818f69bc75751ef'
city = "London"
coordinates = get_coordinates(city,key)
print(f"Координаты города {city}: {coordinates}")



from handler.api_handler import Weather

query = Weather()
query.weather = "多云"
query._translate()

query.city = "beijing"
query._get_city_code()
print(query.city_code == '101010100')

assert query.resp != "Partly Cloudy", False
assert query.city_code == '101010100', True

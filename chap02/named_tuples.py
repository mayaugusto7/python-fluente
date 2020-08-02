from collections import namedtuple, OrderedDict

City = namedtuple('City', 'name country population coordinates')  # tuple object with name
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print('\nOthers attributes')

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
print(City._make(delhi_data))
delhi = City._make(delhi_data)
print(delhi._asdict())
OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935), ('coordinates', LatLong(lat=28.613889,
                                                                                                       long=77.208889))]
            )

for key, value in delhi._asdict().items():
    print(key + ':', value)



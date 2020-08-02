lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# BRA/CE342567
# ESP/XDA205856
# USA/31195855

for country, _ in traveler_ids:
    print(country)

# USA
# BRA
# ESP

# Desempacotamento de tuplas
latitude, longitude = lax_coordinates
print(latitude)
# 33.9425
print(longitude)
# -118.408056

divmod(20, 8)
# (2, 4)
t = (20, 8)
divmod(*t)
# (2, 4)
quotient, remainder = divmod(*t)
print(quotient)
# 2
print(remainder)
# 4

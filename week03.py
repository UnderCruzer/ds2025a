def duplicate_city(cities):
    result_city = []
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)
    return result_city



cities = ['Incheon', 'Seoul', 'Incheon', 'Incheon', 'Gwangju']
#cities = set(cities)
#cities.add('Incheon')
#cities.add('Suwon')
cities.append('Incheon')
cities.append('Suwon')
cities.append('Seoul')
# 딕셔너리와 리스트는 순서를 갖지 않는다. (중복값은 존재하지 않음) -> 딕셔너리의 키 값만 존재하는것을 set
print(cities)
print(set(duplicate_city(cities))) #중복값찾기
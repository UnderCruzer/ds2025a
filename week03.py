cities = ['Incheon', 'Seoul', 'Incheon', 'Incheon', 'Gwangju']
cities = set(cities)
cities.add('Incheon')
cities.add('Suwon')
# 딕셔너리와 리스트는 순서를 갖지 않는다. (중복값은 존재하지 않음) -> 딕셔너리의 키 값만 존재하는것을 set
print(cities)
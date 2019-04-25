# 인수가 하나뿐인 함수가 아니라면 리스트 컴프리헨션이 내장함수 map 보다 명확
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in a]
print(squares)

# map 일경우 아래와 같다
squares_lambda = map(lambda x: x ** 2, a)
print(list(squares_lambda))

# 이런식으로도 가능
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

# 이게 읽기 힘듬 위와 같은 예제임
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(list(alt))

# 익셔너리와 세트에도 리스트 컴프리헨션에 해당하는 문법이 존재함
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

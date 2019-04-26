def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# 제너레이터를 사용할경우 다음과 같다
# 결과는 [] 으로 문제가 발생한다
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


# 위 문제를 해결하기 위해 복사본을 리스트에 저장
# 다만 또 문제가 복사본이 클수도 있기때문에 메모리 고갈되서 망할확률있음
def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# 위 문제해결방법은 호출될때마다 새 이터레이터를 반환하는 함수를 받게 만드는것
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


# 위 방법을 실행하기엔 더러우므로 이터레이터 프로토콜을 구현하는 새 컨테이너 클래스를 제공하자
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


# 여러번 순회할때는 아래 방법이 좋음
def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


if __name__ == '__main__':
    visits = [15, 35, 80]
    percentages = normalize(visits)
    print(percentages)

    # 이미 소진되었기 떄문에 없음...
    it = read_visits('tmp/my_numbers.txt')
    percentages2 = normalize(it)
    print(percentages2)

    # 카피 떴다..
    it = read_visits('tmp/my_numbers.txt')
    percentages3 = normalize_copy(it)
    print(percentages3)

    # 람다 표현식을 써야하지만 좀 더럽다..
    percentages4 = normalize_func(lambda: read_visits('tmp/my_numbers.txt'))

    # 잠깐 하나 추가
    percentages_ex = normalize_defensive(visits)
    print(percentages_ex)

    # 입력데이터를 여러번 읽는다는 단점이 존재함
    visits = ReadVisits('tmp/my_numbers.txt')
    percentages5 = normalize(visits)
    print(percentages5)

    # 여기에도 잠깐 하나 추가
    percentages_ex2 = normalize_defensive(visits)
    print(percentages_ex2)

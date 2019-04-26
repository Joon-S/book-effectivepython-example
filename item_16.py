# 코드가 복잡, 깔끔 x 또한 새로운 결과가 나올때마다 append 호출
# 추가적으로 모든 결과를 리스트에 저장해야함
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


# 위와 동일한데 더 좋은 방식임
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


# 한번에 한줄씩 읽어서 한번에 한 단어씩 출력하는 제너레이터
# 반환되는 데이터에 상태가 있고 재사용 불가하다는것을 알아야한다
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


if __name__ == '__main__':
    address = 'Four score and seven years ago...'
    result = index_words(address)
    result2 = list(index_words_iter(address))
    print(result2[:3])

    # index_file 쓰는 방법
    with('/path/', 'r') as f:
        it = index_file(f)
        results = islice(it, 0, 3)
        print(list(results))

# 기본
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = '. '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


# 개선
def log2(message, *values):
    if not values:
        print(message)
    else:
        values_str = '. '.join(str(x) for x in values)
        print('%s: %s ' % (message, values_str))


# 참고로 제너레이터와 * 연산자가 함께 사용하면 프로그램이 망가질 확률 높다
# 자바의 args... 이거랑 문제점 등등 다 똑같음
if __name__ == '__main__':
    log('My numbers are', [1, 2])
    log('Hi there', [])

    log2('My numbers are', 1, 2)
    log2('Hi there')

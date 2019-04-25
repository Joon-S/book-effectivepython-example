# 아래가 일반적인 처리
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# 문제는 또 None 처리를 해줘야함...자바도 이런거 엄청 싫어해서 바꾸었는데
result = divide(1, 1)
if result is None:
    print('Invalid inputs')


# 튜플을 이용하는 방법도 있는데 이건 너무 꼴보기 싫다
def divide2(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


# 바로 이게...좀 거시기하다
success, result2 = divide2(1, 1)
if not success:
    print('Invalid inputs')


# 가장 좋은 방법은 아래와 같다
# 바로 예외를 던져주는것이다...근데 자바는 빈배열이나 이렇게 보내주는데
# 파이썬도 그렇게 하면 안되나...? 일단 참고만하자
def divide3(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x, y = 5, 2
try:
    result = divide3(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)

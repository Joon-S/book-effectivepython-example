# for 와 while 루프 뒤에는 else 블럭을 쓰지 말자
# 뭔소리인지 이해하기 힘듬
for i in range(3):
    print('Loop %d' % i)
    if i == 1:
        break
else:
    print('Else block!')


# 헬퍼함수는 이런식으로 작성하자 (뭐...다른 언어에서도 이렇게 쓰고있겠지만..)
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % 1 == 0 and b % i == 0:
            return False
    return True


def coprime2(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

# 기본
def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# 기존 키워드 인수는 강제할수없는 문제때문에 이렇게 하면 됨
# 바로 키워드 인자 앞에 * 를 넣는거다
def safe_division2(number, divisor, *, ignore_overflow=False,
                   ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


if __name__ == '__main__':
    result = safe_division(1, 1, True, False)
    print(result)

    result2 = safe_division2(1, 1, ignore_zero_division=True)
    print(result2)

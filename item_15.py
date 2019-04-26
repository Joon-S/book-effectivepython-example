# 데이터
numbers_1 = [8, 3, 1, 2, 5, 4, 7, 6]
group_1 = {2, 3, 5, 7}


# 올바른 방법이긴한데 긴함수에는 쓰지말것..
def sort_priority3(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return 0, x
        return 1, x

    numbers.sort(key=helper)
    return found


# 길어지면 헬퍼 클래스로 상태를 감싸는 방법이 좋음
class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x


sorter = Sorter(group_1)
numbers_1.sort(key=sorter)
assert sorter.found is True

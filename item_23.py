# 컴포넌트 사이의 간단한 인터페이스용으로 클래스를 정의
# 인스턴스를 생성하는 대신에 함수만 써도 종종 충분
class BetterCountMissing(object):

    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


if __name__ == '__main__':
    names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
    names.sort(key=lambda x: len(x))
    print(names)

    counter = BetterCountMissing
    counter()


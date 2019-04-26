import json
from datetime import datetime
from time import sleep


# 기존
def log(meesage, when=datetime.now()):
    print('%s: %s ' % (when, meesage))


# 개선 - 문서화 하는게 관례임
def log2(message, when=None):
    """Log a message with a timestamp

    Args:
        message: Message to print
        when: datetime of when the message occurred
            Default to the present time.
    """
    when = datetime.now() if when is None else when
    print('%s: %s ' % (when, message))


# 위와 같은 원리로 이런 문제가 발생할수있음
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


# 위에꺼 개선
# 설령 잘못쓴다고 한들 파이참에서 자동수정하면 됨
def decode2(data, default=None):
    """Load JSON data from a string

    Args:
        data: JSON data to decode
        default: Value to return if decoding fails.
            Defaults to an empty dictionary
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


if __name__ == '__main__':
    # 함수를 정의할때 딱 한번만 실행되기때문에 시간은 같음
    log('Hi there')
    sleep(0.1)
    log('Hi again')

    # 이제 실시간으로 나오게 됨
    log2('Hi there')
    sleep(0.1)
    log2('Hi again')

    # 위와 똑같이 함수를 정의할때 딱 한번만 실행되서 결국 같은게 출력
    foo = decode('bad data')
    foo['stuff'] = 5
    bar = decode('also bad')
    bar['meep'] = 1
    print('Foo: ', foo)
    print('Bar: ', bar)

# Basic
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)

# Bad 인덱스를 알고싶은경우
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))

# Good 인덱스를 알고싶은경우
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))

# 숫자 지정도 가능 참고로 기본이 start=0 임
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))


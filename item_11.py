names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

# 반복문이 꼴보기 싫은 케이스
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
        print(longest_name)

# enumerate 를 써도 썩...
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
        print(longest_name)

# zip 이터레이터를 사용했을경우
# 대신에 두개의 길이가 딱 맞지 않으면 이터레이터가 끝날때까지 튜플을 계속 넘겨주기때문에
# 실행할 리스트의 길이가 같다고 확신할수없다면 내장 모듈 itertools 의 zip_longest 를 사용
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

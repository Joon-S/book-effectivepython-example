# case 2 경우처럼 혼동할수있기 때문에
# stride 를 start, end 와 함께 쓰지말것! 사용해야한다면
# 양수값과 start, end 는 생략 꼭 사용해야한다면 stride 값에 또 start 나 end 를 걸어주는형식으로
# 내장 모듈 itertools 의 islice 를 사용하길

# case 1
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

# case 2
a2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a2[2::2])
print(a2[-2::-2])
print(a2[-2:2:-2])
print(a2[2:2:-2])

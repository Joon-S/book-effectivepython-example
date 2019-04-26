# 기본
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period


# 개선
def flow_rate2(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


if __name__ == '__main__':
    # 각 인자가 뭘 뜻하는지 정확히 모름
    print(flow_rate(20, 7, 1))

    # 개선된 부분
    # 선택적인 키워드 인수는 항상 위치가 아닌 키워드로 넘기자
    # 즉 1 이 아니라 period=1 이런식으로
    print(flow_rate(20, 7, period=1))

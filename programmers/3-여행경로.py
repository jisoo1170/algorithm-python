import pytest


def solution(tickets):
    routes = {}
    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]
    for r in routes:
        routes[r].sort(reverse=True)
    print(routes)

    stack = ['ICN']
    answer = []
    while stack:
        top = stack[-1]
        # top 이라는 키가 없을 경우를 위해서 if문을 써줘야 한다.
        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
            continue
        stack.append(routes[top].pop())
    return answer[::-1]


@pytest.mark.parametrize("tickets, expected", [
    ([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']],
        ['ICN', 'JFK', 'HND', 'IAD']),
    ([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'],
        ['ATL', 'ICN'], ['ATL', 'SFO']],
        ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'])
])
def test_simple(tickets, expected):
    assert solution(tickets) == expected


"""
    def solution(tickets):
        answer = ['ICN']
        tickets.sort(key=lambda x: x[1])
        leng = len(tickets)
        while len(answer) <= leng:
            for idx, t in enumerate(tickets):
                if t[0] == answer[-1]:
                    answer.append(t[1])
                    del tickets[idx]
                    break
        print(answer)
        return answer

이렇게 풀었는데 시간초과가 나왔다. list에서 del하는 부분이 시간 복잡도가 n이라서 그런 것 같다.


    def solution(tickets):
        routes = {}
        for (start, end) in tickets:
            routes[start] = routes.get(start, []) + [end]
        for r in routes:
            routes[r].sort(reverse=True)

        stack = ['ICN']
        answer = ['ICN']
        while len(answer) <= len(tickets):
            top = answer[-1]
            # top 이라는 키가 없을 경우를 위해서 if문을 써줘야 한다.
            if top not in routes or len(routes[top]) == 0: 
                continue
            answer.append(routes[top].pop())
        return answer

위와 같은 코드로 바꿨는데 시간 초과가 났다.
그래서 정답 코드로 바꿨는데 통과했다. 시간 복잡도가 똑같을 것 같은데 뭔지 모르겠네ㅜㅜㅜㅜㅜㅜ끠악
"""

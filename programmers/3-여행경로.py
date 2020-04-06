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

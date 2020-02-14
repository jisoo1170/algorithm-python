# pytest

python 기반 테스트 프레임워크. leetcode, programmers 는 웹 ide를 제공해주지만 느리고 버벅거려 한국인 성질에 답답할 수 있다. pytest 를 통해 빠르게 알고리즘 구현이 맞는지 확인해보쟈



## getting started

```python
$ pip install -U pytest
```

바로 깔림! 



파일 이름은 `test` 여야한다.  `pytest` 를 치면 테스트 코드가 실행된다. 여러 파일을 테스트하고싶다면 파일에 `test_*.py` 또는 `*_test.py` 로 작성하면 된다. 



## pytest-watch

매번 pytest 를 치기 귀찮을경우 계속 돌려놓을 수 있다 

```python
$ pip install pytest-watch
```

`ptw` 명령어를 치면 시작하는데, 테스트 파일이 바뀌면 자동으로 테스트를 실행해준다. 



## example

알고리즘 짠 코드 

```python
input = []
output = 2

def test_simple():
    assert solution(input) == expected


def solution(nums):
    """code"""
    return 11

if __name__ == "__main__":
    solution(input)
```


sample

```python
@pytest.mark.parametrize("base, expected", [
    (10, [3, 9]),
    (3, [2]),
    (9, [2, 4, 8]),
    (26, [5, 25]),
    (30, [29])
])
def test_simple(base, expected):
    assert solution(base) == expected


def solution(base):
    arr = []
    for i in range(2, base):
        if (base - 1) % i == 0:
            arr.append(i)
    return arr


if __name__ == "__main__":
    solution(input)
```



출처 [숨토피아](https://github.com/soomtopia)
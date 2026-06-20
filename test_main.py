from typing import Any, Callable
from incomplete_main import map

TestCase = tuple[list[Any], Callable[[Any], Any], list[Any]]

run_cases: list[TestCase] = [
    ([1, 2, 3], lambda x: x * x, [1, 4, 9]),
    ([0, 5, -2], lambda x: f"Item: {x}", ["Item: 0", "Item: 5", "Item: -2"]),
]

submit_cases: list[TestCase] = run_cases + [
    ([], lambda x: x + 1, []),
    ([True, False, True], lambda x: not x, [False, True, False]),
    (["apple", "pi", "banana"], len, [5, 2, 6]),
]


def test(iterable: list[Any], func: Callable[[Any], Any], expected: list[Any]) -> bool:
    print("---------------------------------")
    print(f"Input List: {iterable}")
    print(f"Expected:   {expected}")
    try:
        result = map(iterable, func)
        print(f"Actual:     {result}")
        if str(result) != str(expected):
            return False
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

import random
from typing import Dict, Tuple


def test_return_multi_param():
    def get_number_and_str() -> Tuple[int, str]:
        n = random.randint(1, 5)
        m: Dict[int, str] = {1: "one", 2: "two", 3: "three"}
        s = m.get(n, "nan")
        return n, s

    n, s = get_number_and_str()
    print(f"number={n}, string={s}")


if __name__ == "__main__":
    test_return_multi_param()

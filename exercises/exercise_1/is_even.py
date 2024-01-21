import timeit


class IsEven:
    def __init__(self, value: int) -> None:
        self.value = value

    def is_even_division(self) -> bool:
        return self.value % 2 == 0

    def is_even_binary(self) -> bool:
        return self.value & 1 == 0

    def speed_test_division(self) -> float:
        code = "x = 2; iseven = IsEven(x); iseven.is_even_division(); x"
        return min(
            timeit.repeat(
                code,
                setup="from exercises.exercise_1.is_even import IsEven",
                number=10000,
                repeat=10,
            )
        )

    def speed_test_binary(self) -> float:
        code = "x = 2; iseven = IsEven(x); iseven.is_even_binary(); x"
        return min(
            timeit.repeat(
                code,
                setup="from exercises.exercise_1.is_even import IsEven",
                number=10000,
                repeat=10,
            )
        )

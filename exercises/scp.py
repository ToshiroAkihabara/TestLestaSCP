import logging

from exercises.exercise_1 import IsEven
from exercises.exercise_2 import FifoDeque, FifoList
from exercises.exercise_3 import Sort


class SCP:
    def __init__(
        self, items: list[int] = [5, 6, 10, 23], value: int = 2, log_file=False
    ) -> None:
        if log_file:
            self.logger = logging.basicConfig(
                level=logging.DEBUG, filemode="w", filename="log.txt"
            )
        self.logger = logging.basicConfig(level=logging.DEBUG)
        self.value = value
        self.items = items
        self.is_even = IsEven(value=self.value)
        self.fifo_list = FifoList()
        self.fifo_deque = FifoDeque()
        self.sort = Sort()

    def is_even_division_show(self) -> bool:
        result = self.is_even.is_even_division()
        speed_test = self.is_even.speed_test_division()
        logging.debug(f"Division: Is number {self.value} even? {result}")
        logging.debug(f"Speedtest_division: {speed_test}")
        return result

    def is_even_binary_show(self) -> bool:
        result = self.is_even.is_even_binary()
        speed_test = self.is_even.speed_test_binary()
        logging.debug(f"Binary: Is number {self.value} even? {result}")
        logging.debug(f"Speedtest_binary: {speed_test}")
        return result

    def fifo_list_show(self) -> list[list, str]:
        [self.fifo_list.add_item(item) for item in self.items]
        [self.fifo_list.delete_item() for _ in self.items]
        self.fifo_list.delete_item()

    def fifo_deque_show(self) -> list[list, str]:
        [self.fifo_deque.add_item(item) for item in self.items]
        [self.fifo_deque.delete_item() for _ in self.items]
        self.fifo_deque.delete_item()

    def sort_show(self) -> list[int]:
        result = self.sort.merge_sort(self.items)
        logging.debug(f"Mergesort result: {result}")
        return result

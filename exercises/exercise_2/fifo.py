import logging
from abc import ABC
from collections import deque


class Fifo(ABC):
    def __init__(self, storage_items: list[int] | deque[int]) -> None:
        self.storage_items = storage_items

    def add_item(self, item: int) -> None:
        self.storage_items.append(item)
        logging.debug(f"Inserted {item}. Items in list: {self.storage_items}.")

    def delete_item(self) -> int:
        if self.storage_items:
            item = self.pop()
            logging.debug(
                f"Return and delete {item}. Items in list: {self.storage_items}."
            )
            return item
        logging.debug(f"No more items in {self.storage_items}.")
        return False

    def pop(self) -> int:
        raise NotImplementedError()


class FifoList(Fifo):
    def __init__(self) -> None:
        super().__init__(storage_items=[])

    def pop(self) -> int:
        return self.storage_items.pop(0)


class FifoDeque(Fifo):
    def __init__(self) -> None:
        super().__init__(storage_items=deque([]))

    def pop(self) -> int:
        return self.storage_items.popleft()

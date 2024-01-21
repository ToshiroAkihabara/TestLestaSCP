from exercises.scp import SCP


def server_core_programmer(items: list[int], value: int) -> None:
    scp = SCP(items=items, value=value, log_file=False)
    scp.is_even_division_show()
    scp.is_even_binary_show()
    scp.fifo_list_show()
    scp.fifo_deque_show()
    scp.sort_show()


def main() -> None:
    items = [2, 2, 1, 15, -2, 23, 36, 72, 105, 0, -52]
    value = 2
    server_core_programmer(items=items, value=value)


if __name__ == "__main__":
    main()

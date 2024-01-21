class Sort:
    @classmethod
    def merge_sort(cls, arr: list[int]) -> list[int]:
        if len(arr) > 1:
            middle = len(arr) // 2
            left = arr[:middle]
            right = arr[middle:]
            cls.merge_sort(left)
            cls.merge_sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr

from typing import Optional, List, Callable, Dict
import time

class Methods:

    def __init__(self, data: List | None) -> None:
        self.data = data

    @staticmethod
    def timer(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Dict:
            data_len = len(args[0].data)

            time_start = time.time()
            result = func(*args, **kwargs)
            time_spent = time.time() - time_start
            print(f'Потраченное время функции `{func.__name__}` на обработку {data_len} чисел',
                  f'Составляет - {"{:.2f}".format(time_spent)} секунд', sep='\n')

            return {'time_spent': time_spent, 'data_len': data_len,'result': result}

        return wrapper

    @timer
    def _min(self) -> Optional[int]:
        if not self.data: return

        min_value = self.data[0]
        for val in self.data:
            if val < min_value:
                min_value = val

        return min_value

    @timer
    def _max(self) -> Optional[int]:
        if not self.data: return

        max_value = self.data[0]
        for val in self.data:
            if val > max_value:
                max_value = val

        return max_value

    @timer
    def _sum(self) -> Optional[int]:
        if not self.data: return

        array_sum = 0
        for val in self.data:
            array_sum += val


        return array_sum

    @timer
    def _mult(self) -> Optional[int]:
        if not self.data: return

        array_mult = 1
        for val in self.data:
            array_mult *= val

        return array_mult
import matplotlib
import matplotlib.pyplot as plt
from methods import Methods
from typing import List, Callable

matplotlib.use('MacOSX')

plt.title('Зависимость времени выполнения функции `_sum` и `_mult` от кол-ва чисел в файле')
plt.xlabel('Количество чисел в файле')
plt.ylabel('Время выполнения')
data = [[_ for _ in range(1, __ + 1)] for __ in [___ for ___ in range(0, 100001, 5000)]]

sum_result = []
mult_result = []

for data_set in data:
    methods = Methods(data_set)
    sum_result.append(methods._sum())
for data_set in data:
    methods = Methods(data_set)
    mult_result.append(methods._mult())


_sum = plt.plot([_['data_len'] for _ in sum_result], [_['time_spent'] for _ in sum_result], label='sum', marker='o')
_mult = plt.plot([_['data_len'] for _ in mult_result], [_['time_spent'] for _ in mult_result], label='mult', marker='^')
plt.legend()
plt.show()
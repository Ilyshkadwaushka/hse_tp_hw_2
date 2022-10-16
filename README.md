![Master Branch Status](https://github.com/Ilyshkadwaushka/hse_tp_hw_2/actions/workflows/ci_master.yml/badge.svg?branch=master) 
![Develop Branch Status](https://github.com/Ilyshkadwaushka/hse_tp_hw_2/actions/workflows/ci_develop.yml/badge.svg?branch=develop)

# Техническое задание 2 <hr>

### Описание стуктуры проекта
Проект четко структурирован. Все рабочие в файлы вынесены в отдельные модули: `fileReader`, `methods`, `test` 
и `chartPrinter`.<br/><br/>
Модуль `fileReader` содержит в себе `fileReader.py`, где реализован класс `FileReader` для чтения входного файла.<br/><br/>
Модуль `methods` содержит в себе `methods.py`, где реализован класс `Methods`, содержащий в себе функции для поиска
минимального, максимального значения, а также для поиска значения, полученного при перемножении или суммировании всех
значений файла.<br/><br/>
Модуль `test` содержит в себе `test.py`, где реализован класс `TestMethods` для тестирования написанных
методов для работы с значениями, полученными из входного файла.<br/><br/>
Модуль `chartPrinter` содержит в себе `chartPrinter.py`, где реализован вывод графика зависимости времени
работы функции `_sum` и `_mult` от количества входных данных.<br/><br/>


### Входные данные:
Данная программа в качестве входных данных принимает файл, состоящий из значений типа данных `Intiger` и `Float`.
Количество значений во входном файле не ограничено.

### Тестирование: 
Для тестирования методов была выбрана библиотека `Unittest`. В файле с тестами по умолчанию указан входной файл `file.txt`.
Для тестирования методов со значениями из своего входного файла необходимо переименовать переменную `FILE_PATH` на 7 строке в
файле `test.py`, который содержится в модуле `test`.

Также реализована возможность получения уведомлений об успешном или неуспешном прохождении автоматического тестирования
в группе telegram с помощью интеграции telegram бота. [Ссылка на telegram группу](https://t.me/+GXhfsUHnBRQ4NmE6)

### Функционал программы:
1. `_min`  - поиск минимального значения во входном файле
2. `_max`  - поиск максимального значения во входном файле
3. `_sum`  - результат суммирования значений входного файла
4. `_mult` - результат умножения значений входного файла

### График зависимости времени выполнения функций `_sum` и `_mult` от кол-ва чисел в файле:<br/>
![Chart](https://github.com/Ilyshkadwaushka/hse_tp_hw_2/raw/master/images/chart.png)

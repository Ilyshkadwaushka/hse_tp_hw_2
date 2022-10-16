from methods import Methods
from fileReader import FileReader

if __name__ == '__main__':
    data = FileReader(input('Введите название файла: '))
    methods = Methods(data())

    methods._min()
    methods._max()
    methods._sum()
    print(methods._mult())
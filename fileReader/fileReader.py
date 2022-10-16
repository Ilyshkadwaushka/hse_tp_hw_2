from typing import AnyStr, Optional, List
import logging

logging.basicConfig(level=logging.INFO)

class FileReader:

    def __init__(self, file_path: AnyStr) -> None:
        self.file_data = self.__read_file(file_path)

    def __read_file(self, file_path: AnyStr) -> Optional[List]:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return list(map(int, file.readline().split()))
        except (FileExistsError, FileNotFoundError) as exception:
            logging.error(exception)

    def __call__(self, *args, **kwargs):
        return self.file_data
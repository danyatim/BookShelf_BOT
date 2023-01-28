from re import findall, DOTALL

from itertools import count

BOOK_PATH = 'book/book'
PAGE_SIZE = 1000

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    page = text[start:page_size + start]
    regex = findall(r'(.+[?!:;,.]+\s)|(.+[^?!:;,]\.+$)', page, flags=DOTALL)

    return_page = ''.join(
        [string for tpl in regex for string in tpl]
    ).strip()

    return return_page, len(return_page)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    numerate = count(1)
    start_part = 0

    with open(path, 'r', encoding='utf-8') as file:
        txt = file.read()

    while True:
        text_part, end_page = _get_part_text(text=txt, start=start_part, page_size=PAGE_SIZE)
        start_part += end_page
        if text_part:
            book.setdefault(next(numerate), text_part.lstrip())
        else:
            break


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)

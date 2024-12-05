import os
from typing import List, Dict, Optional


def search_util(books: List[Dict], search_obj: str | int) -> Dict | None:
    for idx, itm in enumerate(books):
        if search_obj in (itm['title'], itm['author'], itm['year']):
            return itm
        return None


def get_book_by_id(books: List[Dict], book_id: int) -> Optional[Dict] | None:
    for book in books:
        if book.get("id") == book_id:
            return book
    return None


def path_exists(path: str) -> bool:
    if os.path.exists(path):
        return True
    return False
#!/usr/bin/env python3
"""
get the contect
"""
index_range = __import__('0-simple_helper_function').index_range
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get the content of the page """

        assert (type(page) is int and type(page_size) is int) and (
                page > 0 and page_size > 0)

        ranges = index_range(page, page_size)
        data = self.dataset()
        if len(data) < ranges[0] or ranges[1] > len(data):
            return []

        return data[ranges[0]: ranges[1]]

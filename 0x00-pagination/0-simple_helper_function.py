#!/usr/bin/env python3
"""
get the first index and the last index of the page
"""


def index_range(page: int, page_size: int) -> tuple:
    """ 
    function named index_range that takes 
    two integer arguments page and page_size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

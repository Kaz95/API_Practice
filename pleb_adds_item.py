# !/usr/bin/python
from pleb_adds_rows import pleb_adds_rows
from pleb_search import pleb_search

search_results = pleb_search()   # Holds API info for slicing into pleb_adds_rows


def pleb_adds_item():
    pleb_adds_rows('store', search_results[0], search_results[1])


if __name__ == '__main__':
    pleb_adds_item()

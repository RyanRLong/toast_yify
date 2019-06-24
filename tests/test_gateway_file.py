#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import csv
import toast_yify.gateway.file as db



__author__ = "Ryan Long"
__copyright__ = "Ryan Long"
__license__ = "mit"



@pytest.fixture
def db_file():
    global htmldoc
    with open(
            "./../tests/fixtures/view-source_https___yts.lt_browse-movies.html") as html_file:
        htmldoc = html_file.read()


def test_fetch_latest_entries():
    for row in db.fetch_latest_entries():
        assert row == {
            'categories': 'Comedy, Family',
            'image_url': 'https://img.yts.lt/assets/images/movies/cecil_2019/medium-cover.jpg',
            'name': 'Cecil (2019)',
            'rating': '6.7 / 10',
        }
        break

def test_add_entry():
    row = {
        'categories': 'Comedy, Family',
        'image_url': 'https://img.yts.lt/assets/images/movies/cecil_2019/medium-cover.jpg',
        'name': 'Cecil (2019)',
        'rating': '6.7 / 10',
    }

def test_add_entries():
    pass


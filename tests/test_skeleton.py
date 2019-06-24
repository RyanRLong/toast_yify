#!/usr/bin/env python
# -*- coding: utf-8 -*-

from toast_yify.skeleton import get_latest_x_entries_from_persistence, \
    get_latest_x_entries_from_site, update, parse_entries_from_html

__author__ = "Ryan Long"
__copyright__ = "Ryan Long"
__license__ = "mit"


def test_update_WhenSuccessful_ReturnsTrue():
    assert update() is True


def test_update_WhenFails_PrintsError(capsys):
    # captured = capsys.readouterr()
    # assert captured.out == "hello\n"
    # assert captured.err == "world\n"
    pass


def test_get_latest_x_entries_from_site_withEntries_ReturnsListWithTenEntries():
    assert len(get_latest_x_entries_from_site()) == 10


def test_get_latest_x_entries_from_site_withFiveEntries_ReturnsListWithFiveEntries():
    assert len(get_latest_x_entries_from_site(5)) == 5


def test_get_latest_x_entries_from_persistence_withEntries_ReturnsListWithTenEntries():
    assert len(get_latest_x_entries_from_persistence()) == 10


def test_get_latest_x_entries_from_persistence_withFiveEntries_ReturnsListWithFiveEntries():
    assert len(get_latest_x_entries_from_persistence(5)) == 5

def test_parse_entries_from_html_withValidHtml_ReturnsParsedEntries():
    with open("./fixtures/view-source_https___yts.lt_browse-movies.html", "r") as html_file:
        html = html_file.read().replace("\n", "  ")
        for entry in parse_entries_from_html(html):
            assert entry == {
                'name': 'Cecil (2019)',
                'image_url': 'https://img.yts.lt/assets/images/movies/cecil_2019/medium-cover.jpg',
                'rating': '6.7 / 10',
                'categories': 'Comedy, Family',
            }
            break



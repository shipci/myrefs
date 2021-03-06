import time
from nose.tools import eq_
from utils import json_encode, get_unread_entries


class TestJsonEncoder(object):
    def test_encode_time_struct(self):
        data = {'title': 'title', 'publish_date': time.struct_time((2014, 3, 7, 10, 44, 30, 4, 66, 0))}
        actual = json_encode(data)
        eq_('{"publish_date": "2014-03-07T10:44:30", "title": "title"}', actual)


class TestFeedFiltering(object):
    def test_unread_entries__when_no_articles_is_read(self):
        eq_([], get_unread_entries([], []))
        eq_([{'link': 'article1'}], get_unread_entries([{'link': 'article1'}], []))

    def test_unread_entries(self):
        eq_([], get_unread_entries([{'link': 'article1'}], [{'url': 'article1'}]))
        eq_([{'link': 'article2'}], get_unread_entries([{'link': 'article1'}, {'link': 'article2'}], [{'url': 'article1'}]))
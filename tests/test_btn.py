from btn.btn import btn

import pytest
try:
    from .config import APIKEY
except ImportError:
    from os import getenv
    APIKEY = getenv('APIKEY')


class TestBtn:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = btn(APIKEY)

    def test_get_user(self):
        req = self.client.get_user()
        assert isinstance(req.get('UserID'), str)

    def test_get_changelog(self):
        req = self.client.get_changelog()
        assert req[0].get('Changes') == 'Test'

    def test_get_news(self):
        req = self.client.get_news()
        nextitem = req.get(next(iter(req)))
        assert len(req) == 5
        assert 'Title' in nextitem.keys()

    def test_get_news_id(self):
        id = 303
        req = self.client.get_news(id=id)
        nextitem = req.get(next(iter(req)))
        assert len(req) == 1
        assert nextitem.get('Time')

    def test_get_blog(self):
        req = self.client.get_blog()
        nextitem = req.get(next(iter(req)))
        assert len(req) == 5
        assert 'Body' in nextitem.keys()

    def test_get_blog_id(self):
        id = 132
        req = self.client.get_blog(id=id)
        nextitem = req.get(next(iter(req)))
        assert len(req) == 1
        assert 'Body' in nextitem.keys()

    def test_get_tvnews(self):
        req = self.client.get_tvnews()
        nextitem = req.get(next(iter(req)))
        assert len(req) == 5
        assert 'Title' in nextitem.keys()

    def test_get_tvnews_id(self):
        id = 1892
        req = self.client.get_tvnews(id=id)
        nextitem = req.get(next(iter(req)))
        assert len(req) == 1
        assert 'Body' in nextitem.keys()

    def test_get_inbox(self):
        req = self.client.get_inbox()
        assert isinstance(req.get('MaxPages'), int)
        assert 'results' in req

    def test_get_schedule(self):
        req = self.client.get_schedule()
        assert isinstance(req, list)

    def test_get_newseries(self):
        req = self.client.get_newseries()
        assert 'series' in req

    def test_filter_match(self):
        data = {'category': 'Season'}
        req = self.client.filter_match(data)
        assert req

    def test_filter_match_attrib(self):
        data = {'fake': 'Data'}
        with pytest.raises(AttributeError):
            self.client.filter_match(data)

    def test_filter_match_value(self):
        data = {'container': 'joe'}
        with pytest.raises(ValueError):
            self.client.filter_match(data)

    def test_search_handler_string(self):
        string = '%simpsons%'
        assert self.client.search_handler(string) == string

    def test_search_handler(self):
        data = {'category': 'Season', 'source': 'HDTV'}
        assert self.client.search_handler(data) == data

    def test_get_torrents(self):
        data = {'series': '%simpsons%', 'source': 'HDTV'}
        req = self.client.get_torrents(data).get('torrents')
        nextitem = req.get(next(iter(req)))
        assert len(req) == 10
        assert 'Snatched' in nextitem

    def test_get_torrentsurl(self):
        torrent_id = 959414
        assert 'torrents.php?action=download' in self.client.get_torrentsurl(
            torrent_id)

    def test_get_forumsindex(self):
        assert 'TV' in self.client.get_forumsindex()

    def test_get_forumspage(self):
        forumid = 72
        assert 'Threads' in self.client.get_forumspage(forumid)

    def test_get_torrentsbyid(self):
        torrents = 550105
        assert 'SeriesBanner' in self.client.get_torrentsbyid(torrents)

    def test_get_usersubscription(self):
        assert isinstance(self.client.get_usersubscription(), list)

    def test_get_usersnatchlist(self):
        assert len(self.client.get_usersnatchlist().get('torrents')) == 10

    def test_get_userstats(self):
        req = self.client.get_userstats()
        assert 'Moderator' in req.get('results').keys()

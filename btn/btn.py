from jsonrpc_requests import Server
from jsonrpc_requests.jsonrpc import ProtocolError
from .constants import BASEURI
from .filters import filters


class btn():
    """
    Initializes a client to broadcasthe.net
    """
    def __init__(self, apikey):
        self.server = Server(BASEURI)
        self.apikey = apikey

    def get_user(self):
        """
        Gets the authenticated users information
        :returns: dictionary
        """
        try:
            return self.server.userInfo(self.apikey)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_changelog(self):
        """
        Gets the changelog for the api interface
        """
        try:
            return self.server.getChangelog(self.apikey)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_news(self, id=None):
        """
        Get news information
        """
        try:
            if id:
                return self.server.getNewsById(self.apikey, id)

            return self.server.getNews(self.apikey)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_blog(self, id=None):
        """
        Get blog items
        """
        try:
            if id:
                return self.server.getBlogById(self.apikey, id)

            return self.server.getBlog(self.apikey)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_tvnews(self, id=None):
        """
        Get last tvnews items
        """
        try:
            if id:
                return self.server.getTVNewsById(self.apikey, id)

            return self.server.getTVNews(self.apikey)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_inbox(self, page=1, id=None):
        """
        Get recent inbox messages
        """
        try:
            if id:
                return self.server.getInboxConversation(self.apikey, id)

            return self.server.getInbox(self.apikey, page)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def send_inbox(self, id, body=None):
        """
        Send a message
        """
        try:
            return self.server.sendInboxConversation(self.apikey, id, body)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_schedule(self, sort='today'):
        """
        get the television schedule
        """
        try:
            return self.server.getSchedule(self.apikey, sort)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_newseries(self):
        """
        get the latest new series
        """
        try:
            return self.server.getNewSeries(self.apikey)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def filter_match(self, search):
        '''
        Ensure that a filter and query item is valid
        :search: dictionary of key/value to search for
        :return: true
        '''
        freeform_search = [
            'id', 'series', 'name', 'search', 'hash', 'tvdb', 'tvrage', 'time',
            'age'
        ]
        key = list(search.keys())[0].lower()
        value = search.get(key)

        if key in freeform_search:
            return True

        if not hasattr(filters, key):
            raise AttributeError(
                "{} not found in available search terms".format(key))

        if value in getattr(filters, key)(''):
            return True

        raise ValueError("{} is not a valid search item for {}".format(
            value, key))

    def search_handler(self, search):
        '''
        Handles the logic required for search
        '''

        if isinstance(search, str):
            return search
        else:
            for dictobj in search.items():
                self.filter_match(dict([dictobj]))

        return search

    def get_torrents(self, search, results=10, offset=0):
        '''
        Get a list of torrents
        :search: Search string or array, accepted id, series, category,
        episode, group name, codec, container
        :results: total number of results to return
        :offset: offset
        :return: array
        '''
        self.search_handler(search)
        try:
            return self.server.getTorrents(self.apikey, search, results,
                                           offset)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_torrentsurl(self, torrentid):
        '''
        get a url for a torrent download
        :torrentid: int number of torrent to get
        :return: string
        '''
        try:
            return self.server.getTorrentsUrl(self.apikey, torrentid)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_forumsindex(self, lastpost=1):
        '''
        get the list of forums
        :lastpost: get last post ordering
        :return: array
        '''
        try:
            return self.server.getForumsIndex(self.apikey, lastpost)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_forumspage(self, forumid, pageid=1):
        '''
        get a forums threads
        :forumid: id of the forum to get
        :pageid: what page from the forum you want
        :return: array
        '''
        try:
            return self.server.getForumsPage(self.apikey, forumid, pageid)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_torrentsbyid(self, ids):
        '''
        get a set of torrents by id
        :ids: int/list of torrent ids
        :return: list
        '''
        try:
            return self.server.getTorrentById(self.apikey, ids)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_usersubscription(self):
        '''
        get the users subscriptions
        :returns: list of subscriptions
        '''
        try:
            return self.server.getUserSubscriptions(self.apikey)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_usersnatchlist(self, results=10, offset=0):
        '''
        get the users snatched torrents
        :results: number of results to return
        :offset: id to start with
        :return: list of torrents grabbed
        '''
        try:
            return self.server.getUserSnatchlist(self.apikey, results, offset)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_userstats(self):
        '''
        get stats for users
        '''
        try:
            return self.server.getUserStats(self.apikey)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

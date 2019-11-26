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

    def call_api(self, endpoint, *args, **kwargs):
        '''
        Abstract the api out to remove duplication in individual functions
        '''
        try:
            return getattr(self.server, endpoint)(self.apikey, *args, **kwargs)
        except ProtocolError:
            raise ProtocolError("Exceeded the 150 calls per hour limit")

    def get_user(self):
        """
        Gets the authenticated users information
        :returns: dictionary
        """

        return self.call_api('userinfo')

    def get_changelog(self):
        """
        Gets the changelog for the api interface
        """

        return self.call_api('getChangelog')

    def get_news(self, id=None):
        """
        Get news information
        """

        if id:
            return self.call_api('getNewsById', id)

        return self.call_api('getNews')

    def get_blog(self, id=None):
        """
        Get blog items
        """

        if id:
            return self.call_api('getBlogById', id)

        return self.call_api('getBlog')

    def get_tvnews(self, id=None):
        """
        Get last tvnews items
        """

        if id:
            return self.call_api('getTVNewsById', id)

        return self.call_api('getTVNews')

    def get_inbox(self, page=1, id=None):
        """
        Get recent inbox messages
        """

        if id:
            return self.call_api('getInboxConversation', id)

        return self.call_api('getInbox', page)

    def send_inbox(self, id, body=None):
        """
        Send a message
        """

        return self.call_api('sendInboxConversation', id, body)

    def get_schedule(self, sort='today'):
        """
        get the television schedule
        """

        return self.call_api('getSchedule', sort)

    def get_newseries(self):
        """
        get the latest new series
        """

        return self.call_api('getNewSeries')

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

        return self.call_api('getTorrents', search, results, offset)

    def get_torrentsurl(self, torrentid):
        '''
        get a url for a torrent download
        :torrentid: int number of torrent to get
        :return: string
        '''

        return self.call_api('getTorrentsUrl', torrentid)

    def get_forumsindex(self, lastpost=1):
        '''
        get the list of forums
        :lastpost: get last post ordering
        :return: array
        '''

        return self.call_api('getForumsIndex', lastpost)

    def get_forumspage(self, forumid, pageid=1):
        '''
        get a forums threads
        :forumid: id of the forum to get
        :pageid: what page from the forum you want
        :return: array
        '''

        return self.call_api('getForumsPage', forumid, pageid)

    def get_torrentsbyid(self, ids):
        '''
        get a set of torrents by id
        :ids: int/list of torrent ids
        :return: list
        '''

        return self.call_api('getTorrentById', ids)

    def get_usersubscription(self):
        '''
        get the users subscriptions
        :returns: list of subscriptions
        '''

        return self.call_api('getUserSubscriptions')

    def get_usersnatchlist(self, results=10, offset=0):
        '''
        get the users snatched torrents
        :results: number of results to return
        :offset: id to start with
        :return: list of torrents grabbed
        '''

        return self.call_api('getUserSnatchlist', results, offset)

    def get_userstats(self):
        '''
        get stats for users
        '''

        return self.call_api('getUserStats')

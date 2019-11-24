class filters():
    def category(self):
        '''
        Allowed categories for torrents search
        '''

        return ['Season', 'Episode']

    def codec(self):
        '''
        Allowed codecs in torrents search
        '''

        return [
            'XViD', 'x264', 'MPEG2', 'DiVX', 'DVDR', 'VC-1', 'h.264', 'WMV',
            'BD', 'x264-Hi10P'
        ]

    def container(self):
        '''
        Allowed container formats in torrent search
        '''

        return [
            'AVI', 'MKV', 'VOB', 'MPEG', 'MP4', 'ISO', 'WMV', 'TS', 'M4V',
            'M2TS'
        ]

    def source(self):
        '''
        Allowed source in torrents search
        '''

        return [
            'HDTV', 'PDTV', 'DSR', 'DVDRip', 'TVRip', 'VHSRip', 'Bluray',
            'BDRip', 'BRRip', 'DVD5', 'DVD9', 'HDDVD', 'WEB', 'BD5', 'BD9',
            'BD25', 'BD50', 'Mixed'
        ]

    def resolution(self):
        '''
        Allowed resolution in torrents search
        '''

        return ['Portable Device', 'SD', '720p', '1080i', '1080p']

    def origin(self):
        '''
        Allowed origin for torrent searches
        '''

        return ['Scene', 'P2P', 'User']

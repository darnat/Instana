# CONSTANT
ROUTES = {
    'follow': 'friendships/create/{id}/',
    'unfollow': 'friendships/destroy/{id}/',
    'login': 'accounts/login/',
    'logout': 'accounts/logout/',
    'comment': 'media/{id}/comment/',
    'like': 'media/{id}/like/',
    'unlike': 'media/{id}/unlike/',
    'userInfo': 'users/{id}/info/',
    'userFeed': 'feed/user/{id}/?{maxID}rank_token={rankToken}',
    'timelineFeed': ('feed/timeline/?{maxID}'
                     'rank_token={rankToken}&ranked_content=true'),
    'tagFeed': ('feed/tag/{tag}/?{maxID}'
                'rank_token={rankToken}&ranked_content=false'),
    'recentTags': 'tags/{tag}/media/recent?rank_token={rankToken}',
    'locationFeed': ('feed/location/{id}/?{maxID}'
                     'rank_token={rankToken}&ranked_content=false'),
    'hashtagsSearch': 'tags/search/?count=50&q={query}&rank_token={rankToken}',
    'locationsSearch': ('fbsearch/places/?count=50&query={query}'
                        '&rank_token={rankToken}'),
    'mediaInfo': 'media/{id}/info/',
    'mediaLikes': 'media/{id}/likers/',
    'mediaComments': 'media/{id}/comments/{maxID}',
    'qeSync': 'qe/sync/',
    'inbox': 'direct_v2/inbox/{cursor}'
}

PRIVATE_KEY = {
    'SIG_KEY': ('299a77ffe98a252a20e1fb6bc87df721'
                'b90fe70c4cb327391b2dacaffd187f99'),
    'SIG_VERSION': '4',
    'APP_VERSION': '10.21.0',
}

TLD = 'instagram.com'
HOSTNAME = 'i.instagram.com'
WEB_HOSTNAME = 'www.instagram.com'
HOST = 'https://{}/'.format(HOSTNAME)
WEBHOST = 'https://{}/'.format(WEB_HOSTNAME)
API_ENDPOINT = '{}api/v1/'.format(HOST)

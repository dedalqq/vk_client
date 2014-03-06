import urllib2
import json
import urllib


class vk_api:

    token = None
    app_id = 4089597

    API_URL = 'https://api.vk.com/method'

    permission = [
        'messages',
        'audio',
        'offline',
        'status',
        'docs',
        'notes',
        'friends'
    ]

    _instance = None

    def __init__(self, token=None):
        if token is not None:
            self.token = token

    def getUrl(self, method, param, api_url=None):
        if api_url is None:
            api_url = self.API_URL
        parameters = []
        for name, value in param.iteritems():
            parameters.append(name + '=' + urllib.unquote_plus(str(value)))
        return api_url + '/' + method + '?' + '&'.join(parameters)

    def execUrl(self, url):
        response = urllib2.urlopen(url)
        return json.loads(response.read())

    def getLoginUrl(self):
        scope = ','.join(self.permission)
        return self.getUrl(
            'authorize',
            {
                'client_id': self.app_id,
                'scope': scope,
                'redirect_uri': 'blank.html',
                'display': 'popup',
                'response_type': 'token'
            },
            'https://oauth.vk.com'
        )

    def getFriends(self):
        url = self.getUrl(
            'friends.get',
            {
                'access_token': self.token,
                'fields': 'uid,first_name,last_name,nickname,photo'
            }
        )
        friends = self.execUrl(url)
        return friends['response']

    def getUserInfo(self):
        url = self.getUrl(
            'users.get',
            {
                'access_token': self.token,
                'fields': 'photo'
            }
        )
        user_response = self.execUrl(url)
        return user_response['response']
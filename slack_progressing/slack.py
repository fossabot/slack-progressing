import requests


class Slack:
    _POST_URL = "https://slack.com/api/chat.postMessage"
    _UPDATE_URL = "https://slack.com/api/chat.update"

    icon = ":snake:"
    name = "Slack Progressing"

    def __init__(self, token, channel, as_user=False):
        self._token = token
        self._channel = channel
        self._as_user = as_user

        self._ts = None

    def post(self, text):
        payload = {
            "token": self._token,
            "channel": self._channel,
            "text": text,
            "as_user": self._as_user,
            "icon_emoji": self.icon,
            "username": self.name,
        }
        r = requests.post(url=self._POST_URL, data=payload).json()

        self._ts = r["message"]["ts"]

    def update(self, text):
        payload = {
            "token": self._token,
            "channel": self._channel,
            "text": text,
            "ts": self._ts,
            "as_user": self._as_user,
            "icon_emoji": self.icon,
            "username": self.name,
        }
        requests.post(url=self._UPDATE_URL, data=payload)

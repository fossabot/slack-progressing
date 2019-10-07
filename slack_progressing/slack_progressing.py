from .progress_bar import ProgressBar
from .slack import Slack

__all__ = ["SlackProgressing"]


class SlackProgressing:
    def __init__(self, token, channel, length=20):
        """Control iterations.

        Args:
            token (str): Slack access token
            channel (str): Slack channel ID
            length (int, optional): Bar length. Defaults to 20.
        """
        self._progress_bar = ProgressBar(length=length)
        self._slack = Slack(token=token, channel=channel)

    def __call__(self, iterable):
        return self.progress(iterable)

    def progress(self, iterable):
        """Control iterations.

        Args:
            iterable (object): Iterable object such as list, tuple, or range
        """
        self._progress_bar.num_iters = len(iterable)

        for idx, obj in enumerate(iterable):
            yield obj
            self._progress_bar.done()

            if idx == 0:
                self._slack.post(self._progress_bar)
            else:
                self._slack.update(self._progress_bar)

    def set_params(self, params):
        """Set additional parameters to progress bar.

        Args:
            params (dict): Additional parameters
        """
        self._progress_bar.params = params

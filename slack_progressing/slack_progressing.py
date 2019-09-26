from .progress_bar import ProgressBar
from .slack import Slack

__all__ = ["SlackProgressing"]


class SlackProgressing:
    def __init__(self, token, channel, length=20):
        self._progress_bar = ProgressBar(length=length)
        self._slack = Slack(token=token, channel=channel)

    def set_params(self, params):
        self._progress_bar.params = params

    def progress(self, iterable):
        self._progress_bar.num_iters = len(iterable)

        for idx, obj in enumerate(iterable):
            yield obj
            self._progress_bar.done()

            if idx == 0:
                self._slack.post(self._progress_bar)
            else:
                self._slack.update(self._progress_bar)

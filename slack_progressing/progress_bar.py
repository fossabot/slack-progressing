class ProgressBar:
    bar_char = "■"
    empty_char = "□"
    delimiter = "\t"

    def __init__(self, length: int):
        """Progress bat controller.

        Args:
            length (int): Progress bar length
        """
        self._length = length

        self._num_iters = None
        self._current_iter = 0
        self._params = {}

        self._bar_text = ""

    def __str__(self):
        return self._bar_text

    def done(self):
        if self._num_iters is None:
            raise ProgressBarError(
                "Set number of iterations before starting iterations."
            )

        self._current_iter += 1

        progress_rate = self._current_iter / self._num_iters
        bar_length = round(self._length * progress_rate)
        empty_length = self._length - bar_length

        self._bar_text = (
            self.bar_char * bar_length
            + self.empty_char * empty_length
            + self.delimiter
            + "{:>3d}%".format(round(progress_rate * 100))
            + self.delimiter
            + "[{:>3d}/{:>3d}]".format(self._current_iter, self._num_iters)
            + self.delimiter
            + self.formatter(self._params)
        )

    @property
    def num_iters(self):
        return self._num_iters

    @num_iters.setter
    def num_iters(self, num_iters):
        self._num_iters = num_iters

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        self._params = params

    def formatter(self, d: dict):
        string = ""
        for k, v in d.items():
            if string:
                string += self.delimiter
            string += "{}: {}".format(k, v)
        return string


class ProgressBarError(Exception):
    pass

# Slack Progressing

[![](https://img.shields.io/travis/skmatz/slack-progressing)](https://travis-ci.org/skmatz/slack-progressing)

## Overview

The **Slack Progressing** helps you monitor your deep learning activity with Slack.

![demo](https://i.imgur.com/iPM0FxP.gif)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fskmatz%2Fslack-progressing.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fskmatz%2Fslack-progressing?ref=badge_shield)

## Get Started

```bash
pip install slack-progressing
```

## Usage

```python
from os import environ
from time import sleep

from slack_progressing import SlackProgressing


def main():
    sp = SlackProgressing(
        token=environ.get("TOKEN"), channel=environ.get("CHANNEL")
    )

    acc = 0.0
    loss = 10.0

    for _epoch in sp(range(10)):
        acc += 1.0
        loss -= 1.0
        d = {"acc": acc, "loss": loss}
        sp.set_params(d)

        sleep(1)


if __name__ == "__main__":
    main()
```

## Development

```bash
git clone https://github.com/skmatz/slack-progressing.git
cd slack-progressing
poetry install
```


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fskmatz%2Fslack-progressing.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fskmatz%2Fslack-progressing?ref=badge_large)
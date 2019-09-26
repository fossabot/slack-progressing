# Slack Progressing

## Overview

The **Slack Progressing** helps you monitor your deep learning activity with Slack.

![demo](https://i.imgur.com/iPM0FxP.gif)

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

    for _epoch in sp.progress(range(10)):
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

from os import environ
from time import sleep

from tqdm import tqdm

from slack_progressing import SlackProgressing


def main():
    sp = SlackProgressing(
        token=environ.get("TOKEN"), channel=environ.get("CHANNEL")
    )

    acc = 0.0
    loss = 10.0

    for _epoch in sp(tqdm((range(10)))):
        acc += 1.0
        loss -= 1.0
        d = {"acc": acc, "loss": loss}
        sp.set_params(d)

        sleep(1)


if __name__ == "__main__":
    main()

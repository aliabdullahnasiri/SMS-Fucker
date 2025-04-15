import re
import threading
from typing import List

import click

from utils.core.roshan import Roshan
from utils.logger import logger


@click.command()
@click.option(
    "-MSISDN",
    type=str,
    required=True,
    help="Target MSISDN (phone number) to send messages to.",
)
@click.option(
    "-THREADS-COUNT",
    type=click.IntRange(5, 30),
    default=5,
    help="Number of threads to use (default: 5).",
)
def main(msisdn: str, threads_count: int) -> None:
    threads: List[threading.Thread] = []

    classes: List = [Roshan]

    for cls in classes:
        if re.match(cls.RE_MSISDN_PATTERN, msisdn):
            obj = cls(msisdn)

            for count in range(threads_count):
                threads.append(threading.Thread(target=obj.fuck))
                logger.info(f"Thread {count+1!r:>02} successfully started.")

            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()

            break


if __name__ == "__main__":
    main()

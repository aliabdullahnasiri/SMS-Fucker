from typing import Self

import requests

from utils.logger import logger


class Roshan(object):
    HOST: str = "api.roshan.af"

    def __init__(self: Self, msisdn: str) -> None:
        self.msisdn: str = msisdn

    def register(self: Self) -> bool:
        response: requests.Response = requests.post(
            f"https://{self.HOST}/api/register",
            headers={
                "Content-Type": "application/json",
            },
        )

        if response.ok:
            logger.success(f"Phone number {self.msisdn!r} successfully registered.")

        else:
            logger.error("An error occurred during registering the phone number! ")

            return False

        return True

    def send(self: Self) -> bool:
        return self.register()


def main() -> None:
    pass


if __name__ == "__main__":
    main()

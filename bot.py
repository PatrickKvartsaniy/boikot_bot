import os

import httpx
from httpx import AsyncClient

from schemas import ResponseToMessage

APP_HOST = os.environ["APP_HOST"]


async def request(url: str, payload: dict, headers: dict, debug: bool = False):
    async with AsyncClient() as client:
        req = await client.post(url, json=payload, headers=headers)
        if debug:
            print(req.json())
        return req


class TelegramBot:
    TELEGRAM_BASE_URL = "https://api.telegram.org/bot"
    TELEGRAM_SEND_MESSAGE_URL = "/sendMessage"
    TELEGRAM_SET_WEBHOOK_URL = "/setWebhook"
    token = "5137407807:AAGV01AHckbr_vM-okf2MKMyx2CqTfUu2LI"

    def set_webhook(self) -> bool:
        payload = {"url": f"{APP_HOST}/webhook/"}
        url = self.TELEGRAM_BASE_URL + self.token + self.TELEGRAM_SET_WEBHOOK_URL
        req = httpx.post(url=url, data=payload, headers={})
        return req.status_code == 200

    async def send_message(self, telegram_id: int, message: str) -> bool:
        message = ResponseToMessage(
            **{
                "text": message,
                "chat_id": telegram_id,
            }
        )
        url = self.TELEGRAM_BASE_URL + self.token + self.TELEGRAM_SEND_MESSAGE_URL
        req = await request(url=url, payload=message.dict(), headers={})
        return req.status_code == 200

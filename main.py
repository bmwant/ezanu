import requests

from urllib.parse import urljoin


TOKEN = '507912965:AAGyKwGcaIDo5IDVx7gQ5sm2btfOlJWNkPg'


class TelegramBot(object):
    BASE_URI = 'https://api.telegram.org/bot{0.token}/'
    FILE_URI = 'https://api.telegram.org/file/bot{0.token}/'
    USERNAME = 'ezanu'

    def __init__(self, token):
        self.update_offset = 0
        self.username = "ZamzaBot"
        self.token = token

    def _get_uri(self, endpoint):
        return urljoin(self.BASE_URI.format(self), endpoint)

    def test(self):
        resp = requests.get(self._get_uri('messages.getDialogs'))
        print(resp.json())


def main():
    bot = TelegramBot(token=TOKEN)
    bot.test()


if __name__ == '__main__':
    main()

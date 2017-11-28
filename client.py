from telethon import TelegramClient
from telethon.tl.types import PeerUser

import config


def list_dialogs(client):
    dialogs = client.get_dialogs()[0]
    for dialog in dialogs:
        if isinstance(dialog.peer, PeerUser):
            user_id = dialog.peer.user_id
            user = client.get_entity(user_id)
            print('Dialog with user', user_id, user.first_name, user.last_name)
        else:
            print(dialog.to_dict())


def print_messages():
    pass


def main():
    client = TelegramClient('session_name', config.API_ID, config.API_HASH)
    client.connect()

    # me = client.sign_in(code='27105')
    me = client.get_me()
    target_user = client.get_entity(config.TARGET_USER_ID)
    total_messages, messages, _ = client.get_message_history(config.TARGET_USER_ID)
    for message in messages:
        print(message.message)
        import pdb; pdb.set_trace()
    # print(mh)


if __name__ == '__main__':
    main()

import keyring

from config import config


def get_credentials(uid):
    username = get_username(uid)
    password = get_password(username, uid)

    return username, password


def get_username(uid):
    if uid in config.machines and 'Username' in config.machines[uid]:
        return config.machines[uid]['Username']

    return config.credentials.get('Username')


def get_password(username, uid):
    if uid in config.machines:
        if 'Password' in config.machines[uid]:
            return config.machines[uid]['Password']
        elif config.machines[uid].get('UseKeyring', False):
            return keyring.get_password(uid, username)

    if 'UseKeyring' in config.credentials:
        return keyring.get_password('vmupdate', username)

    return config.credentials.get('Password')

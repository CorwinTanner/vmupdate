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
        elif config.machines[uid].get('Use Keyring', False):
            return keyring.get_password(uid, username)

    if 'Use Keyring' in config.credentials:
        return keyring.get_password('vmupdate', username)

    return config.credentials.get('Password')

def get_run_as_elevated(uid):
    if uid in config.machines and 'Run As Elevated' in config.machines[uid]:
        return config.machines[uid]['Run As Elevated']

    return config.credentials.get('Run As Elevated')

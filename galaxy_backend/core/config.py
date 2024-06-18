import os


class env:
    game_url: str = 'https://gmankab.github.io/galaxy_frontend'
    db_url: str = 'sqlite://:memory:'
    tg_token: str = ''
    tests: str = ''
    channel_username: str = '@foo'
    max_autoclicks: int = 100
    clicks_interval: int = 1
    #bonus_coins_count: int = 500

def set_env():
    for key, value_type in env.__annotations__.items():
        value = os.getenv(key)
        if value:
            assert isinstance(value, value_type)
            setattr(env, key, value)


set_env()


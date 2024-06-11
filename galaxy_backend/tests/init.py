from models.db import User
import api.app

async def create_user():
    await api.app.init_db()
    await User.get_or_create(
        tg_id=0,
        coins=0,
        autoclicks_remain=0,
    )
    return 'create user'


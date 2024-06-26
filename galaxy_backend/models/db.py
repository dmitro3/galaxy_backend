from tortoise.models import Model
from tortoise import fields


class User(Model):
    tg_id = fields.IntField(primary_key=True)
    coins = fields.IntField(default=0)
    autoclicks_remain = fields.IntField(default=0)
    clan = fields.ForeignKeyField('models.Clan', related_name='members', null=True)


class Clan(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=30)


class ClanOwner(Model):
    clan = fields.OneToOneField('models.Clan', related_name='owner_clan')
    user = fields.OneToOneField('models.User', related_name='clan_owner')


class Sector(Model):
    id = fields.IntField(pk=True)
    available = fields.BooleanField()


class Planet(Model):
    id = fields.IntField(pk=True)
    sector = fields.ForeignKeyField('models.Sector', related_name='planets')
    total_resources = fields.IntField()
    mined_resources = fields.IntField()
    available = fields.BooleanField()


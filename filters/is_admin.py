import os
import json

import typing

from aiogram.filters import Filter

class IsAdmin(Filter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj):
        if self.is_admin is None:
            return False
        admins = json.loads(os.environ.get("ADMINS"))
        return (obj.from_user.id in admins) == self.is_admin
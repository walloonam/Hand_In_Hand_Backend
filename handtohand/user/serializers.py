from user.models import User


def serializeUser(entity: User) -> dict:
    return {
        "user": entity.email,
        "password": entity.password,
        "name": entity.name,
        "nickname": entity.nickname,
        "date_of_birth": entity.date_of_birth,
        "address": entity.address
    }
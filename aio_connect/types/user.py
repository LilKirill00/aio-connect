from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from .base import ConnectObject

from ..types import UUID


class User(ConnectObject):
    """
    Название объекта: User
    Описание объекта: Пользователь

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/1289355329/User
    """

    user_id: UUID
    """ID пользователя"""
    name: str
    """Имя пользователя"""
    surname: str
    """Фамилия пользователя"""
    patronymic: str
    """Отчество пользователя"""
    avatar_url: Optional[str] = None
    """Ссылка на аватар"""
    avatar_small_url: Optional[str] = None
    """Ссылка на превью аватара"""
    email: str
    """Email пользователя"""
    post: str
    """Должность пользователя"""
    phone: str
    """Телефон пользователя"""

    if TYPE_CHECKING:
        # DO NOT EDIT MANUALLY!!!
        # This section was auto-generated via `butcher`

        def __init__(
            __pydantic__self__,
            *,
            user_id: UUID,
            name: str,
            surname: str,
            patronymic: str,
            avatar_url: Optional[str] = None,
            avatar_small_url: Optional[str] = None,
            email: str,
            post: str,
            phone: str,
            **__pydantic_kwargs: Any,
        ) -> None:
            # DO NOT EDIT MANUALLY!!!
            # This method was auto-generated via `butcher`
            # Is needed only for type checking and IDE support without any additional plugins

            super().__init__(
                user_id=user_id,
                name=name,
                surname=surname,
                patronymic=patronymic,
                avatar_url=avatar_url,
                avatar_small_url=avatar_small_url,
                email=email,
                post=post,
                phone=phone,
                **__pydantic_kwargs,
            )


class Users(User):
    """
    Название объекта: Users
    Описание объекта: Пользователи

    Source: https://1c-connect.atlassian.net/wiki/spaces/PUBLIC/pages/2068938769/Users

    Данные: Такие же как у User
    """

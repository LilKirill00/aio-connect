import uuid
from typing import TypeVar, Union
from pydantic import UUID3, UUID4, UUID5

UUID = TypeVar("UUID", bound=Union[UUID5, UUID4, UUID3, str])


def is_valid_uuid(uuid_to_test: UUID) -> UUID:
    if uuid_to_test:
        try:
            if uuid.UUID(str(uuid_to_test)).version:
                return str(uuid_to_test)
        except ValueError as e:
            raise ValueError(e, uuid_to_test)
        return -1

from dataclasses import dataclass

from logic.events.exceptions.base import LogicException


@dataclass(eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicException):
    title: str
    @property
    def message(self):
        return f"That title '{self.title}' is already taken."
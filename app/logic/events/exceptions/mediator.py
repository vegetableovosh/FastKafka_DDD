from dataclasses import dataclass

from logic.events.exceptions.base import LogicException


@dataclass(eq=False)
class EventHandlersNotRegisteredExcepted(LogicException):
    event_type: type
    @property
    def message(self):
        return f'Не удалось найти обработчики для события: {self.event_type}'


@dataclass(eq=False)
class CommandHandlersNotRegisteredExcepted(LogicException):
    command_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчики для события: {self.command_type}'
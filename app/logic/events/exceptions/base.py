from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=True)
class LogicException(ApplicationException):
    @property
    def message(self):
        return 'В обработке запроса возникла ошибка'

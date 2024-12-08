from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar
from domain.events.base import BaseEvent

ET = TypeVar(name='ET', bound=BaseEvent)
ER = TypeVar(name='ER', bound=BaseEvent)


@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    def handle(self, event: ET) -> ER:
        ...
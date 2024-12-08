from dataclasses import dataclass

from pip._internal.exceptions import CommandError

from domain.entities.messages import Chat
from domain.values.messages import Title
from infra.repositories.messages import BaseChatRepository
from logic.commands.base import BaseCommand, CommandHandler
from logic.events.exceptions.messages import ChatWithThatTitleAlreadyExistsException


@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
    title: str

@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand, Chat]):
    chat_repository: BaseChatRepository
    async def handle(self, command: CreateChatCommand) -> Chat:
        if await self.chat_repository.check_chat_exists_by_title(command.title):
            raise ChatWithThatTitleAlreadyExistsException(command.title)

        title = Title(value=command.title)
        # TODO: считать ивенты

        new_chat = Chat.create_chat(title=title)

        await self.chat_repository.add_chat(new_chat)

        return new_chat




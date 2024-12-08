import pytest

from domain.entities.messages import Chat
from infra.repositories.messages import BaseChatRepository
from logic import Mediator
from logic.commands.messages import CreateChatCommand


@pytest.mark.asyncio
async def test_create_chat_command_success(
        chat_repository: BaseChatRepository,
        mediator: Mediator,
):
    # TODO: Закинуть фейкерочик для генеарции рандомных текстов
    chat: Chat = (await mediator.handler_command(CreateChatCommand(title='gigaTitle')))[0]

    assert chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type())

from infra.repositories.messages import MemoryChatRepository, BaseChatRepository
from logic.commands.messages import CreateChatCommandHandler, CreateChatCommand
from logic.mediator import Mediator


def init_mediator(
        mediator: Mediator,
        chat_repository: BaseChatRepository,
):
    mediator.register_command(
        CreateChatCommand,
        [CreateChatCommandHandler(chat_repository=chat_repository)],
    )
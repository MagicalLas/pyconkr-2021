import abc
import dataclasses
from typing import Optional, List

from src.domain.backlog import BackLog
from src.domain.card import Card
from src.domain.line import Line


@dataclasses.dataclass
class BoardID(object):
    board_id: int


class KanbanBoard(object):
    def __init__(
        self,
        board_id: BoardID,
        name: str,
        todo_cards: Line,
        wip_cards: Line,
        done_cards: Line,
        backlog: BackLog,
    ):
        self._id = board_id
        self._name = name
        self._todo_cards = todo_cards
        self._wip_cards = wip_cards
        self._done_cards = done_cards
        self._backlog = backlog


class KanbanBoardRepository(object):
    @abc.abstractmethod
    def get_all(self) -> List[KanbanBoard]:
        pass

    @abc.abstractmethod
    def get_by_id(self, board_id: BoardID) -> Optional[KanbanBoard]:
        pass

    @abc.abstractmethod
    def save(self, board: KanbanBoard) -> KanbanBoard:
        pass

    @abc.abstractmethod
    def delete(self, board: KanbanBoard) -> None:
        pass


class NotificationService(object):
    @abc.abstractmethod
    def card_done_alert(self, card: Card) -> None:
        pass

    @abc.abstractmethod
    def wip_limit_alert(self, board: KanbanBoard) -> None:
        pass

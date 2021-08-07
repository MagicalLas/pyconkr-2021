import dataclasses
from enum import Enum, auto

from src.domain.backlog import BackLog
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


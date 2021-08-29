import abc
from dataclasses import dataclass
from typing import Optional


@dataclass
class Board(object):
    board_id: int
    name: str


class BoardRepository(object):
    @abc.abstractmethod
    async def save(self, board: Board) -> Board:
        pass

    @abc.abstractmethod
    async def find_by_id(self, board_id: int) -> Optional[Board]:
        pass


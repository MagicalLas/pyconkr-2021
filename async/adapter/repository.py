from typing import Optional

from domain.board import BoardRepository, Board


class MySQLBoardRepository(BoardRepository):
    async def save(self, board: Board) -> Board:
        pass

    async def find_by_id(self, board_id: int) -> Optional[Board]:
        pass
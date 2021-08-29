import asyncio

from domain.board import Board, BoardRepository

class UseCase:
    async def create_board(
        self,
        repository: BoardRepository,
        name: str
    ) -> Board:
        board = Board(0, name)
        board = await asyncio.wait_for(
            repository.save(board), 1
        )
        return board

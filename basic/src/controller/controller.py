from __future__ import annotations

from fastapi import FastAPI
from pydantic.main import BaseModel

from src.adapter.django_kanban_repository import DjangoKanbanBoardRepository
from src.application.usecases import UseCases
from src.domain.kanbanboard import KanbanBoard

app = FastAPI()

use_cases = UseCases(repository=DjangoKanbanBoardRepository())


class Board(BaseModel):
    @staticmethod
    def from_model(board: KanbanBoard) -> Board:
        return Board()  # Skip implementation.


@app.get("boards/")
def get_boards():
    boards = use_cases.get_all_boards()
    return [Board.from_model(board) for board in boards]

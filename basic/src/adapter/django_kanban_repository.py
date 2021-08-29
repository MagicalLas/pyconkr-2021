from typing import Optional, List

from django.db import models

from src.domain.kanbanboard import KanbanBoardRepository, KanbanBoard, BoardID


class DjangoKanbanBoardModel(models.Model):
    name = models.CharField(max_length=30)


class DjangoCardsModel(models.Model):
    title = models.CharField(max_length=30)
    kanban_id = models.ForeignKey(
        DjangoKanbanBoardModel,
        db_constraint=False,
        on_delete=models.CASCADE,
    )


class DjangoKanbanBoardRepository(KanbanBoardRepository):
    def get_all(self) -> List[KanbanBoard]:
        pass

    def get_by_id(self, board_id: BoardID) -> Optional[KanbanBoard]:
        pass

    def save(self, board: KanbanBoard) -> KanbanBoard:
        pass

    def delete(self, board: KanbanBoard) -> None:
        pass

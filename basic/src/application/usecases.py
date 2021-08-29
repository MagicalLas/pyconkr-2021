from typing import List

from src.domain.kanbanboard import KanbanBoardRepository, KanbanBoard


class UseCases(object):
    def __init__(self, repository: KanbanBoardRepository):
        self._repo = repository

    def get_all_boards(self) -> List[KanbanBoard]:
        return self._repo.get_all()

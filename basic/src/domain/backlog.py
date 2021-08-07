from dataclasses import dataclass
from typing import List

from src.domain.kanbanboard import Card


@dataclass
class BackLog(object):
    cards: List[Card]

from __future__ import annotations

import datetime
from dataclasses import dataclass
from enum import Enum, auto

from pydantic import BaseModel

class CardStatus(Enum):
    TODO = auto()
    DONE = auto()
    WIP = auto()
    BACKLOG = auto()
    ARCHIVE = auto()


class UserID(BaseModel):
    user_id: str


@dataclass(frozen=True)
class CardID(object):
    card_id: int


@dataclass(frozen=True)
class Card(object):
    card_id: CardID
    title: str
    description: str
    assigned_user: UserID
    status: CardStatus
    end_date: datetime.date

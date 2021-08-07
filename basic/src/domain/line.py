from dataclasses import dataclass
from typing import Dict, Optional

from src.domain.card import CardID, Card


@dataclass
class Line(object):
    cards: Dict[CardID, Card]

    def find_card(self, card_id: CardID) -> Optional[Card]:
        return self.cards.get(card_id)

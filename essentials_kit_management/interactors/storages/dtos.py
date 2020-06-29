from typing import List
from dataclasses import dataclass
from datetime import datetime
from essentials_kit_management.constants.enums import StatusType

@dataclass
class FormDto:
    form_id: int
    form_name: str
    closed_date: datetime
    expected_date: datetime
    status: StatusType


@dataclass
class ItemsAndCostDto:
    form_id: int
    items_count: int
    pending_items: int
    estimated_cost: int
    cost_incurred: int


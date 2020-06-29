import enum

from ib_common.constants import BaseEnumClass


class StatusType(BaseEnumClass, enum.Enum):
    CLOSE = "CLOSE"
    LIVE = "LIVE"
    DONE = "DONE"

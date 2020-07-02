import re

from dataclasses import dataclass
from typing import Pattern

@dataclass
class UserDetailsDto:
    user_id: int
    username: str
    profile_pic: str
    name: str


@dataclass
class UserDto:

    user_id: int
    username: str
    email: str
    profile_pic: Pattern = re.compile("(https?)://([^/\r\n]+)(/[^\r\n]*)?")

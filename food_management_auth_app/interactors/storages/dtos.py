from dataclasses import dataclass


@dataclass
class UserDetailsDto:
    user_id: int
    username: str
    profile_pic: str
    name: str

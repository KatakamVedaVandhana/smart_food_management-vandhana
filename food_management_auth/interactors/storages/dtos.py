from dataclasses import dataclass


@dataclass
class UserDetailsDto:
    user_id: int
    username: str
    name: str
    profile_pic: str

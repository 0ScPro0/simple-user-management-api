# models/user.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    """
    Data class representing a User entity.
    
    This class is a pure data container following the Single Responsibility Principle.
    It contains only user attributes without any business logic or API-specific concerns.
    
    Attributes:
        id: Unique identifier for the user
        username: User's chosen display name
        password: User's authentication credential (in production, this should be hashed)
    """
    id: int
    username: str
    password: str
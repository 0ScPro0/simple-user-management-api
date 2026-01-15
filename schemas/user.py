# schemas/user.py
from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    """
    Pydantic schema for user data in API responses.
    
    This schema defines the structure of user data as it appears in API responses.
    It serves as a contract between the backend and API consumers.
    
    Note: In production, password should never be exposed in API responses.
    This example includes it for demonstration purposes only.
    
    Attributes:
        id: User's unique identifier
        username: User's display name
        password: User's password (exposed here for demonstration only)
    """
    id: int
    username: str
    password: str

    class Config:
        """
        Pydantic model configuration.
        
        from_attributes: Enables creation of model instances from ORM objects or dataclasses.
        This allows automatic conversion between User (dataclass) and UserResponse (Pydantic model).
        """
        from_attributes = True


class UserCreate(BaseModel):
    """
    Schema for user creation requests.
    
    This schema validates incoming data when creating new users.
    It can include different validation rules than the response schema.
    """
    username: str
    password: str


class UserUpdate(BaseModel):
    """
    Schema for user update requests.
    
    All fields are optional to allow partial updates.
    """
    username: Optional[str] = None
    password: Optional[str] = None
# repositories/user_repository.py
from typing import List, Optional
from models.user import User


class UserRepository:
    """
    Data access layer for User entities.
    
    This class encapsulates all database operations and follows the
    Repository pattern. It separates data access logic from business logic.
    
    In a real application, this would interact with a database instead of
    storing data in memory.
    """
    
    def __init__(self):
        """
        Initialize the repository with in-memory storage.
        
        In production, this would initialize database connections.
        """
        self._users = [
            User(1, "ScPro", "ga182#s!"),
            User(2, "Yoru", "yu1482xx"),
        ]
        self._next_id = 3
    
    def get_all(self) -> List[User]:
        """
        Retrieve all users from the repository.
        
        Returns:
            List[User]: All user entities in the repository
        """
        return self._users.copy()  # Return copy to prevent external modification
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """
        Find a user by their ID.
        
        Args:
            user_id: The ID of the user to find
            
        Returns:
            Optional[User]: The user if found, None otherwise
        """
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def create(self, username: str, password: str) -> User:
        """
        Create a new user in the repository.
        
        Args:
            username: The new user's username
            password: The new user's password
            
        Returns:
            User: The newly created user entity
        """
        new_user = User(self._next_id, username, password)
        self._users.append(new_user)
        self._next_id += 1
        return new_user
    
    def update(self, user_id: int, **kwargs) -> Optional[User]:
        """
        Update an existing user's attributes.
        
        Args:
            user_id: The ID of the user to update
            **kwargs: Attributes to update (username, password)
            
        Returns:
            Optional[User]: The updated user if found, None otherwise
        """
        user = self.get_by_id(user_id)
        if not user:
            return None
        
        for key, value in kwargs.items():
            if hasattr(user, key) and value is not None:
                setattr(user, key, value)
        
        return user
    
    def delete(self, user_id: int) -> bool:
        """
        Delete a user from the repository.
        
        Args:
            user_id: The ID of the user to delete
            
        Returns:
            bool: True if user was deleted, False if user was not found
        """
        user = self.get_by_id(user_id)
        if user:
            self._users.remove(user)
            self._next_id -= 1
            return True
        return False
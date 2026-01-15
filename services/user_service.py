# services/user_service.py
from typing import List, Optional
from models.user import User
from schemas.user import UserResponse, UserCreate, UserUpdate
from repositories.user_repository import UserRepository


class UserService:
    """
    Business logic layer for user operations.
    
    This service class contains all business rules and use cases related to users.
    It acts as an intermediary between the API layer (controllers) and the data layer (repository).
    
    Following the Single Responsibility Principle, this class focuses only on
    business logic, not on HTTP concerns or data persistence details.
    """
    
    def __init__(self, repository: UserRepository = None):
        """
        Initialize the user service with a repository.
        
        Args:
            repository: UserRepository instance. If None, creates a new one.
                        This allows dependency injection for testing.
        """
        self.repository = repository or UserRepository()
    
    def get_all_users(self) -> List[UserResponse]:
        """
        Retrieve all users as API response objects.
        
        This method applies any business rules (filtering, sorting, etc.)
        before converting entities to API response objects.
        
        Returns:
            List[UserResponse]: All users formatted for API response
        """
        users = self.repository.get_all()
        # Business logic could be applied here (e.g., filtering active users)
        return [UserResponse.model_validate(user) for user in users]
    
    def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        """
        Find a user by ID and return as API response object.
        
        Args:
            user_id: The ID of the user to find
            
        Returns:
            Optional[UserResponse]: User formatted for API response, or None if not found
        """
        user = self.repository.get_by_id(user_id)
        if user:
            return UserResponse.model_validate(user)
        return None
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        """
        Create a new user with validation and business rules.
        
        Args:
            user_data: Validated data for the new user
            
        Returns:
            UserResponse: The newly created user formatted for API response
            
        Raises:
            ValueError: If username already exists (example business rule)
        """
        # Example business rule: Check if username is unique
        existing_users = self.repository.get_all()
        if any(u.username == user_data.username for u in existing_users):
            raise ValueError(f"Username '{user_data.username}' already exists")
        
        # Additional business logic could be applied here
        # (e.g., password strength validation, name formatting)
        
        # Create the user in the repository
        new_user = self.repository.create(
            username=user_data.username,
            password=user_data.password  # In production, hash the password here
        )
        
        return UserResponse.model_validate(new_user)
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
        """
        Update an existing user with provided data.
        
        Args:
            user_id: The ID of the user to update
            user_data: Validated update data
            
        Returns:
            Optional[UserResponse]: Updated user formatted for API response, or None if not found
        """
        # Convert Pydantic model to dictionary, removing None values
        update_data = user_data.model_dump(exclude_none=True)
        
        updated_user = self.repository.update(user_id, **update_data)
        if updated_user:
            return UserResponse.model_validate(updated_user)
        return None
    
    def delete_user(self, user_id: int) -> bool:
        """
        Delete a user by ID.
        
        Args:
            user_id: The ID of the user to delete
            
        Returns:
            bool: True if user was deleted, False if not found
        """
        return self.repository.delete(user_id)
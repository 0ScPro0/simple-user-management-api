# api/endpoints/users.py
from typing import List
from fastapi import APIRouter, HTTPException, status
from schemas.user import UserResponse, UserCreate, UserUpdate
from services.user_service import UserService

# Create router with prefix and tags for OpenAPI documentation
router = APIRouter(prefix="/users", tags=["users"])
user_service = UserService()


@router.get("/", response_model=List[UserResponse])
async def get_users():
    """
    Retrieve all users.
    
    This endpoint returns a list of all registered users.
    Note: In production, consider adding pagination for large datasets.
    
    Returns:
        List[UserResponse]: All users in the system
    """
    return user_service.get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """
    Retrieve a specific user by ID.
    
    Args:
        user_id: The unique identifier of the user
        
    Returns:
        UserResponse: The requested user
        
    Raises:
        HTTPException 404: If user with specified ID is not found
    """
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    """
    Create a new user.
    
    Args:
        user_data: User creation data
        
    Returns:
        UserResponse: The newly created user
        
    Raises:
        HTTPException 400: If username already exists or data is invalid
    """
    try:
        return user_service.create_user(user_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserUpdate):
    """
    Update an existing user.
    
    Args:
        user_id: The ID of the user to update
        user_data: User update data (partial updates allowed)
        
    Returns:
        UserResponse: The updated user
        
    Raises:
        HTTPException 404: If user with specified ID is not found
    """
    updated_user = user_service.update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """
    Delete a user by ID.
    
    Args:
        user_id: The ID of the user to delete
        
    Raises:
        HTTPException 404: If user with specified ID is not found
    """
    if not user_service.delete_user(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
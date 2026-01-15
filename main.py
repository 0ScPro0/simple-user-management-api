# main.py
from fastapi import FastAPI
import uvicorn
from api.endpoints import users

# Initialize FastAPI application with metadata for OpenAPI documentation
app = FastAPI(
    title="Simple User Management API",
    description="A RESTful API for user management operations",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI documentation
    redoc_url="/redoc",  # Alternative ReDoc documentation
)

# Include all API routers
app.include_router(users.router)

# Root endpoint for health checks
@app.get("/")
async def root():
    """
    Root endpoint for health checks and API information.
    
    Returns:
        dict: API metadata and status
    """
    return {
        "message": "Simple User Management API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "operational"
    }


if __name__ == "__main__":
    """
    Application entry point for development server.
    
    In production, use a production ASGI server like:
    uvicorn main:app --host 0.0.0.0 --port 8000
    """
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Listen on all network interfaces
        port=8000,        # Default FastAPI port
        reload=True       # Enable auto-reload for development
    )
from pydantic import BaseModel, Field


class EmptyResponse(BaseModel):
    """Success"""
    __root__: None


class ErrorResponse(BaseModel):
    error: str = Field(description='Error message')

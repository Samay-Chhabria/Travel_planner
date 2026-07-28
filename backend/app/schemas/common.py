from pydantic import BaseModel, Field


class PaginationMeta(BaseModel):
    page: int = Field(default=1, ge=1, description="Current page number")
    limit: int = Field(default=10, ge=1, le=100, description="Results per page")
    total: int = Field(default=0, ge=0, description="Total number of results")

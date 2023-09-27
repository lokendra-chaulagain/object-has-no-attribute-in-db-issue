from typing import Optional
from pydantic import BaseModel
from models.Table import Table


class SaleIn(BaseModel):
    discount_amount: float
    is_draft: bool
    table: int


class SaleOut(BaseModel):
    id: int
    discount_amount: float
    is_draft: bool
    table: int


class SaleQueryParams(BaseModel):
    page: Optional[int] = 1
    limit: Optional[int] = 5
    table: Optional[int] = None

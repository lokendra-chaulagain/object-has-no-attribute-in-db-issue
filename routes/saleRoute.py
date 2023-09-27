from fastapi import APIRouter, Depends
from typing import List
from models.Sale import Sale
from schemas.saleSchema import SaleIn, SaleOut, SaleQueryParams
saleRouter = APIRouter()


@saleRouter.post("", response_model=SaleOut)
async def create(sale: SaleIn) -> SaleOut:
    # new_sale = await Sale.create(**sale.model_dump())
    # return new_sale

    new_sale = await Sale.create(discount_amount=sale.discount_amount, is_draft=sale.is_draft, table=sale.table)
    saved_sale=new_sale.save()
    return saved_sale


@saleRouter.get("", response_model=List[SaleOut])
async def get_all(query_params: SaleQueryParams = Depends()) -> List[SaleOut]:
    offset = (query_params.page - 1) * query_params.limit
    query = Sale.all()

    if query_params.table:
        query = query.filter(table__icontains=query_params.name)

    sales = await query.offset(offset).limit(query_params.limit)
    return list(sales)

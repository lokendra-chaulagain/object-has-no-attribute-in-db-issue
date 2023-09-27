from fastapi import APIRouter, Depends
from typing import List
from models.Table import Table
from schemas.tableSchema import TableIn, TableOut, TableQueryParams
tableRouter = APIRouter()


@tableRouter.post("", response_model=TableOut)
async def create(table: TableIn) -> TableOut:
     table = await Table.create(**table.model_dump())
     return table


@tableRouter.get("", response_model=List[TableOut])
async def get_all(query_params: TableQueryParams = Depends()) -> List[TableOut]:
    offset = (query_params.page - 1) * query_params.limit
    query = Table.all()

    if query_params.name:
        query = query.filter(name__icontains=query_params.name)

    tables = await query.offset(offset).limit(query_params.limit)
    return list(tables)

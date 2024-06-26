# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteAllProducts(BaseModel):
    delete_all_products: Optional[
        List[Optional["DeleteAllProductsDeleteAllProducts"]]
    ] = Field(alias="deleteAllProducts")


class DeleteAllProductsDeleteAllProducts(BaseModel):
    id: str
    state: EntityState


DeleteAllProducts.model_rebuild()

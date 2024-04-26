# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from .base_model import BaseModel


class QueryCategories(BaseModel):
    categories: Optional["QueryCategoriesCategories"]


class QueryCategoriesCategories(BaseModel):
    results: Optional[List[Optional["QueryCategoriesCategoriesResults"]]]


class QueryCategoriesCategoriesResults(BaseModel):
    id: str
    name: str


QueryCategories.model_rebuild()
QueryCategoriesCategories.model_rebuild()

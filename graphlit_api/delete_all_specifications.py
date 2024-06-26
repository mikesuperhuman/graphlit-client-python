# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteAllSpecifications(BaseModel):
    delete_all_specifications: Optional[
        List[Optional["DeleteAllSpecificationsDeleteAllSpecifications"]]
    ] = Field(alias="deleteAllSpecifications")


class DeleteAllSpecificationsDeleteAllSpecifications(BaseModel):
    id: str
    state: EntityState


DeleteAllSpecifications.model_rebuild()

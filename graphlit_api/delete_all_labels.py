# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteAllLabels(BaseModel):
    delete_all_labels: Optional[List[Optional["DeleteAllLabelsDeleteAllLabels"]]] = (
        Field(alias="deleteAllLabels")
    )


class DeleteAllLabelsDeleteAllLabels(BaseModel):
    id: str
    state: EntityState


DeleteAllLabels.model_rebuild()

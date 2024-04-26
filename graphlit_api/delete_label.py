# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteLabel(BaseModel):
    delete_label: Optional["DeleteLabelDeleteLabel"] = Field(alias="deleteLabel")


class DeleteLabelDeleteLabel(BaseModel):
    id: str
    state: EntityState


DeleteLabel.model_rebuild()

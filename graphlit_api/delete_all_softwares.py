# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteAllSoftwares(BaseModel):
    delete_all_softwares: Optional[
        List[Optional["DeleteAllSoftwaresDeleteAllSoftwares"]]
    ] = Field(alias="deleteAllSoftwares")


class DeleteAllSoftwaresDeleteAllSoftwares(BaseModel):
    id: str
    state: EntityState


DeleteAllSoftwares.model_rebuild()

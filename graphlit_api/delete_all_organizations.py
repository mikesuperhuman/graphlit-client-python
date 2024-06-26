# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteAllOrganizations(BaseModel):
    delete_all_organizations: Optional[
        List[Optional["DeleteAllOrganizationsDeleteAllOrganizations"]]
    ] = Field(alias="deleteAllOrganizations")


class DeleteAllOrganizationsDeleteAllOrganizations(BaseModel):
    id: str
    state: EntityState


DeleteAllOrganizations.model_rebuild()

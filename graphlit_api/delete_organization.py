# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteOrganization(BaseModel):
    delete_organization: Optional["DeleteOrganizationDeleteOrganization"] = Field(
        alias="deleteOrganization"
    )


class DeleteOrganizationDeleteOrganization(BaseModel):
    id: str
    state: EntityState


DeleteOrganization.model_rebuild()

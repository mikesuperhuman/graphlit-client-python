# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState, ModelServiceTypes, SpecificationTypes


class UpdateSpecification(BaseModel):
    update_specification: Optional["UpdateSpecificationUpdateSpecification"] = Field(
        alias="updateSpecification"
    )


class UpdateSpecificationUpdateSpecification(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[SpecificationTypes]
    service_type: Optional[ModelServiceTypes] = Field(alias="serviceType")


UpdateSpecification.model_rebuild()

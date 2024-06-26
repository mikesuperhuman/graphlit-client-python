# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import CollectionTypes, EntityState


class UpdateCollection(BaseModel):
    update_collection: Optional["UpdateCollectionUpdateCollection"] = Field(
        alias="updateCollection"
    )


class UpdateCollectionUpdateCollection(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[CollectionTypes]


UpdateCollection.model_rebuild()

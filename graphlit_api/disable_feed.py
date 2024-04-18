# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DisableFeed(BaseModel):
    disable_feed: Optional["DisableFeedDisableFeed"] = Field(alias="disableFeed")


class DisableFeedDisableFeed(BaseModel):
    id: str
    state: EntityState


DisableFeed.model_rebuild()
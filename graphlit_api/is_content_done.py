# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class IsContentDone(BaseModel):
    is_content_done: Optional["IsContentDoneIsContentDone"] = Field(
        alias="isContentDone"
    )


class IsContentDoneIsContentDone(BaseModel):
    result: Optional[bool]


IsContentDone.model_rebuild()

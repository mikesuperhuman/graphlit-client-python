# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ConversationTypes, EntityState


class CreateConversation(BaseModel):
    create_conversation: Optional["CreateConversationCreateConversation"] = Field(
        alias="createConversation"
    )


class CreateConversationCreateConversation(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[ConversationTypes]


CreateConversation.model_rebuild()

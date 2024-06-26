# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteWorkflow(BaseModel):
    delete_workflow: Optional["DeleteWorkflowDeleteWorkflow"] = Field(
        alias="deleteWorkflow"
    )


class DeleteWorkflowDeleteWorkflow(BaseModel):
    id: str
    state: EntityState


DeleteWorkflow.model_rebuild()

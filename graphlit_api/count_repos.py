# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class CountRepos(BaseModel):
    count_repos: Optional["CountReposCountRepos"] = Field(alias="countRepos")


class CountReposCountRepos(BaseModel):
    count: Optional[Any]


CountRepos.model_rebuild()

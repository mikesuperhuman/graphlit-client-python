# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class QueryMicrosoftTeamsTeams(BaseModel):
    microsoft_teams_teams: Optional["QueryMicrosoftTeamsTeamsMicrosoftTeamsTeams"] = (
        Field(alias="microsoftTeamsTeams")
    )


class QueryMicrosoftTeamsTeamsMicrosoftTeamsTeams(BaseModel):
    results: Optional[
        List[Optional["QueryMicrosoftTeamsTeamsMicrosoftTeamsTeamsResults"]]
    ]


class QueryMicrosoftTeamsTeamsMicrosoftTeamsTeamsResults(BaseModel):
    team_name: Optional[str] = Field(alias="teamName")
    team_id: Optional[str] = Field(alias="teamId")


QueryMicrosoftTeamsTeams.model_rebuild()
QueryMicrosoftTeamsTeamsMicrosoftTeamsTeams.model_rebuild()

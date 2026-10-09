from pydantic import BaseModel, Field


class GitHubUser(BaseModel):
    login: str
    followers: int = Field(ge=0)
    public_repos: int = Field(ge=0)
    html_url: str
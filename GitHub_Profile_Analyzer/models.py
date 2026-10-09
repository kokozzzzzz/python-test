

from pydantic import BaseModel, Field


class GitHubUser(BaseModel):
    login: str = Field(min_length=1,description="用户名")
    followers: int = Field(ge=0,description="粉丝数")
    public_repos: int = Field(ge=0,description="公开仓库数")
    html_url: str = Field(min_length=1,description="主页地址")

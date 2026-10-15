from pydantic import BaseModel, HttpUrl, RootModel


class Request(BaseModel):
    username: str
    repository: str


class Overview(BaseModel):
    stars_count: int
    forks_count: int
    issues_count: int
    last_update: str
    topics: list[str]


class CommitActivity(BaseModel):
    week_start_date: str
    commits_count: list[int]


class Author(BaseModel):
    username: str
    avatar_url: HttpUrl


class Contributors(BaseModel):
    commits_count: int
    author: Author | None


class PunchCard(BaseModel):
    day: int
    hour: int
    commits_count: int


class Languages(RootModel[dict[str, float]]):
    pass

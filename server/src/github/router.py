import os
from typing import Annotated

import httpx2
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from github.dependencies import get_http_client
from github.models import (
    CommitActivity,
    Contributors,
    Languages,
    Overview,
    PunchCard,
    Request,
)
from github.services import compute_percentages, format_date

load_dotenv()
GITHUB_PAT = os.environ["GITHUB_PAT"]

router = APIRouter()
headers = {"Authorization": f"Bearer {GITHUB_PAT}"}


@router.get("/repository/{username}/{repository}/overview", response_model=Overview)
async def get_overview(
    client: Annotated[httpx2.AsyncClient, Depends(get_http_client)],
    request: Annotated[Request, Depends()],
):
    response = await client.get(
        url=f"https://api.github.com/repos/{request.username}/{request.repository}",
        headers=headers,
    )

    data = response.json()

    return Overview(
        stars_count=data["stargazers_count"],
        forks_count=data["forks_count"],
        issues_count=data["open_issues_count"],
        last_update=format_date(data["updated_at"]),
    )


@router.get(
    "/repository/{username}/{repository}/commit-activity",
    response_model=list[CommitActivity],
)
async def get_commit_activity(
    client: Annotated[httpx2.AsyncClient, Depends(get_http_client)],
    request: Annotated[Request, Depends()],
):
    response = await client.get(
        url=f"https://api.github.com/repos/{request.username}/{request.repository}/stats/commit_activity",
        headers=headers,
    )

    data = response.json()

    return [
        CommitActivity(
            week_start_date=format_date(item["week"]), commits_count=item["days"]
        )
        for item in data
    ]


@router.get(
    "/repository/{username}/{repository}/contributors",
    response_model=list[Contributors],
)
async def get_contributors(
    client: Annotated[httpx2.AsyncClient, Depends(get_http_client)],
    request: Annotated[Request, Depends()],
):
    response = await client.get(
        url=f"https://api.github.com/repos/{request.username}/{request.repository}/stats/contributors",
        headers=headers,
        timeout=30,
    )

    data = response.json()
    return data


@router.get(
    "/repository/{username}/{repository}/punch-card",
    response_model=list[PunchCard],
)
async def get_punch_card(
    client: Annotated[httpx2.AsyncClient, Depends(get_http_client)],
    request: Annotated[Request, Depends()],
):
    response = await client.get(
        url=f"https://api.github.com/repos/{request.username}/{request.repository}/stats/punch_card",
        headers=headers,
    )

    data = response.json()

    keys = ["day", "hour", "commits_count"]
    result = [dict(zip(keys, item)) for item in data]

    return result


@router.get(
    "/repository/{username}/{repository}/languages",
    response_model=Languages,
)
async def get_languages(
    client: Annotated[httpx2.AsyncClient, Depends(get_http_client)],
    request: Annotated[Request, Depends()],
):
    response = await client.get(
        url=f"https://api.github.com/repos/{request.username}/{request.repository}/languages",
        headers=headers,
    )

    data = compute_percentages(response.json())
    return data

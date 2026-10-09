from pydantic import ValidationError
import pytest

from day7.models import GitHubUser


def test_valid_user():
    user = GitHubUser(
        login="octocat",
        followers=100,
        public_repos=10,
        html_url="https://github.com/octocat",
    )

    assert user.login == "octocat"
    assert user.followers == 100



def test_invalid_followers():
    with pytest.raises(ValidationError):
        GitHubUser(
            login="octocat",
            followers=-1,
            public_repos=10,
            html_url="https://github.com/octocat",
        )
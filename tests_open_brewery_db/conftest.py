import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://api.openbrewerydb.org',
        help='this is request url'
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

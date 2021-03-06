import json
import re
from requests.exceptions import HTTPError

from origo.status import Status
from origo.auth.auth import Authenticate
from origo.config import Config
from origo.file_cache import FileCache

config = Config()
file_cache = FileCache(config)
file_cache.credentials_cache_enabled = False
auth_default = Authenticate(config, file_cache=file_cache)


class TestStatus:
    def test_get_status(self, requests_mock):
        uuid = "my-uu-ii-dd-1"
        status = Status(config=config, auth=auth_default)
        response = json.dumps([{"id": "my-id"}, {"id": "my-other-id"}])
        matcher = re.compile(uuid)
        requests_mock.register_uri("GET", matcher, text=response, status_code=200)
        body = status.get_status(uuid)
        assert len(body) == 2

    def test_get_status_fails_will_produce_http_error(self, requests_mock):
        uuid = "my-uu-ii-dd-2"
        status = Status(config=config, auth=auth_default)
        response = json.dumps([{"id": "my-id"}, {"id": "my-other-id"}])
        matcher = re.compile(uuid)
        requests_mock.register_uri("GET", matcher, text=response, status_code=404)
        try:
            status.get_status(uuid)
        except HTTPError:
            assert True

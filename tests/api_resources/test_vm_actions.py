# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from kthcloud_go_deploy_v_ import KthcloudGoDeployV2, AsyncKthcloudGoDeployV2
from kthcloud_go_deploy_v_.types import VmActionCreated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVmActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: KthcloudGoDeployV2) -> None:
        vm_action = client.vm_actions.create(
            action="start",
        )
        assert_matches_type(VmActionCreated, vm_action, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: KthcloudGoDeployV2) -> None:
        response = client.vm_actions.with_raw_response.create(
            action="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm_action = response.parse()
        assert_matches_type(VmActionCreated, vm_action, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: KthcloudGoDeployV2) -> None:
        with client.vm_actions.with_streaming_response.create(
            action="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm_action = response.parse()
            assert_matches_type(VmActionCreated, vm_action, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVmActions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm_action = await async_client.vm_actions.create(
            action="start",
        )
        assert_matches_type(VmActionCreated, vm_action, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.vm_actions.with_raw_response.create(
            action="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm_action = await response.parse()
        assert_matches_type(VmActionCreated, vm_action, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.vm_actions.with_streaming_response.create(
            action="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm_action = await response.parse()
            assert_matches_type(VmActionCreated, vm_action, path=["response"])

        assert cast(Any, response.is_closed) is True

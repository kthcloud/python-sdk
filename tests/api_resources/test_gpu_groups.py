# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from kthcloud_go_deploy_v2 import KthcloudGoDeployV2, AsyncKthcloudGoDeployV2
from kthcloud_go_deploy_v2.types import GpuGroup, GpuGroupListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGpuGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: KthcloudGoDeployV2) -> None:
        gpu_group = client.gpu_groups.retrieve(
            "string",
        )
        assert_matches_type(GpuGroup, gpu_group, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: KthcloudGoDeployV2) -> None:
        response = client.gpu_groups.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_group = response.parse()
        assert_matches_type(GpuGroup, gpu_group, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: KthcloudGoDeployV2) -> None:
        with client.gpu_groups.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_group = response.parse()
            assert_matches_type(GpuGroup, gpu_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: KthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gpu_group_id` but received ''"):
            client.gpu_groups.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: KthcloudGoDeployV2) -> None:
        gpu_group = client.gpu_groups.list()
        assert_matches_type(GpuGroupListResponse, gpu_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: KthcloudGoDeployV2) -> None:
        gpu_group = client.gpu_groups.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(GpuGroupListResponse, gpu_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: KthcloudGoDeployV2) -> None:
        response = client.gpu_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_group = response.parse()
        assert_matches_type(GpuGroupListResponse, gpu_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: KthcloudGoDeployV2) -> None:
        with client.gpu_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_group = response.parse()
            assert_matches_type(GpuGroupListResponse, gpu_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGpuGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_group = await async_client.gpu_groups.retrieve(
            "string",
        )
        assert_matches_type(GpuGroup, gpu_group, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.gpu_groups.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_group = await response.parse()
        assert_matches_type(GpuGroup, gpu_group, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.gpu_groups.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_group = await response.parse()
            assert_matches_type(GpuGroup, gpu_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gpu_group_id` but received ''"):
            await async_client.gpu_groups.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_group = await async_client.gpu_groups.list()
        assert_matches_type(GpuGroupListResponse, gpu_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_group = await async_client.gpu_groups.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(GpuGroupListResponse, gpu_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.gpu_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_group = await response.parse()
        assert_matches_type(GpuGroupListResponse, gpu_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.gpu_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_group = await response.parse()
            assert_matches_type(GpuGroupListResponse, gpu_group, path=["response"])

        assert cast(Any, response.is_closed) is True
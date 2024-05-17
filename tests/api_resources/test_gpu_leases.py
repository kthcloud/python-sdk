# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from kthcloud_go_deploy_v_ import KthcloudGoDeployV2, AsyncKthcloudGoDeployV2
from kthcloud_go_deploy_v_.types import (
    GPULeaseRead,
    GPULeaseCreated,
    GPULeaseDeleted,
    GPULeaseUpdated,
    GPULeaseListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGPULeases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: KthcloudGoDeployV2) -> None:
        gpu_lease = client.gpu_leases.create(
            gpu_group_id="string",
        )
        assert_matches_type(GPULeaseCreated, gpu_lease, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: KthcloudGoDeployV2) -> None:
        gpu_lease = client.gpu_leases.create(
            gpu_group_id="string",
            lease_forever=True,
        )
        assert_matches_type(GPULeaseCreated, gpu_lease, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: KthcloudGoDeployV2) -> None:
        response = client.gpu_leases.with_raw_response.create(
            gpu_group_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = response.parse()
        assert_matches_type(GPULeaseCreated, gpu_lease, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: KthcloudGoDeployV2) -> None:
        with client.gpu_leases.with_streaming_response.create(
            gpu_group_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = response.parse()
            assert_matches_type(GPULeaseCreated, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: KthcloudGoDeployV2) -> None:
        gpu_lease = client.gpu_leases.retrieve(
            "string",
        )
        assert_matches_type(GPULeaseRead, gpu_lease, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: KthcloudGoDeployV2) -> None:
        response = client.gpu_leases.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = response.parse()
        assert_matches_type(GPULeaseRead, gpu_lease, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: KthcloudGoDeployV2) -> None:
        with client.gpu_leases.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = response.parse()
            assert_matches_type(GPULeaseRead, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: KthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gpu_lease_id` but received ''"):
            client.gpu_leases.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: KthcloudGoDeployV2) -> None:
        gpu_lease = client.gpu_leases.update(
            "string",
        )
        assert_matches_type(GPULeaseUpdated, gpu_lease, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: KthcloudGoDeployV2) -> None:
        gpu_lease = client.gpu_leases.update(
            "string",
            vm_id="string",
        )
        assert_matches_type(GPULeaseUpdated, gpu_lease, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: KthcloudGoDeployV2) -> None:
        response = client.gpu_leases.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = response.parse()
        assert_matches_type(GPULeaseUpdated, gpu_lease, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: KthcloudGoDeployV2) -> None:
        with client.gpu_leases.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = response.parse()
            assert_matches_type(GPULeaseUpdated, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: KthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gpu_lease_id` but received ''"):
            client.gpu_leases.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: KthcloudGoDeployV2) -> None:
        gpu_lease = client.gpu_leases.list()
        assert_matches_type(GPULeaseListResponse, gpu_lease, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: KthcloudGoDeployV2) -> None:
        gpu_lease = client.gpu_leases.list(
            all=True,
            page=0,
            page_size=0,
            vm_id="string",
        )
        assert_matches_type(GPULeaseListResponse, gpu_lease, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: KthcloudGoDeployV2) -> None:
        response = client.gpu_leases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = response.parse()
        assert_matches_type(GPULeaseListResponse, gpu_lease, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: KthcloudGoDeployV2) -> None:
        with client.gpu_leases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = response.parse()
            assert_matches_type(GPULeaseListResponse, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: KthcloudGoDeployV2) -> None:
        gpu_lease = client.gpu_leases.delete(
            "string",
        )
        assert_matches_type(GPULeaseDeleted, gpu_lease, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: KthcloudGoDeployV2) -> None:
        response = client.gpu_leases.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = response.parse()
        assert_matches_type(GPULeaseDeleted, gpu_lease, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: KthcloudGoDeployV2) -> None:
        with client.gpu_leases.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = response.parse()
            assert_matches_type(GPULeaseDeleted, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: KthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gpu_lease_id` but received ''"):
            client.gpu_leases.with_raw_response.delete(
                "",
            )


class TestAsyncGPULeases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_lease = await async_client.gpu_leases.create(
            gpu_group_id="string",
        )
        assert_matches_type(GPULeaseCreated, gpu_lease, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_lease = await async_client.gpu_leases.create(
            gpu_group_id="string",
            lease_forever=True,
        )
        assert_matches_type(GPULeaseCreated, gpu_lease, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.gpu_leases.with_raw_response.create(
            gpu_group_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = await response.parse()
        assert_matches_type(GPULeaseCreated, gpu_lease, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.gpu_leases.with_streaming_response.create(
            gpu_group_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = await response.parse()
            assert_matches_type(GPULeaseCreated, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_lease = await async_client.gpu_leases.retrieve(
            "string",
        )
        assert_matches_type(GPULeaseRead, gpu_lease, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.gpu_leases.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = await response.parse()
        assert_matches_type(GPULeaseRead, gpu_lease, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.gpu_leases.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = await response.parse()
            assert_matches_type(GPULeaseRead, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gpu_lease_id` but received ''"):
            await async_client.gpu_leases.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_lease = await async_client.gpu_leases.update(
            "string",
        )
        assert_matches_type(GPULeaseUpdated, gpu_lease, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_lease = await async_client.gpu_leases.update(
            "string",
            vm_id="string",
        )
        assert_matches_type(GPULeaseUpdated, gpu_lease, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.gpu_leases.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = await response.parse()
        assert_matches_type(GPULeaseUpdated, gpu_lease, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.gpu_leases.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = await response.parse()
            assert_matches_type(GPULeaseUpdated, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gpu_lease_id` but received ''"):
            await async_client.gpu_leases.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_lease = await async_client.gpu_leases.list()
        assert_matches_type(GPULeaseListResponse, gpu_lease, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_lease = await async_client.gpu_leases.list(
            all=True,
            page=0,
            page_size=0,
            vm_id="string",
        )
        assert_matches_type(GPULeaseListResponse, gpu_lease, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.gpu_leases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = await response.parse()
        assert_matches_type(GPULeaseListResponse, gpu_lease, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.gpu_leases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = await response.parse()
            assert_matches_type(GPULeaseListResponse, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        gpu_lease = await async_client.gpu_leases.delete(
            "string",
        )
        assert_matches_type(GPULeaseDeleted, gpu_lease, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.gpu_leases.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gpu_lease = await response.parse()
        assert_matches_type(GPULeaseDeleted, gpu_lease, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.gpu_leases.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gpu_lease = await response.parse()
            assert_matches_type(GPULeaseDeleted, gpu_lease, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gpu_lease_id` but received ''"):
            await async_client.gpu_leases.with_raw_response.delete(
                "",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from kthcloud_go_deploy_v_ import KthcloudGoDeployV2, AsyncKthcloudGoDeployV2
from kthcloud_go_deploy_v_.types import (
    VmRead,
    VmCreated,
    VmDeleted,
    VmUpdated,
    VmListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: KthcloudGoDeployV2) -> None:
        vm = client.vms.create(
            cpu_cores=1,
            disk_size=10,
            name="xxx",
            ram=1,
            ssh_public_key="string",
        )
        assert_matches_type(VmCreated, vm, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: KthcloudGoDeployV2) -> None:
        vm = client.vms.create(
            cpu_cores=1,
            disk_size=10,
            name="xxx",
            ram=1,
            ssh_public_key="string",
            ports=[
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
            ],
            zone="string",
        )
        assert_matches_type(VmCreated, vm, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: KthcloudGoDeployV2) -> None:
        response = client.vms.with_raw_response.create(
            cpu_cores=1,
            disk_size=10,
            name="xxx",
            ram=1,
            ssh_public_key="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = response.parse()
        assert_matches_type(VmCreated, vm, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: KthcloudGoDeployV2) -> None:
        with client.vms.with_streaming_response.create(
            cpu_cores=1,
            disk_size=10,
            name="xxx",
            ram=1,
            ssh_public_key="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = response.parse()
            assert_matches_type(VmCreated, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: KthcloudGoDeployV2) -> None:
        vm = client.vms.retrieve(
            "string",
        )
        assert_matches_type(VmRead, vm, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: KthcloudGoDeployV2) -> None:
        response = client.vms.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = response.parse()
        assert_matches_type(VmRead, vm, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: KthcloudGoDeployV2) -> None:
        with client.vms.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = response.parse()
            assert_matches_type(VmRead, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: KthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vm_id` but received ''"):
            client.vms.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: KthcloudGoDeployV2) -> None:
        vm = client.vms.update(
            "string",
        )
        assert_matches_type(VmUpdated, vm, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: KthcloudGoDeployV2) -> None:
        vm = client.vms.update(
            "string",
            cpu_cores=1,
            name="xxx",
            owner_id="string",
            ports=[
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
            ],
            ram=1,
        )
        assert_matches_type(VmUpdated, vm, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: KthcloudGoDeployV2) -> None:
        response = client.vms.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = response.parse()
        assert_matches_type(VmUpdated, vm, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: KthcloudGoDeployV2) -> None:
        with client.vms.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = response.parse()
            assert_matches_type(VmUpdated, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: KthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vm_id` but received ''"):
            client.vms.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: KthcloudGoDeployV2) -> None:
        vm = client.vms.list()
        assert_matches_type(VmListResponse, vm, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: KthcloudGoDeployV2) -> None:
        vm = client.vms.list(
            all=True,
            page=0,
            page_size=0,
            user_id="string",
        )
        assert_matches_type(VmListResponse, vm, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: KthcloudGoDeployV2) -> None:
        response = client.vms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = response.parse()
        assert_matches_type(VmListResponse, vm, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: KthcloudGoDeployV2) -> None:
        with client.vms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = response.parse()
            assert_matches_type(VmListResponse, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: KthcloudGoDeployV2) -> None:
        vm = client.vms.delete(
            "string",
        )
        assert_matches_type(VmDeleted, vm, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: KthcloudGoDeployV2) -> None:
        response = client.vms.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = response.parse()
        assert_matches_type(VmDeleted, vm, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: KthcloudGoDeployV2) -> None:
        with client.vms.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = response.parse()
            assert_matches_type(VmDeleted, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: KthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vm_id` but received ''"):
            client.vms.with_raw_response.delete(
                "",
            )


class TestAsyncVms:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm = await async_client.vms.create(
            cpu_cores=1,
            disk_size=10,
            name="xxx",
            ram=1,
            ssh_public_key="string",
        )
        assert_matches_type(VmCreated, vm, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm = await async_client.vms.create(
            cpu_cores=1,
            disk_size=10,
            name="xxx",
            ram=1,
            ssh_public_key="string",
            ports=[
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
            ],
            zone="string",
        )
        assert_matches_type(VmCreated, vm, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.vms.with_raw_response.create(
            cpu_cores=1,
            disk_size=10,
            name="xxx",
            ram=1,
            ssh_public_key="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = await response.parse()
        assert_matches_type(VmCreated, vm, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.vms.with_streaming_response.create(
            cpu_cores=1,
            disk_size=10,
            name="xxx",
            ram=1,
            ssh_public_key="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = await response.parse()
            assert_matches_type(VmCreated, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm = await async_client.vms.retrieve(
            "string",
        )
        assert_matches_type(VmRead, vm, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.vms.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = await response.parse()
        assert_matches_type(VmRead, vm, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.vms.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = await response.parse()
            assert_matches_type(VmRead, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vm_id` but received ''"):
            await async_client.vms.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm = await async_client.vms.update(
            "string",
        )
        assert_matches_type(VmUpdated, vm, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm = await async_client.vms.update(
            "string",
            cpu_cores=1,
            name="xxx",
            owner_id="string",
            ports=[
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
                {
                    "http_proxy": {
                        "custom_domain": "string",
                        "name": "xxx",
                    },
                    "name": "x",
                    "port": 1,
                    "protocol": "tcp",
                },
            ],
            ram=1,
        )
        assert_matches_type(VmUpdated, vm, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.vms.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = await response.parse()
        assert_matches_type(VmUpdated, vm, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.vms.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = await response.parse()
            assert_matches_type(VmUpdated, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vm_id` but received ''"):
            await async_client.vms.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm = await async_client.vms.list()
        assert_matches_type(VmListResponse, vm, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm = await async_client.vms.list(
            all=True,
            page=0,
            page_size=0,
            user_id="string",
        )
        assert_matches_type(VmListResponse, vm, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.vms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = await response.parse()
        assert_matches_type(VmListResponse, vm, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.vms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = await response.parse()
            assert_matches_type(VmListResponse, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        vm = await async_client.vms.delete(
            "string",
        )
        assert_matches_type(VmDeleted, vm, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.vms.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vm = await response.parse()
        assert_matches_type(VmDeleted, vm, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.vms.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vm = await response.parse()
            assert_matches_type(VmDeleted, vm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vm_id` but received ''"):
            await async_client.vms.with_raw_response.delete(
                "",
            )

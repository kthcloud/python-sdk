# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from kthcloud_go_deploy_v_ import KthcloudGoDeployV2, AsyncKthcloudGoDeployV2
from kthcloud_go_deploy_v_.types.vms import VmSnapshotDeleted

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshot:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: KthcloudGoDeployV2) -> None:
        snapshot = client.vms.snapshot.delete(
            "string",
            vm_id="string",
        )
        assert_matches_type(VmSnapshotDeleted, snapshot, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: KthcloudGoDeployV2) -> None:
        response = client.vms.snapshot.with_raw_response.delete(
            "string",
            vm_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(VmSnapshotDeleted, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: KthcloudGoDeployV2) -> None:
        with client.vms.snapshot.with_streaming_response.delete(
            "string",
            vm_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(VmSnapshotDeleted, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: KthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vm_id` but received ''"):
            client.vms.snapshot.with_raw_response.delete(
                "string",
                vm_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            client.vms.snapshot.with_raw_response.delete(
                "",
                vm_id="string",
            )


class TestAsyncSnapshot:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        snapshot = await async_client.vms.snapshot.delete(
            "string",
            vm_id="string",
        )
        assert_matches_type(VmSnapshotDeleted, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        response = await async_client.vms.snapshot.with_raw_response.delete(
            "string",
            vm_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(VmSnapshotDeleted, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        async with async_client.vms.snapshot.with_streaming_response.delete(
            "string",
            vm_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(VmSnapshotDeleted, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKthcloudGoDeployV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vm_id` but received ''"):
            await async_client.vms.snapshot.with_raw_response.delete(
                "string",
                vm_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            await async_client.vms.snapshot.with_raw_response.delete(
                "",
                vm_id="string",
            )

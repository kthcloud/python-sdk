# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from kthcloud import Kthcloud, AsyncKthcloud
from tests.utils import assert_matches_type
from kthcloud.types import VmSnapshotCreated, SnapshotListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Kthcloud) -> None:
        snapshot = client.snapshots.create()
        assert_matches_type(VmSnapshotCreated, snapshot, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Kthcloud) -> None:
        response = client.snapshots.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(VmSnapshotCreated, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Kthcloud) -> None:
        with client.snapshots.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(VmSnapshotCreated, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Kthcloud) -> None:
        snapshot = client.snapshots.list()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Kthcloud) -> None:
        snapshot = client.snapshots.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Kthcloud) -> None:
        response = client.snapshots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Kthcloud) -> None:
        with client.snapshots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSnapshots:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKthcloud) -> None:
        snapshot = await async_client.snapshots.create()
        assert_matches_type(VmSnapshotCreated, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKthcloud) -> None:
        response = await async_client.snapshots.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(VmSnapshotCreated, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKthcloud) -> None:
        async with async_client.snapshots.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(VmSnapshotCreated, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncKthcloud) -> None:
        snapshot = await async_client.snapshots.list()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKthcloud) -> None:
        snapshot = await async_client.snapshots.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKthcloud) -> None:
        response = await async_client.snapshots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKthcloud) -> None:
        async with async_client.snapshots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

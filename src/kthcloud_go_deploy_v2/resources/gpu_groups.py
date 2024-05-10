# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import gpu_group_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.gpu_group import GpuGroup
from ..types.gpu_group_list_response import GpuGroupListResponse

__all__ = ["GpuGroupsResource", "AsyncGpuGroupsResource"]


class GpuGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GpuGroupsResourceWithRawResponse:
        return GpuGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GpuGroupsResourceWithStreamingResponse:
        return GpuGroupsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        gpu_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GpuGroup:
        """
        Get GPU group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gpu_group_id:
            raise ValueError(f"Expected a non-empty value for `gpu_group_id` but received {gpu_group_id!r}")
        return self._get(
            f"/v2/gpuGroups/{gpu_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GpuGroup,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GpuGroupListResponse:
        """
        List GPU groups

        Args:
          page: Page number

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gpuGroups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    gpu_group_list_params.GpuGroupListParams,
                ),
            ),
            cast_to=GpuGroupListResponse,
        )


class AsyncGpuGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGpuGroupsResourceWithRawResponse:
        return AsyncGpuGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGpuGroupsResourceWithStreamingResponse:
        return AsyncGpuGroupsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        gpu_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GpuGroup:
        """
        Get GPU group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gpu_group_id:
            raise ValueError(f"Expected a non-empty value for `gpu_group_id` but received {gpu_group_id!r}")
        return await self._get(
            f"/v2/gpuGroups/{gpu_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GpuGroup,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GpuGroupListResponse:
        """
        List GPU groups

        Args:
          page: Page number

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gpuGroups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    gpu_group_list_params.GpuGroupListParams,
                ),
            ),
            cast_to=GpuGroupListResponse,
        )


class GpuGroupsResourceWithRawResponse:
    def __init__(self, gpu_groups: GpuGroupsResource) -> None:
        self._gpu_groups = gpu_groups

        self.retrieve = to_raw_response_wrapper(
            gpu_groups.retrieve,
        )
        self.list = to_raw_response_wrapper(
            gpu_groups.list,
        )


class AsyncGpuGroupsResourceWithRawResponse:
    def __init__(self, gpu_groups: AsyncGpuGroupsResource) -> None:
        self._gpu_groups = gpu_groups

        self.retrieve = async_to_raw_response_wrapper(
            gpu_groups.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            gpu_groups.list,
        )


class GpuGroupsResourceWithStreamingResponse:
    def __init__(self, gpu_groups: GpuGroupsResource) -> None:
        self._gpu_groups = gpu_groups

        self.retrieve = to_streamed_response_wrapper(
            gpu_groups.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            gpu_groups.list,
        )


class AsyncGpuGroupsResourceWithStreamingResponse:
    def __init__(self, gpu_groups: AsyncGpuGroupsResource) -> None:
        self._gpu_groups = gpu_groups

        self.retrieve = async_to_streamed_response_wrapper(
            gpu_groups.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            gpu_groups.list,
        )

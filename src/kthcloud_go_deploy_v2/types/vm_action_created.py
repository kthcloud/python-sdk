# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VmActionCreated"]


class VmActionCreated(BaseModel):
    id: Optional[str] = None

    job_id: Optional[str] = FieldInfo(alias="jobId", default=None)

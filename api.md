# Shared Types

```python
from kthcloud_go_deploy_v2.types import VmSnapshotRead
```

# GpuGroups

Types:

```python
from kthcloud_go_deploy_v2.types import GpuGroup, GpuGroupListResponse
```

Methods:

- <code title="get /v2/gpuGroups/{gpuGroupId}">client.gpu_groups.<a href="./src/kthcloud_go_deploy_v2/resources/gpu_groups.py">retrieve</a>(gpu_group_id) -> <a href="./src/kthcloud_go_deploy_v2/types/gpu_group.py">GpuGroup</a></code>
- <code title="get /v2/gpuGroups">client.gpu_groups.<a href="./src/kthcloud_go_deploy_v2/resources/gpu_groups.py">list</a>(\*\*<a href="src/kthcloud_go_deploy_v2/types/gpu_group_list_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/gpu_group_list_response.py">GpuGroupListResponse</a></code>

# GpuLeases

Types:

```python
from kthcloud_go_deploy_v2.types import (
    GpuLeaseCreated,
    GpuLeaseDeleted,
    GpuLeaseRead,
    GpuLeaseUpdated,
    GpuLeaseListResponse,
)
```

Methods:

- <code title="post /v2/gpuLeases">client.gpu_leases.<a href="./src/kthcloud_go_deploy_v2/resources/gpu_leases.py">create</a>(\*\*<a href="src/kthcloud_go_deploy_v2/types/gpu_lease_create_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/gpu_lease_created.py">GpuLeaseCreated</a></code>
- <code title="get /v2/gpuLeases/{gpuLeaseId}">client.gpu_leases.<a href="./src/kthcloud_go_deploy_v2/resources/gpu_leases.py">retrieve</a>(gpu_lease_id) -> <a href="./src/kthcloud_go_deploy_v2/types/gpu_lease_read.py">GpuLeaseRead</a></code>
- <code title="post /v2/gpuLeases/{gpuLeaseId}">client.gpu_leases.<a href="./src/kthcloud_go_deploy_v2/resources/gpu_leases.py">update</a>(gpu_lease_id, \*\*<a href="src/kthcloud_go_deploy_v2/types/gpu_lease_update_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/gpu_lease_updated.py">GpuLeaseUpdated</a></code>
- <code title="get /v2/gpuLeases">client.gpu_leases.<a href="./src/kthcloud_go_deploy_v2/resources/gpu_leases.py">list</a>(\*\*<a href="src/kthcloud_go_deploy_v2/types/gpu_lease_list_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/gpu_lease_list_response.py">GpuLeaseListResponse</a></code>
- <code title="delete /v2/gpuLeases/{gpuLeaseId}">client.gpu_leases.<a href="./src/kthcloud_go_deploy_v2/resources/gpu_leases.py">delete</a>(gpu_lease_id) -> <a href="./src/kthcloud_go_deploy_v2/types/gpu_lease_deleted.py">GpuLeaseDeleted</a></code>

# Snapshots

Types:

```python
from kthcloud_go_deploy_v2.types import VmSnapshotCreated, SnapshotListResponse
```

Methods:

- <code title="post /v2/snapshots">client.snapshots.<a href="./src/kthcloud_go_deploy_v2/resources/snapshots.py">create</a>() -> <a href="./src/kthcloud_go_deploy_v2/types/vm_snapshot_created.py">VmSnapshotCreated</a></code>
- <code title="get /v2/snapshots">client.snapshots.<a href="./src/kthcloud_go_deploy_v2/resources/snapshots.py">list</a>(\*\*<a href="src/kthcloud_go_deploy_v2/types/snapshot_list_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/snapshot_list_response.py">SnapshotListResponse</a></code>

# VmActions

Types:

```python
from kthcloud_go_deploy_v2.types import VmActionCreated
```

Methods:

- <code title="post /v2/vmActions">client.vm_actions.<a href="./src/kthcloud_go_deploy_v2/resources/vm_actions.py">create</a>(\*\*<a href="src/kthcloud_go_deploy_v2/types/vm_action_create_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/vm_action_created.py">VmActionCreated</a></code>

# Vms

Types:

```python
from kthcloud_go_deploy_v2.types import VmCreated, VmDeleted, VmRead, VmUpdated, VmListResponse
```

Methods:

- <code title="post /v2/vms">client.vms.<a href="./src/kthcloud_go_deploy_v2/resources/vms/vms.py">create</a>(\*\*<a href="src/kthcloud_go_deploy_v2/types/vm_create_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/vm_created.py">VmCreated</a></code>
- <code title="get /v2/vms/{vmId}">client.vms.<a href="./src/kthcloud_go_deploy_v2/resources/vms/vms.py">retrieve</a>(vm_id) -> <a href="./src/kthcloud_go_deploy_v2/types/vm_read.py">VmRead</a></code>
- <code title="post /v2/vms/{vmId}">client.vms.<a href="./src/kthcloud_go_deploy_v2/resources/vms/vms.py">update</a>(vm_id, \*\*<a href="src/kthcloud_go_deploy_v2/types/vm_update_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/vm_updated.py">VmUpdated</a></code>
- <code title="get /v2/vms">client.vms.<a href="./src/kthcloud_go_deploy_v2/resources/vms/vms.py">list</a>(\*\*<a href="src/kthcloud_go_deploy_v2/types/vm_list_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v2/types/vm_list_response.py">VmListResponse</a></code>
- <code title="delete /v2/vms/{vmId}">client.vms.<a href="./src/kthcloud_go_deploy_v2/resources/vms/vms.py">delete</a>(vm_id) -> <a href="./src/kthcloud_go_deploy_v2/types/vm_deleted.py">VmDeleted</a></code>

## Snapshot

Methods:

- <code title="delete /v2/vms/{vmId}/snapshot/{snapshotId}">client.vms.snapshot.<a href="./src/kthcloud_go_deploy_v2/resources/vms/snapshot.py">delete</a>(snapshot_id, \*, vm_id) -> <a href="./src/kthcloud_go_deploy_v2/types/vms/vm_snapshot_deleted.py">VmSnapshotDeleted</a></code>

## Snapshots

Types:

```python
from kthcloud_go_deploy_v2.types.vms import VmSnapshotDeleted
```

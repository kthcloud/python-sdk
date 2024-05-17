# Shared Types

```python
from kthcloud_go_deploy_v_.types import VmSnapshotRead
```

# GPUGroups

Types:

```python
from kthcloud_go_deploy_v_.types import GPUGroup, GPUGroupListResponse
```

Methods:

- <code title="get /v2/gpuGroups/{gpuGroupId}">client.gpu*groups.<a href="./src/kthcloud_go_deploy_v*/resources/gpu*groups.py">retrieve</a>(gpu_group_id) -> <a href="./src/kthcloud_go_deploy_v*/types/gpu_group.py">GPUGroup</a></code>
- <code title="get /v2/gpuGroups">client.gpu*groups.<a href="./src/kthcloud_go_deploy_v*/resources/gpu*groups.py">list</a>(\*\*<a href="src/kthcloud_go_deploy_v*/types/gpu*group_list_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v*/types/gpu_group_list_response.py">GPUGroupListResponse</a></code>

# GPULeases

Types:

```python
from kthcloud_go_deploy_v_.types import (
    GPULeaseCreated,
    GPULeaseDeleted,
    GPULeaseRead,
    GPULeaseUpdated,
    GPULeaseListResponse,
)
```

Methods:

- <code title="post /v2/gpuLeases">client.gpu*leases.<a href="./src/kthcloud_go_deploy_v*/resources/gpu*leases.py">create</a>(\*\*<a href="src/kthcloud_go_deploy_v*/types/gpu*lease_create_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v*/types/gpu_lease_created.py">GPULeaseCreated</a></code>
- <code title="get /v2/gpuLeases/{gpuLeaseId}">client.gpu*leases.<a href="./src/kthcloud_go_deploy_v*/resources/gpu*leases.py">retrieve</a>(gpu_lease_id) -> <a href="./src/kthcloud_go_deploy_v*/types/gpu_lease_read.py">GPULeaseRead</a></code>
- <code title="post /v2/gpuLeases/{gpuLeaseId}">client.gpu*leases.<a href="./src/kthcloud_go_deploy_v*/resources/gpu*leases.py">update</a>(gpu_lease_id, \*\*<a href="src/kthcloud_go_deploy_v*/types/gpu*lease_update_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v*/types/gpu_lease_updated.py">GPULeaseUpdated</a></code>
- <code title="get /v2/gpuLeases">client.gpu*leases.<a href="./src/kthcloud_go_deploy_v*/resources/gpu*leases.py">list</a>(\*\*<a href="src/kthcloud_go_deploy_v*/types/gpu*lease_list_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v*/types/gpu_lease_list_response.py">GPULeaseListResponse</a></code>
- <code title="delete /v2/gpuLeases/{gpuLeaseId}">client.gpu*leases.<a href="./src/kthcloud_go_deploy_v*/resources/gpu*leases.py">delete</a>(gpu_lease_id) -> <a href="./src/kthcloud_go_deploy_v*/types/gpu_lease_deleted.py">GPULeaseDeleted</a></code>

# Snapshots

Types:

```python
from kthcloud_go_deploy_v_.types import VmSnapshotCreated, SnapshotListResponse
```

Methods:

- <code title="post /v2/snapshots">client.snapshots.<a href="./src/kthcloud_go_deploy_v_/resources/snapshots.py">create</a>() -> <a href="./src/kthcloud_go_deploy_v_/types/vm_snapshot_created.py">VmSnapshotCreated</a></code>
- <code title="get /v2/snapshots">client.snapshots.<a href="./src/kthcloud_go_deploy_v_/resources/snapshots.py">list</a>(\*\*<a href="src/kthcloud_go_deploy_v_/types/snapshot_list_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v_/types/snapshot_list_response.py">SnapshotListResponse</a></code>

# VmActions

Types:

```python
from kthcloud_go_deploy_v_.types import VmActionCreated
```

Methods:

- <code title="post /v2/vmActions">client.vm*actions.<a href="./src/kthcloud_go_deploy_v*/resources/vm*actions.py">create</a>(\*\*<a href="src/kthcloud_go_deploy_v*/types/vm*action_create_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v*/types/vm_action_created.py">VmActionCreated</a></code>

# Vms

Types:

```python
from kthcloud_go_deploy_v_.types import VmCreated, VmDeleted, VmRead, VmUpdated, VmListResponse
```

Methods:

- <code title="post /v2/vms">client.vms.<a href="./src/kthcloud_go_deploy_v_/resources/vms/vms.py">create</a>(\*\*<a href="src/kthcloud_go_deploy_v_/types/vm_create_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v_/types/vm_created.py">VmCreated</a></code>
- <code title="get /v2/vms/{vmId}">client.vms.<a href="./src/kthcloud_go_deploy_v_/resources/vms/vms.py">retrieve</a>(vm*id) -> <a href="./src/kthcloud_go_deploy_v*/types/vm_read.py">VmRead</a></code>
- <code title="post /v2/vms/{vmId}">client.vms.<a href="./src/kthcloud_go_deploy_v_/resources/vms/vms.py">update</a>(vm*id, \*\*<a href="src/kthcloud_go_deploy_v*/types/vm*update_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v*/types/vm_updated.py">VmUpdated</a></code>
- <code title="get /v2/vms">client.vms.<a href="./src/kthcloud_go_deploy_v_/resources/vms/vms.py">list</a>(\*\*<a href="src/kthcloud_go_deploy_v_/types/vm_list_params.py">params</a>) -> <a href="./src/kthcloud_go_deploy_v_/types/vm_list_response.py">VmListResponse</a></code>
- <code title="delete /v2/vms/{vmId}">client.vms.<a href="./src/kthcloud_go_deploy_v_/resources/vms/vms.py">delete</a>(vm*id) -> <a href="./src/kthcloud_go_deploy_v*/types/vm_deleted.py">VmDeleted</a></code>

## Snapshot

Methods:

- <code title="delete /v2/vms/{vmId}/snapshot/{snapshotId}">client.vms.snapshot.<a href="./src/kthcloud_go_deploy_v_/resources/vms/snapshot.py">delete</a>(snapshot*id, \*, vm_id) -> <a href="./src/kthcloud_go_deploy_v*/types/vms/vm_snapshot_deleted.py">VmSnapshotDeleted</a></code>

## Snapshots

Types:

```python
from kthcloud_go_deploy_v_.types.vms import VmSnapshotDeleted
```

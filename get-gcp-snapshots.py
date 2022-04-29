import os
from typing import Dict, Iterable
from unicodedata import name
import json

from google.cloud import compute_v1


def list_snapshots(
    project_id: str,
) -> Dict[str, Iterable[compute_v1.SnapshotList]]:

    snapshot_client = compute_v1.SnapshotsClient()
    request = compute_v1.ListSnapshotsRequest()
    request.project = project_id
    request.order_by = 'creationTimestamp desc'

    agg_list = snapshot_client.list(request=request)

    snapshot_dict = {}
    for i in agg_list:
        if("snapshot-1" in i.name ):
            snapshot_dict.update(snapshot_1=i.name)
        elif("snapshot-2" in i.name):
            snapshot_dict.update(snapshot_2=i.name)
        elif("snapshot-3" in i.name):
            snapshot_dict.update(snapshot_3=i.name)
        if(len(snapshot_dict) == 3):
            break
    # it will dump the dict into json format to make it useable with terraform, ansible and other SDK's
    snapshot_json = json.dumps(snapshot_dict)
    print(snapshot_json)


if __name__ == '__main__':
    # export your project ID in terminal as 
    # export PROJECT_ID=<type-here>
    PROJECT_ID = os.environ['PROJECT_ID']
    list_snapshots(PROJECT_ID)
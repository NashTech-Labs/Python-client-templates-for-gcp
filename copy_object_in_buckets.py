import os
from google.cloud import storage


def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name
):
    """Copies a blob from one bucket to another with a new name."""

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )

if __name__ == "__main__":
    # export these variables to copy the data between two buckets
    BUCKET_NAME=os.environ['BUCKET_NAME']
    BLOB_NAME=os.environ['OBJECT_NAME']
    DEST_BUCKET_NAME=os.environ['DEST_BUCKET_NAME']
    DEST_BLOB_NAME=os.environ['DEST_BLOB_NAME']

    copy_blob(BUCKET_NAME, BLOB_NAME, DEST_BUCKET_NAME, DEST_BLOB_NAME)
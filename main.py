import base64
import os
from google.cloud import storage

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event

    storage_client = storage.Client()

    destination = storage_client.bucket(os.environ['DESTINATION_BUCKET'])

    bucket_name = file['bucket']
    file_name = file['name']
    uri = f"gs://{bucket_name}/{file_name}"

    origin = storage_client.bucket(bucket_name)

    blob = origin.blob(file_name)

    origin.copy_blob(blob, destination)

    return "done"
import anvil.server
from google.cloud import storage

# @anvil.server.http_endpoint("/get_product/:id")
@anvil.server.callable
def get_product(id):
#   ip = anvil.server.request.remote_address
  return f"You requested product {id}"


@anvil.server.callable
def send_audio_file(file):
#   ip = anvil.server.request.remote_address
  upload_blob()
  res = {
    "name": file.name,
    "length": file.length,
    "content_type": file.content_type,
  }
  return res


def upload_blob(source_file_name):
  bucket_name = "make3400_cloudbuild"
  source_file_name = local/path/to/file
  destination_blob_name = "gs://make3400_cloudbuild"
  storage_client = storage.Client()
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)
  blob.upload_from_filename(source_file_name)

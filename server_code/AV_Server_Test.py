import anvil.server
# from google.cloud import storage

# @anvil.server.http_endpoint("/get_product/:id")
@anvil.server.callable
def get_product(id):
#   ip = anvil.server.request.remote_address
  return f"You requested product {id}"


@anvil.server.callable
def send_audio_file(file):
#   ip = anvil.server.request.remote_address
#   upload_blob()
  headers = {
    'Authorization': 'Bearer ya29.A0ARrdaM93tW9QhwnJbE-7G_arWDI3g6WE58jnEYXnjx3P7QoXxIKiPL24pQDSZLp_PPQlWiJLAXs32h0-W8w3jtVf8Wk4WL4Y7yc9650dDxzqK4KXcFhs4gHirlK3Ih9v6O9noQJ0h-5WhzaQK5a1luDD4YPh',
    'Content-Type': file.content_type,
  }
  resp = anvil.http.request(f'https://storage.googleapis.com/upload/storage/v1/b/make3400_cloudbuild/o?uploadType=media&name={file.name}', method="POST", headers=headers, data=file)
  res = {
    "name": file.name,
    "length": file.length,
    "content_type": file.content_type,
  }
  return res

# def upload_blob(source_file_name):
#   bucket_name = "make3400_cloudbuild"
#   source_file_name = local/path/to/file
#   destination_blob_name = "gs://make3400_cloudbuild"
#   storage_client = storage.Client()
#   bucket = storage_client.bucket(bucket_name)
#   blob = bucket.blob(destination_blob_name)
#   blob.upload_from_filename(source_file_name)

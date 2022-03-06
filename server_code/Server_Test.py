import anvil.server
import base64

@anvil.server.callable
def get_product(id):
#   ip = anvil.server.request.remote_address
  return f"You requested product {id}"

@anvil.server.callable
def get_blobmedia(b64str,mediatype):
    binary_content = base64.standard_b64decode(b64str)
    my_media = anvil.BlobMedia(content_type=mediatype, content=binary_content, name="audio.obj")
    return my_media

@anvil.server.callable
def send_audio_file(file, key):
  headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': file.content_type,
  }
  resp = anvil.http.request(f'https://storage.googleapis.com/upload/storage/v1/b/make3400_audiofiles/o?uploadType=media&name={file.name}', method="POST", headers=headers, data=file)
  print(resp)
  res = {
    "name": file.name,
    "length": file.length,
    "content_type": file.content_type,
  }  
  return res

@anvil.server.http_endpoint("/transcript/:id")
def insert_transcript(id):
  ip = anvil.server.request.remote_address
  data = anvil.server.request.body_json["response"]
  return {
    "status": "Okie-dokey",
    "your_ip": ip,
    "unique_id": id,
    "your_data": data
  }

@anvil.server.http_endpoint("/summary/:id")
def insert_summary(id):
  ip = anvil.server.request.remote_address
  data = anvil.server.request.body_json["response"]
  return {
    "status": "Okie-dokey",
    "your_ip": ip,
    "unique_id": id,
    "your_data": data
  }



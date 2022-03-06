import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.server

@anvil.server.callable
def get_product(id):
#   ip = anvil.server.request.remote_address
  return f"You requested product {id}"


@anvil.server.callable
def send_audio_file(file):
  headers = {
    'Authorization': 'Bearer ya29.A0ARrdaM8bXb8tguHAoIgYvCiRyXETurDnh8kNF-tYOagBvO1KLnm6arORWxSqZ_N1O_UIEvmPzmw88HOX8BTn0tIMtxoPd-z1vCfpOgSHYDsjUAK0ojRVnJDFP6qgmnwxjKxK16nv1-jzLP7IjGFVaJPgicSs',
    'Content-Type': file.content_type,
  }
  resp = anvil.http.request(f'https://storage.googleapis.com/upload/storage/v1/b/make3400_audiofiles/o?uploadType=media&name={file.name}', method="POST", headers=headers, data=file)
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



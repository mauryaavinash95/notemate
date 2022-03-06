from ._anvil_designer import Upload_And_ProcessTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

google_api_key = "ya29.A0ARrdaM8B7CTQv4aQhWIwHws-1veUzvhC9b-_vsXra9Tz021_YyGa4qQPhBoUeynjBy3ONIp_9pKePHdT5dCVXq90m9k2Q_rs6Y5dd27BOCWA-uchaQODLjIWB63xqXHyYYJWtvmWx-zOR644DHA70VnViOE0"

class Upload_And_Process(Upload_And_ProcessTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.text_box_2.text = "Lecture-"+datetime.now().strftime("%m-%d-%y-%H:%M")
    self.text_box_1.text = "Topic:Data_Structures"
  
  def form_show(self, **event_args):
    self.audio_record_1.set_lec(self.text_box_1.text, self.text_box_2.text, google_api_key)

  def file_loader_1_change(self, file, **event_args):
    res = anvil.server.call('send_audio_file', file=file, key=google_api_key)
    print("Response is", res)
    n = Notification(f"Upload successful for file: {file.name}, of size (B): {file.length}", timeout=5)
    n.show()




  




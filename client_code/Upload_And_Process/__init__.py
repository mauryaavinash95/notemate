from ._anvil_designer import Upload_And_ProcessTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class Upload_And_Process(Upload_And_ProcessTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_box_2.text = "Lecture-"+datetime.now().strftime("%m-%d-%y-%H:%M")
    self.text_box_1.text = "Topic:Data_Structures"
    
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    res = anvil.server.call('send_audio_file', file=file)
    print("Response is", res)
    n = Notification(f"Upload successful for file: {file.name}, of size (B): {file.length}", timeout=5)
    n.show()




  




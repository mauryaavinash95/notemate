from ._anvil_designer import Upload_And_ProcessTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Upload_And_Process(Upload_And_ProcessTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    pass

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    res = anvil.server.call('send_audio_file', file=file)
    print("Response is", res)
    n = Notification(f"Upload successful for file: {file.name}, of size (B): {file.length}", timeout=5)
    n.show()
#     print(f"The file's name is: {file.name}")
#     print(f"The number of bytes in the file is: {file.length}")
#     print(f"The file's content type is: {file.content_type}")
    




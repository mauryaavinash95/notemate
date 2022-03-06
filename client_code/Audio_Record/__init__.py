from ._anvil_designer import Audio_RecordTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Audio_Record(Audio_RecordTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
  def set_lec(self, lec_topic, lec_name, key):
    self.call_js('update_lec', lec_topic, lec_name, key)
    
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    self.call_js('InitLibary') # take note of the calling form
    
  def onStop(self, audio_b64_str, mediatype):
    print(audio_b64_str)
    # The following code doesn't work on client side but works on server side
    #binary_content = base64.b64decode(audio_b64_str)
    #my_media = anvil.BlobMedia(content_type="audio/ogg", content=binary_content, name="audio.ogg")
    my_media = anvil.server.call('get_blobmedia', b64str = audio_b64_str, mediatype=mediatype)
    self.audio = my_media
    self.raise_event('x_onstop')


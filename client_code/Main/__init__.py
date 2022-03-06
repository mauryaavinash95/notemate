from ._anvil_designer import MainTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Upload_And_Process import Upload_And_Process
from ..All_topics import All_topics
from ..Landing import Landing

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.clear()
    self.content_panel.add_component(Landing(), full_width_row=True)
    
    
  def button_2_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Upload_And_Process(), full_width_row=True)

  def content_panel_show(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(All_topics(), full_width_row=True)

  def button_3_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(All_topics(), full_width_row=True)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form()





from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Upload_And_Process import Upload_And_Process
from ..All_topics import All_topics

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Upload_And_Process(), full_width_row=True)
    pass

  def content_panel_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    self.content_panel.clear()
    self.content_panel.add_component(All_topics(), full_width_row=True)
    pass




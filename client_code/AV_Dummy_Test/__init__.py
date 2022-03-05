from ._anvil_designer import AV_Dummy_TestTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AV_Dummy_Test(AV_Dummy_TestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    return_value = anvil.server.call('get_product', id=1)
    alert(return_value)
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    alert(f"Button is clicked here")




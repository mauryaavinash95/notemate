from ._anvil_designer import tempTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class temp(tempTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     self.repeating_panel_1.items = [{"Name": "a", "ID": "abc"}]
    self.repeating_panel_1.items = app_tables.test.search()
    # Any code you write here will run when the form opens.

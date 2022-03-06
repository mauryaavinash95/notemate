from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    curr_visible = self.view_all_notes_card_1.visible
    self.view_all_notes_card_1.find_tags(self.button_1.tag)
    self.view_all_notes_card_1.visible = not curr_visible
    self.button_1.text = "Expand"
    if self.view_all_notes_card_1.visible:
      self.button_1.text = "Collapse"
    
    
    
    

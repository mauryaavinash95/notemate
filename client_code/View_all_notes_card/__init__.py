from ._anvil_designer import View_all_notes_cardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..View_notes_card import View_notes_card

class View_all_notes_card(View_all_notes_cardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     self.repeating_panel_1.items = app_tables.notes
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.item_template = View_notes_card
    self.repeating_panel_1.items = app_tables.notes.search()
    # Any code you write here will run when the form opens.

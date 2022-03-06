from ._anvil_designer import RepeatingCardsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from Card_Template import Card_Template

class RepeatingCards(RepeatingCardsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.item_template = Card_Template
    self.repeating_panel_1.items = app_tables.notes.search()

    # Any code you write here will run when the form opens.

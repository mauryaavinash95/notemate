from ._anvil_designer import Card_TemplateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Card_Template(Card_TemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     self.label_from.text = self.item['from']
#     self.view_notes_card_1.image_1 = self.item['Image1']
    self.view_notes_card_1.link_1 = self.item['Link1']
    self.view_notes_card_1.link_2 = self.item['Link2']
    self.view_notes_card_1.link_3 = self.item['Link3']
    
    
    
    # Any code you write here will run when the form opens.

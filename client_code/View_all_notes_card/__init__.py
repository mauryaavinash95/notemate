from ._anvil_designer import View_all_notes_cardTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from Single_Note_View import Single_Note_View

class View_all_notes_card(View_all_notes_cardTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
  
  def find_tags(self, tag):
    res = app_tables.notes.search()
    if (tag):
      res = [x for x in res if x['Tag']==tag]
    self.repeating_panel_1.items = res
    

from ._anvil_designer import All_topicsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import numpy as np

class All_topics(All_topicsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     self.repeating_panel_1.items = app_tables.notes.search()
    self.repeating_panel_1.items = np.array([{"lec_name": "BFS", "lec_count": 3}])
    
    # Any code you write here will run when the form opens.
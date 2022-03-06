from ._anvil_designer import All_topicsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class All_topics(All_topicsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    res = [x for x in app_tables.notes.search()]
    unique_topics = {}
    for x in res:
      k = x['Tag']
      unique_topics[k] = 1 if k not in unique_topics.keys() else unique_topics[k]+1
    self.data_grid_1.items = [{"lec_name": k, "lec_count": v} for k, v in unique_topics.items()]
    
    # Any code you write here will run when the form opens.
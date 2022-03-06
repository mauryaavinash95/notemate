from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    while anvil.users.get_user() is None:
      try:
        user = anvil.users.login_with_google()
      except anvil.users.AuthenticationFailed as e:
        alert("Your username/password is wrong. Please retry!")



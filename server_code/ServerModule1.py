import anvil.server

# @anvil.server.http_endpoint("/get_product/:id")
@anvil.server.callable
def get_product(id):
#   ip = anvil.server.request.remote_address
  return f"You requested product {id}"
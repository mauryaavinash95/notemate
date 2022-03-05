@anvil.server.http_endpoint("/users/:id")
def get_user(id):
  ip = anvil.server.request.remote_address
  return f"You requested user {id} from IP {ip}"
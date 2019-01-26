import smartcar
import webbrowser
#smartcar.AuthClient(client_id, client_secret, redirect_uri, scope, test_mode)
client = smartcar.AuthClient("90844701-84f0-4845-bb9f-6c060ce22216", "c489c726-b7dc-4f77-bcdf-a4584ac9cdb9", "http://localhost:8000/callback", scope=None, test_mode=False)
client.get_auth_url(force=True)

print(client.get_auth_url())
#helloooo
#ok
import requests

class APIClient:
    """A sample API client class"""
    def get_user_data(self, user_id):
        response = requests.get(f'http://api.example.com/users/{user_id}')
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Could not retrieve user data")
    
class UserService:
    """A sample service class that uses the APIClient"""
    def __init__(self, api_client):
        self.api_client = api_client # Dependency Injection

    def get_user_name(self, user_id):
        user_data = self.api_client.get_user_data(user_id)
        return user_data["name"].upper()
        
    
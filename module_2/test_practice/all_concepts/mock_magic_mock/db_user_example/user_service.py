class UserService:
    def __init__(self, db_service):
        self.db_service = db_service

    def get_user_name(self, user_id):
        user = self.db_service.get_user(user_id)
        return user["name"]
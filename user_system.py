# user_system.py

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        """
        註冊邏輯：
        1. 帳號長度必須大於 3 個字元。
        2. 帳號不能重複。
        3. 密碼長度必須大於 6 個字元。
        """
        if len(username) < 3:
            return "Error: Username too short"
        
        if username in self.users:
            return "Error: User already exists"
        
        if len(password) <= 6:
            return "Error: Password too weak"

        # 儲存使用者
        self.users[username] = password
        return "Success"

    def get_user_count(self):
        return len(self.users)
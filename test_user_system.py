# test_user_system.py
import pytest
from user_system import UserManager

# 建立一個測試用的實例
@pytest.fixture
def system():
    return UserManager()

def test_register_success(system):
    """測試正常註冊流程"""
    result = system.register_user("Alice", "password123")
    assert result == "Success"
    assert system.get_user_count() == 1

def test_username_too_short(system):
    """測試帳號過短的情況（邊界值測試）"""
    result = system.register_user("Ab", "password123")
    assert result == "Error: Username too short"
    assert system.get_user_count() == 0

def test_duplicate_registration(system):
    """測試重複註冊"""
    system.register_user("Bob", "securePass123")
    result = system.register_user("Bob", "anotherPass")
    assert result == "Error: User already exists"

def test_password_too_weak(system):
    """測試密碼強度不足"""
    result = system.register_user("Charlie", "123")
    assert result == "Error: Password too weak"
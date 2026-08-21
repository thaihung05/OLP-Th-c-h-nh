import unittest

from OLP_Init import auth


class TestRegister(unittest.TestCase):
    def setUp(self):
        auth.reset_users()

    def test_register_success(self):
        ok, message = auth.register("newuser", "123456", "new@example.com")
        self.assertTrue(ok)
        self.assertIn("newuser", auth.users)

    def test_register_duplicate_username(self):
        ok, message = auth.register("admin", "anypass", "another@example.com")
        self.assertFalse(ok)
        self.assertIn("đã tồn tại", message)

    def test_register_missing_fields(self):
        ok, message = auth.register("", "123456", "new@example.com")
        self.assertFalse(ok)


class TestLogin(unittest.TestCase):
    def setUp(self):
        auth.reset_users()

    def test_login_success(self):
        ok, message = auth.login("admin", "admin123")
        self.assertTrue(ok)

    def test_login_wrong_password(self):
        ok, message = auth.login("admin", "wrongpass")
        self.assertFalse(ok)

    def test_login_unknown_user(self):
        ok, message = auth.login("khongtontai", "123456")
        self.assertFalse(ok)

    def test_login_after_register(self):
        auth.register("newuser", "mypassword", "new@example.com")
        ok, message = auth.login("newuser", "mypassword")
        self.assertTrue(ok)


if __name__ == "__main__":
    unittest.main()

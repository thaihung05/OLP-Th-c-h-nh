import unittest

from main import app
from OLP_Init import auth


class TestRoutes(unittest.TestCase):
    def setUp(self):
        auth.reset_users()
        app.testing = True
        self.client = app.test_client()

    def test_login_page_loads(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_register_then_login(self):
        response = self.client.post(
            "/register",
            data={"username": "vidu", "password": "abcxyz", "email": "vidu@example.com"},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("vidu", auth.users)

        response = self.client.post(
            "/login",
            data={"username": "vidu", "password": "abcxyz"},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("vidu".encode(), response.data)

    def test_login_wrong_password_stays_on_login(self):
        response = self.client.post(
            "/login",
            data={"username": "admin", "password": "saipass"},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("không đúng".encode(), response.data)

    def test_dashboard_requires_login(self):
        response = self.client.get("/dashboard", follow_redirects=True)
        self.assertIn("Đăng nhập".encode(), response.data)


if __name__ == "__main__":
    unittest.main()

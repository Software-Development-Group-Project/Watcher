import unittest
from watcher import app

class WatcherTest(unittest.TestCase):

    # check for the response 200
    def test_watcher_page(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for the response 200
    def test_help_page(self):
        tester = app.test_client(self)
        response = tester.get("/help")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for the response 200
    def test_live_page(self):
        tester = app.test_client(self)
        response = tester.get("/live")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for the response 200
    def test_video_feed_page(self):
        tester = app.test_client(self)
        response = tester.get("/video_feed")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for the response 200
    def test_member_page(self):
        tester = app.test_client(self)
        response = tester.get("/member")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for the response 200
    def test_add_member_page(self):
        tester = app.test_client(self)
        response = tester.get("/add")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for the response 200
    def test_view_page(self):
        tester = app.test_client(self)
        response = tester.get("/view")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for the response 200
    def test_delete_page(self):
        tester = app.test_client(self)
        response = tester.get("/delete")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for the response 200
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check login credentials
    # jenoshanan 123
    # def test_login_credentials(self):
    #     tester = app.test_client(self)
    #     response = tester.post("/loginValidation", data=dict(username="jenoshanan", password="123", folow_redirects=True))
    #     self.assertIn(b'Welcome to Watcher', response.data)


if __name__ == "__main__":
    unittest.main()


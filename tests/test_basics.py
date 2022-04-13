# imports
from flask import current_app
from cafes import create_app, db
import unittest


# basic test for the application
class BasicTests(unittest.TestCase):
    def setUp(self) -> None:
        # create an app context
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

        # init the database
        db.create_all()

    def tearDown(self) -> None:
        # destroy the database
        db.session.remove()
        db.drop_all()

        # pop the app context
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])


if __name__ == '__main__':
    unittest.main()

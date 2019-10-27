from unittest import TestCase

from app.service.score_generator import ScoreGenerator
from run import app


class TestRun(TestCase):

    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.sut = app.test_client()
        self.score_generator = ScoreGenerator.load_default()

    def test_landing_page_should_return_fine(self):
        # act
        response = self.sut.get("/")

        # assert
        self.assertEqual(response.status_code, 200)

import shutil
from unittest import TestCase, mock

import os

from app.service.file_operator import FileOperator
from app.service.score_generator import ScoreGenerator
from run import app, form_post


class TestRun(TestCase):

    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.sut = app.test_client()
        self.score_generator = ScoreGenerator.load_default()
        self.score_generator.run = mock.MagicMock()
        self.score_generator.run.return_value = None

        self.file_operator = mock.MagicMock(FileOperator)
        self.file_operator.load_default = mock.MagicMock()
        self.file_operator.load_default.return_value = mock.MagicMock()

        self.test_workdir = os.path.join(os.path.dirname(__file__), "test_workdir")

    def test_should_call_file_operator_load_default_once_when_form_post(self):
        # act
        form_post("testing",
                  self.score_generator,
                  self.file_operator)

        # assert
        self.file_operator.load_default.assert_called_once()

    def test_should_call_score_generator_run_with_correct_parameters_when_form_post(self):
        # act
        form_post("testing",
                  self.score_generator,
                  self.file_operator)

        # assert
        self.score_generator.run.assert_called_once_with("testing", self.file_operator.load_default.return_value)

    def test_should_return_default_text_when_output_filepath_is_none(self):
        # act
        response = form_post("testing",
                             self.score_generator,
                             self.file_operator)

        # assert
        self.assertEqual(response, "Something wrong...please follow correct lilypond syntax for input text")

    def tearDown(self):
        if os.path.isdir(self.test_workdir):
            shutil.rmtree(self.test_workdir)

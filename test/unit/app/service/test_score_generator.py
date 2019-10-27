from unittest import TestCase, mock
import os
import shutil

from app.service.file_operator import FileOperator
from app.service.score_generator import ScoreGenerator
from config import Config


class TestScoreGenerator(TestCase):
    def setUp(self) -> None:
        self.sut = ScoreGenerator
        self.test_workdir = os.path.join(os.path.dirname(__file__), "test_workdir")

        self.test_file_operator = mock.MagicMock(FileOperator)
        self.test_file_operator.workdir = self.test_workdir
        self.test_file_operator.input_filepath = "test/filepath/that/doesnt/exist"
        self.test_file_operator.output_filepath = "test/filepath/that/doesnt/exist"

        os.makedirs(self.test_workdir, exist_ok=True)

        with open(os.path.join(os.path.dirname(__file__), "../../../common/harry_potter_intro.ly"), "r") as f:
            self.good_test_input = f.read()

    def test_should_return_instance_with_specified_lilypond_path_when_init(self):
        # act
        temp_instance = self.sut("/path/to/lilypond")

        # assert
        self.assertIsInstance(temp_instance, ScoreGenerator)
        self.assertEqual(temp_instance._lilypond_path, "/path/to/lilypond")

    def test_should_return_instance_with_defaults_when_load_default(self):
        # act
        temp_instance = self.sut.load_default()

        # assert
        self.assertIsInstance(temp_instance, ScoreGenerator)
        self.assertEqual(temp_instance._lilypond_path, Config.lilypond_path)

    def test_should_call_write_text_to_file_when_run(self):
        # arrange
        temp_instance = self.sut.load_default()
        self.test_file_operator.write_text_to_file = mock.MagicMock()

        # act
        temp_instance.run("testing", self.test_file_operator)

        # assert
        self.test_file_operator.write_text_to_file.assert_called_once_with("testing")

    def test_should_call_create_workdir_when_run(self):
        # arrange
        temp_instance = self.sut.load_default()
        self.test_file_operator.create_workdir = mock.MagicMock()

        # act
        temp_instance.run("testing", self.test_file_operator)

        # assert
        self.test_file_operator.create_workdir.assert_called_once()

    def test_should_create_workdir_when_run(self):
        # arrange
        temp_instance = self.sut(Config.lilypond_path)

        # act
        temp_instance.run("testing", FileOperator.load_default())

        # assert
        self.assertTrue(os.path.isdir(self.test_workdir))

    def test_should_create_output_file_when_run_with_correct_input(self):
        # arrange
        temp_instance = self.sut(Config.lilypond_path)

        # act
        output = temp_instance.run(self.good_test_input, FileOperator.load_default())

        # assert
        self.assertIsNotNone(output)
        self.assertIsInstance(output, str)

    def test_should_return_output_none_when_run_with_incorrect_input(self):
        # arrange
        temp_instance = self.sut(Config.lilypond_path)

        # act
        output = temp_instance.run("testing", FileOperator.load_default())

        # assert
        self.assertIsNone(output)

    def tearDown(self):
        if os.path.isdir(self.test_workdir):
            shutil.rmtree(self.test_workdir)
        if os.path.isdir(Config.workdir):
            shutil.rmtree(Config.workdir)

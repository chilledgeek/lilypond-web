from unittest import TestCase
import os
import shutil

from app.service.file_operator import FileOperator
from config import Config


class TestFileOperator(TestCase):
    def setUp(self) -> None:
        self.sut = FileOperator
        self.test_workdir = os.path.join(os.path.dirname(__file__), "test_workdir")

    def test_should_return_instance_with_input_output_filepaths_not_none_when_init(self):
        # act
        temp_instance = self.sut()

        # assert
        self.assertIsNotNone(temp_instance.input_filepath)
        self.assertIsNotNone(temp_instance.output_filepath)

    def test_should_return_instance_with_specified_workdir_populated_when_init_with_parameters(self):
        # act
        temp_instance = self.sut("whatever")

        # assert
        self.assertIsInstance(temp_instance, FileOperator)
        self.assertEqual(temp_instance.workdir, "whatever")

    def test_should_return_instance_with_default_workdir_when_init_without_parameters(self):
        # act
        temp_instance = self.sut()

        # assert
        self.assertIsInstance(temp_instance, FileOperator)
        self.assertEqual(temp_instance.workdir, ".")

    def test_should_return_instance_with_defaults_when_load_default(self):
        # act
        temp_instance = self.sut.load_default()

        # assert
        self.assertIsInstance(temp_instance, FileOperator)
        self.assertEqual(temp_instance.workdir, Config.workdir)
        self.assertTrue(temp_instance.input_filepath.startswith(Config.workdir))
        self.assertTrue(temp_instance.output_filepath.startswith(Config.workdir))

    def test_should_write_correct_text_to_file_in_correct_location_when_call_write_text_to_file(self):
        # arrange
        temp_instance = self.sut(self.test_workdir)
        os.makedirs(self.test_workdir, exist_ok=True)
        input_text = "whatever gets written to input file"

        # act
        temp_instance.write_text_to_file("whatever gets written to input file")

        # assert
        with open(temp_instance.input_filepath, "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, input_text)

    def test_correct_workdir_exists_when_create_workdir(self):
        # arrange
        temp_instance = self.sut(workdir=self.test_workdir)

        # act
        temp_instance.create_workdir()

        # assert
        self.assertTrue(os.path.isdir(self.test_workdir))

    def test_input_file_should_be_removed_when_remove_input_file(self):
        # arrange
        temp_instance = self.sut(workdir=self.test_workdir)
        os.makedirs(self.test_workdir, exist_ok=True)
        with open(temp_instance.input_filepath, "w") as f:
            f.write("whatever!!! it should be deleted anyway")

        # act
        temp_instance.remove_input_file()

        # assert
        self.assertFalse(os.path.isfile(temp_instance.input_filepath))

    def tearDown(self):
        """
        Remove test and default workdir
        :return:
        """
        if os.path.isdir(self.test_workdir):
            shutil.rmtree(self.test_workdir)
        if os.path.isdir(Config.workdir):
            shutil.rmtree(Config.workdir)

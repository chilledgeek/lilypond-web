import os
import subprocess
from typing import Union

from app.service.file_operator import FileOperator
from config import Config


class ScoreGenerator:
    """
    Provide interface to access lilypond functionality
    """

    def __init__(self, lilypond_path):
        self._lilypond_path = lilypond_path

    @staticmethod
    def load_default():
        """
        :return: ScoreGenerator instance with loaded default values
        """
        score_generator = ScoreGenerator(Config.lilypond_path)
        return score_generator

    def run(self,
            input_text: str,
            file_operator: FileOperator) -> Union[str, None]:
        """
        Writes text to file and runs lilypond to generate output pdf file
        file_operator needs to be initiated everytime this is called to get a unique timestamp for input/output tracking
        :param input_text: text received input UI input
        :param file_operator: FileOperator object that stores info and functions for specific file operations
        :return: output_filepath
        """
        file_operator.create_workdir()
        file_operator.write_text_to_file(input_text)
        os.chdir(file_operator.workdir)

        subprocess.run([self._lilypond_path, file_operator.input_filepath])

        file_operator.remove_input_file()

        if os.path.isfile(file_operator.output_filepath):
            output = file_operator.output_filepath
        else:
            output = None

        return output

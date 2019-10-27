import os
from datetime import datetime

from config import Config


class FileOperator:

    def __init__(self,
                 workdir: str = ".",
                 ):
        self.workdir = workdir
        self.input_filepath = os.path.join(self.workdir,
                                           f"request_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')}.ly")
        self.output_filepath = f"{self.input_filepath[:-3]}.pdf"

    @staticmethod
    def load_default():
        file_operator = FileOperator(Config.workdir)
        return file_operator

    def write_text_to_file(self, input_text: str) -> None:
        with open(self.input_filepath, "w") as f:
            f.write(input_text)
        f.close()

    def create_workdir(self) -> None:
        if not os.path.isdir(self.workdir):
            os.makedirs(self.workdir, exist_ok=True)

    def remove_input_file(self):
        if os.path.isfile(self.input_filepath):
            os.remove(self.input_filepath)

import os


class Config:
    workdir = os.path.join(os.path.dirname(__file__), "workdir") if os.getenv("WORKDIR") is None else os.environ[
        "WORKDIR"]
    lilypond_path = "/lilypond/bin/lilypond" if os.getenv("LILYPOND_PATH") is None else os.environ[
        "LILYPOND_PATH"]

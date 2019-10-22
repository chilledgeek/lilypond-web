import os


class Config:
    workdir = os.path.join(os.path.dirname(__file__), "workdir") if os.environ["WORKDIR"] is None else os.environ[
        "WORKDIR"]

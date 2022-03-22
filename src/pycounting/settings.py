""" Module for holding the settings for pycounting """

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Global Settings"""

    test: str

    class Config:
        """Used to grab specific settings form settings.txt file"""

        env_file = "settings.txt"
        env_file_encoding = "utf-8"

    @classmethod
    def setup_settings(cls):
        """Classmethod to interactivly create a settings.txt file"""
        with open("settings.txt", "w") as file:
            for var, info in cls.__dict__["__fields__"].items():
                value = input("Set value for {var}")
                file.write(f"{var}={value}\n")

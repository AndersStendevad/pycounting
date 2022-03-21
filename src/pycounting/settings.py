from pydantic import BaseSettings


class Settings(BaseSettings):
    test: str 

    class Config:
        env_file = 'settings.txt'
        env_file_encoding = 'utf-8'

    @classmethod
    def setup_settings(cls):
        with open("settings.txt", "w") as file:
            for var in dict(cls).keys():
                value = input("Set value for {var}")
                file.write(f"{var}={value}\n")

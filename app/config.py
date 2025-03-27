from getpass import getuser

class Settings:
    def __init__(self):
        self.db_url = f"postgresql://{getuser()}@localhost:5432/tron_db"
        self.tron_net = "shasta"

settings = Settings()
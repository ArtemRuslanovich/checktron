class Settings:
    def __init__(self):
        self.db_url: str = "postgresql://user:pass@localhost:5432/tron_test_db"
        self.tron_net: str = "shasta"

setting = Settings()
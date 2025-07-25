class BaseExpert:
    def analyze(self, query: str) -> dict:
        raise NotImplementedError("Each expert must implement the analyze method")

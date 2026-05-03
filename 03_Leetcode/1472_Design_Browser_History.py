class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_idx = 0

    def visit(self, url: str) -> None:
        self.current_idx += 1
        self.history = self.history[0:self.current_idx]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.current_idx = max(0, self.current_idx - steps)
        return self.history[self.current_idx]

    def forward(self, steps: int) -> str:
        self.current_idx = min(len(self.history) - 1, self.current_idx + steps)
        return self.history[self.current_idx]
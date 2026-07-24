class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        self.patience = patience
        self.min_delta = min_delta
        self.best = float("-inf")
        self.bad_epochs = 0
        
    def update(self, score):
        if score > self.best + self.min_delta:
            self.best = score
            self.bad_epochs = 0
        else:
            self.bad_epochs += 1
        return self.bad_epochs >= self.patience
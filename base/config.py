class Config:
    def __init__(self) -> None:
        super().__init__()
        self.gpu = False
        self.device = "cpu"
        self.conf = {}

    def set(self, setting, value):
        self.conf[setting] = value

    def get(self, setting):
        self.conf[setting]

    @property
    def device(self):
        return self.device

    def use_gpu(self, device):
        self.device = device

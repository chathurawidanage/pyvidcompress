from abc import ABC, abstractmethod
from base.config import Config
import cv2
from base.tdv import Tdv


def file_to_tensor(file):
    vidcap = cv2.VideoCapture(file)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success, image = vidcap.read()
    count = 0
    frames = []
    while success:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        frames.append(image)
        count += 1
        success, image = vidcap.read()

    frames = np.stack(frames, axis=0)
    return frames, fps


class Encoder(ABC):
    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config

    @abstractmethod
    def encode_tensor(self, tensor) -> Tdv:
        pass

    def encode_file(self, src_file) -> Tdv:
        return self.encode_tensor(file_to_tensor(src_file))

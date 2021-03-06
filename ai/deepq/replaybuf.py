from random import choices
from typing import List


class ReplayBuffer:
    def __init__(self, config: dict[str, int]) -> None:
        self.buffer: List[List[object]] = []

        self.maxSize: int = config["rbSize"]
        self.batchSize: int = config["batchSize"]

    # append new experience to replay buffer
    def append(self, s: List[List[int]], a: int, r: float, t: int, nS: List[List[int]]) -> None:
        # remove earliest experience if full
        if len(self.buffer) == self.maxSize:
            del self.buffer[0]

        self.buffer.append([s, a, r, t, nS])

    # return random sample of experiences
    def getSample(self) -> List[List[object]]:
        return choices(self.buffer, k=self.batchSize)

    # check if buffer is ready for minibatch update
    def isReady(self):
        return len(self.buffer) > self.batchSize

from typing import List
import numpy as np


class Adam:
    def __init__(self, layerSizes: List[int], config: dict[str, float]):
        # initialise hyperparams
        self.layerSizes: List[int] = layerSizes
        self.stepSize: float = config["stepSize"]
        self.bM: float = config["bM"]
        self.bV: float = config["bV"]
        self.bMProd: float = self.bM
        self.bVProd: float = self.bV
        self.epsilon: float = config["epsilon"]

        # initialise mean variance value storage
        self.m = [dict() for i in range(1, len(self.layerSizes))]
        self.v = [dict() for i in range(1, len(self.layerSizes))]
        for i in range(0, len(self.layerSizes) - 1):
            self.m[i]["W"] = np.zeros((self.layerSizes[i], self.layerSizes[i + 1]))
            self.m[i]["b"] = np.zeros((1, self.layerSizes[i + 1]))

            self.v[i]["W"] = np.zeros((self.layerSizes[i], self.layerSizes[i + 1]))
            self.v[i]["b"] = np.zeros((1, self.layerSizes[i + 1]))

    # update values with the adam optimizer
    def updateVals(self, vals: List[dict[str, object]], tdUpdate: List[dict[str, object]]):
        for i in range(len(vals)):
            for param in vals[i].keys():
                self.m[i][param] = self.bM * self.m[i][param] + (1 - self.bM) * tdUpdate[i][param]
                self.v[i][param] = self.bV * self.v[i][param] + (1 - self.bV) * tdUpdate[i][param] ** 2

                mHat = self.m[i][param] / (1 - self.bMProd)
                vHat = self.v[i][param] / (1 - self.bVProd)

                vals[i][param] += self.stepSize * mHat / (np.sqrt(vHat) + self.epsilon)

        self.bMProd *= self.bM
        self.bVProd *= self.bV

        return vals

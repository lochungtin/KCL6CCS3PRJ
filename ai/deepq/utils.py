from typing import List
import numpy as np

from ai.deepq.adam import Adam
from ai.deepq.neuralnet import NeuralNet


class NNUtils:
    # ===== batched optimisation for training =====
    def optimiseNN(tN: NeuralNet, cN: NeuralNet, replays: List[object], gamma: float, tau: float, adam: Adam):
        # explode replays into separate lists
        states, actions, rewards, terminals, nStates = map(list, zip(*replays))

        states = np.concatenate(states)
        rewards = np.array(rewards)
        terminals = np.array(terminals)
        nStates = np.concatenate(nStates)
        minibatchSize = states.shape[0]

        # get TD error of network from replays
        tdError = NNUtils.getTDError(tN, cN, states, actions, rewards, terminals, nStates, gamma, tau)

        # create delta matrix for batch td update
        indices = np.arange(minibatchSize)

        deltaMatrix = np.zeros((minibatchSize, tN.outSize))
        deltaMatrix[indices, actions] = tdError

        # perform td update on target network
        tdUpdate = NNUtils.backpropagation(tN, states, deltaMatrix)

        # pass td update to adam optimiser to get a new set of values for the target network
        tN.setVals(adam.updateVals(tN.getVals(), tdUpdate))

    # get TD error from replays
    def getTDError(tN: NeuralNet, cN: NeuralNet, s, a, r, t, nS, gamma: float, tau: float):
        nextQVals = cN.predict(nS)
        probsVals = NNUtils.softmax(nextQVals, tau)

        vNVector = np.sum(nextQVals * probsVals, axis=1) * (1 - t)

        targetVector = r + gamma * vNVector

        curQVals = tN.predict(s)
        indices = np.arange(curQVals.shape[0])
        qVector = curQVals[indices, a]

        return targetVector - qVector

    # backpropagation for TD error and minibatch pretraining
    def backpropagation(tN: NeuralNet, X: List[List[float]], Y: List[List[float]]) -> List[dict[str, object]]:
        layers: int = len(tN.vals)
        gradient: List[dict[str, object]] = [dict() for i in range(layers)]

        A = [X]
        dZ = []
        for i in range(layers):
            z = np.dot(A[i], tN.vals[i]["W"]) + tN.vals[i]["b"]
            a = np.maximum(z, 0)

            # store activition values of each layer
            A.append(a)

            # store dRelu values
            dZ.append((z > 0).astype(float))

        # calculate deltas of each layer
        deltas = [None for i in range(layers)]
        deltas[layers - 1] = Y
        for i in range(layers - 2, -1, -1):
            deltas[i] = np.dot(deltas[i + 1], tN.vals[i + 1]["W"].T) * dZ[i]

        # calculate gradient of each weight matrix and bias
        minibatchSize: int = X.shape[0]
        for i in range(layers):
            gradient[i]["W"] = np.dot(A[i].T, deltas[i]) * minibatchSize
            gradient[i]["b"] = np.sum(deltas[i], axis=0, keepdims=True) / minibatchSize

        return gradient

    # softmax function for exploration / exploitation actions
    def softmax(qVals: List[float], tau: float) -> List[float]:
        pref = qVals / tau
        maxPref = np.max(pref, axis=1).reshape((-1, 1))

        ePref = np.exp(pref - maxPref)
        sumEPref = np.sum(ePref, axis=1)

        return (ePref / sumEPref.reshape((-1, 1))).squeeze()

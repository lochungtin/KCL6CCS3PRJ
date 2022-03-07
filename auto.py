from tkinter import Tk
import _thread

from agents.pacman import PacmanDQLAgent
from agents.blinky import BlinkyClassicAgent
from agents.inky import InkyClassicAgent
from agents.clyde import ClydeClassicAgent
from agents.pinky import PinkyClassicAgent
from ai.deepq.neuralnet import NeuralNet
from ai.neat.genome import Genome
from ai.neat.utils import GenomeUtils
from game.game import Game
from gui.controller import TimeController
from gui.display import Display
from utils.printer import printPacmanPerfomance


class App:
    def __init__(self, gameConfig: dict[str, object]) -> None:
        self.game = Game(
            gameConfig["agents"]["pacman"],
            blinky=gameConfig["agents"]["blinky"],
            inky=gameConfig["agents"]["inky"],
            clyde=gameConfig["agents"]["clyde"],
            pinky=gameConfig["agents"]["pinky"],
            enablePwrPlt=gameConfig["enablePwrPlt"],
        )

        self.pellets: int = 0
        self.kills: int = 0
        self.stationary: int = 0

        self.main: Tk = Tk()
        self.main.title("Auto Pacman Game Viewer")

        self.display: Display = Display(self.main)
        self.display.newGame(self.game)

        self.tc: TimeController = TimeController(
            gameConfig["gameSpeed"], self.nextStep)

        _thread.start_new_thread(self.tc.start, ())

    def nextStep(self):
        gameover, won, atePellet, atePwrPlt, ateGhost = self.game.nextStep()

        if ateGhost: 
            self.kills += 1

        if not self.game.pacman.moved:
            self.stationary += 1

        if gameover or won:
            printPacmanPerfomance(0, self.game)

            self.tc.end()
            self.main.destroy()

        self.display.rerender()

    def run(self) -> None:
        self.main.mainloop()


# load neural network from config json
def loadNeuralNet(parentFolder: str, prefix: str, ep: int) -> NeuralNet:
    return NeuralNet.load("./{}/{}/rl_nnconf_ep{}.json".format(parentFolder, prefix, ep))


# load genome from config json
def loadGenome(parentFolder: str, prefix: str, gen: int) -> Genome:
    return GenomeUtils.load("./{}/{}/ga_nnconf_ep{}.json".format(parentFolder, prefix, gen))

# 7500

if __name__ == "__main__":
    gameConfig: dict[str, object] = {
        "agents": {
            "pacman": PacmanDQLAgent(loadNeuralNet("out", "RL0703_2025", 2500)),
            "blinky": BlinkyClassicAgent(),
            "inky": None,
            "clyde": None,
            "pinky": PinkyClassicAgent(),
        },
        "enablePwrPlt": True,
        "gameSpeed": 0.05,
    }

    App(gameConfig).run()

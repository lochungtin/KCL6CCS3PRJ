import numpy as np

from agents.base.base import GhostAgent
from agents.blinky import BlinkyClassicAgent, BlinkyClassicAggrAgent, BlinkyDQLAgent, BlinkyMDPAgent
from agents.clyde import ClydeClassicAgent, ClydeClassicAggrAgent
from agents.inky import InkyClassicAgent, InkyClassicAggrAgent, InkyStaticAgent
from agents.pacman import PacmanDQLAgent, PacmanDQLTAgent, PacmanMDPAgent, PlayableAgent
from agents.pinky import PinkyClassicAgent, PinkyClassicAggrAgent
from data.data import AGENT_CLASS_TYPE, REP
from game.game import Game
from utils.file import loadNeuralNetT

# create new game based on agent config
def newGame(agents: dict[str, int], enablePwrPlt: bool, neuralnets: dict[str, str], genomes: dict[str, str]) -> Game:
    # create ai pacman agent
    if agents[REP.PACMAN] == AGENT_CLASS_TYPE.CTRL:
        pacman: PlayableAgent = PlayableAgent()
    elif agents[REP.PACMAN] == AGENT_CLASS_TYPE.SMDP:
        pacman: PacmanMDPAgent = PacmanMDPAgent()
    elif agents[REP.PACMAN] == AGENT_CLASS_TYPE.DQLT:
        pacman: PacmanDQLTAgent = PacmanDQLTAgent()
    else:
        pacman: PacmanDQLAgent = PacmanDQLAgent(loadNeuralNetT(neuralnets[REP.PACMAN]))

    # create ai blinky agent
    blinky: GhostAgent = None
    if agents[REP.BLINKY] == AGENT_CLASS_TYPE.OGNL:
        blinky = BlinkyClassicAgent()
    elif agents[REP.BLINKY] == AGENT_CLASS_TYPE.AGGR:
        blinky = BlinkyClassicAggrAgent()
    elif agents[REP.BLINKY] == AGENT_CLASS_TYPE.SMDP:
        blinky = BlinkyMDPAgent()
    elif agents[REP.BLINKY] == AGENT_CLASS_TYPE.GDQL:
        blinky = BlinkyDQLAgent(loadNeuralNetT(neuralnets[REP.BLINKY]))

    # create secondary ghost ai agent
    inky: GhostAgent = None
    clyde: GhostAgent = None
    pinky: GhostAgent = None

    # check for random generation flag
    if agents["secondary"] == AGENT_CLASS_TYPE.RAND:
        ghostIndex: int = np.random.randint(0, 3)
        typeIndex: int = np.random.randint(0, 2)
        if "randType" in agents:
            typeIndex = agents["randType"]

        if ghostIndex == 0:
            if typeIndex == AGENT_CLASS_TYPE.OGNL:
                inky = InkyClassicAgent()
            else:
                inky = InkyClassicAggrAgent()

        elif ghostIndex == 1:
            if typeIndex == AGENT_CLASS_TYPE.OGNL:
                clyde = ClydeClassicAgent()
            else:
                clyde = ClydeClassicAggrAgent()

        else:
            if typeIndex == AGENT_CLASS_TYPE.OGNL:
                pinky = PinkyClassicAgent()
            else:
                pinky = PinkyClassicAggrAgent()
    else:
        # create ai inky agent
        if agents["secondary"][REP.INKY] == AGENT_CLASS_TYPE.OGNL:
            inky = InkyClassicAgent()
        elif agents["secondary"][REP.INKY] == AGENT_CLASS_TYPE.AGGR:
            inky = InkyClassicAggrAgent()
        elif agents["secondary"][REP.INKY] == AGENT_CLASS_TYPE.STTC:
            inky = InkyStaticAgent()

        # create ai clyde agent
        if agents["secondary"][REP.CLYDE] == AGENT_CLASS_TYPE.OGNL:
            clyde = ClydeClassicAgent()
        elif agents["secondary"][REP.CLYDE] == AGENT_CLASS_TYPE.AGGR:
            clyde = ClydeClassicAggrAgent()
        elif agents["secondary"][REP.CLYDE] == AGENT_CLASS_TYPE.STTC:
            clyde = ClydeClassicAgent()

        # create ai pinky agent
        if agents["secondary"][REP.PINKY] == AGENT_CLASS_TYPE.OGNL:
            pinky = PinkyClassicAgent()
        elif agents["secondary"][REP.PINKY] == AGENT_CLASS_TYPE.AGGR:
            pinky = PinkyClassicAggrAgent()
        elif agents["secondary"][REP.PINKY] == AGENT_CLASS_TYPE.STTC:
            pinky = PinkyClassicAgent()

    return Game(pacman, blinky, inky, clyde, pinky, enablePwrPlt)

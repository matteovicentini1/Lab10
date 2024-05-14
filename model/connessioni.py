from dataclasses import dataclass

@dataclass
class Connect:
    dyad:int
    state1no:int
    state1ab:str
    state2no:int
    state2ab:str
    year:int
    conttype:int
    version:float


    def __hash__(self):
        return hash(self.dyad)
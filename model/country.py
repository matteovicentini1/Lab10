from dataclasses import dataclass

@dataclass
class Country:
    StateAbb:str
    CCode:int
    Nome :str


    def __hash__(self):
        return hash(self.CCode)

    def __str__(self):
        return f'{self.Nome}'
# Abstração e Herança com dataclasses?
# Tem enum no python?
# dataclasses com valor default dao erro?
# para que serve o super()?


# OBS: tem o arquivo band_12.py que usa este arquivo

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List

# Enumeraçao / Enumerador
class InstrumentKind(str, Enum):
    string = "string"
    wind = "wind"
    drums = "drums"

# Classe Abstrata
class ABCInstrument(ABC):

    @abstractmethod
    def play(self):
        pass

# Dataclass com mixin
@dataclass
class DataIntrumentMixin:
    name : str
    sound: str
    kind: InstrumentKind
    colors: List[str] = field(default_factory=list)

# Herança Múltipla
class Instrument(DataIntrumentMixin, ABCInstrument):
    pass

# Subclasses concretas
@dataclass
class Guitar(Instrument):
    n_strings: int = 6
    sound: str = "Trom Trom"
    kind: InstrumentKind = InstrumentKind.string
    colors: List[str] = field(default_factory=lambda: ["black", "white"] )

    def play(self):
        return self.sound
    
@dataclass
class EletricGuitar(Guitar):
    sound: str = "wah wah wah"

    def play(self, distortion="wave"):
        return_from_base_class = super().play()
        if distortion == "wave":
            return "~~~~".join(return_from_base_class.split())
        return return_from_base_class

# Subclasses concretas 
@dataclass
class Flute(Instrument):
    sound: str = "Tooooot"
    kind: InstrumentKind = InstrumentKind.wind
    colors: List[str] = field(default_factory=lambda: ["silver", "gold"] )

    def play(self):
        return self.sound

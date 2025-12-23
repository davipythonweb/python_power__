# Abstração e Herança com dataclasses?
# Tem enum no python?
# dataclasses com valor default dao erro?

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
    sound: str = "Trom Trom"
    kind: InstrumentKind = InstrumentKind.string

    def play(self):
        return self.sound

# Subclasses concretas 
@dataclass
class Flute(Instrument):
    sound: str = "Tooooot"
    kind: InstrumentKind = InstrumentKind.wind

    def play(self):
        return self.sound

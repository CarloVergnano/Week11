from model.object import Object
from dataclasses import dataclass


@dataclass
class Connessione:
    o1 : Object
    o2 : Object
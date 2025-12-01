from dataclasses import dataclass
@dataclass
class Object:
    _object_id : int
    _object_name : str
    _title : str



    def __str__(self):
        return f"{self._object_name} {self._object_id} {self._title}"

    #Serve per portare l'oggetto come nodo del grafo
    def __hash__(self):
        return hash(self._object_id)


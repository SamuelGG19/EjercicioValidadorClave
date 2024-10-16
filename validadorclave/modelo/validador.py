from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) >= self._longitud_esperada:
            return True
        else:
            return False


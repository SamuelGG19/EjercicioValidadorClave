from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) >= self._longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        if clave.isupper():
            return True
        else:
            return False

    def _contiene_minuscula(self, clave: str) -> bool:
        if clave.islower():
            return True
        else:
            return False

    def _contiene_numero(self, clave: str) -> bool:
        if clave.isdigit():
            return True
        else:
            return False

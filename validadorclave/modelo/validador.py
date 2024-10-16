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

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):

    def contiene_caracter_especial(self, clave: str) -> bool:
        if ("@" in clave) or ("_" in clave) or ("#" in clave) or ("$" in clave) or ("%" in clave):
            return True
        else:
            return False

    def es_valida(self, clave: str) -> bool:
        pass

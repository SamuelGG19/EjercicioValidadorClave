from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self._longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True

        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True

        return False

    def _contiene_numero(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True

        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self, _longitud_esperada: int):
        super().__init__(_longitud_esperada)
        self._longitud_esperada: int = 8

    def contiene_caracter_especial(self, clave: str) -> bool:
        if ("@" in clave) or ("_" in clave) or ("#" in clave) or ("$" in clave) or ("%" in clave):
            return True
        else:
            return False

    def es_valida(self, clave: str) -> bool:
        if self._validar_longitud(clave):
            if self._contiene_mayuscula(clave):
                if self._contiene_minuscula(clave):
                    if self._contiene_numero(clave):
                        if self.contiene_caracter_especial(clave):
                            return True
                        else:
                            raise NoTieneCaracterEspecialError()
                    else:
                        raise NoTieneNumeroError()
                else:
                    raise NoTieneLetraMinusculaError()
            else:
                raise NoTieneLetraMayusculaError()
        else:
            raise NoCumpleLongitudMinimaError()


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, _longitud_esperada: int):
        super().__init__(_longitud_esperada)
        self._longitud_esperada: int = 6

    def contiene_calisto(self, clave: str) -> bool:
        pass
        # if "calisto" in clave.lower():
        #     return True
        # else:
        #     return False

    def es_valida(self, clave: str) -> bool:
        if self._validar_longitud(clave):
            if self._contiene_numero(clave):
                if self.contiene_calisto(clave):
                    return True
                else:
                    raise NoTienePalabraSecretaError()
            else:
                raise NoTieneNumeroError()
        else:
            raise NoCumpleLongitudMinimaError()


class Validador:

    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)

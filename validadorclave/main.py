from validadorclave.modelo.validador import ReglaValidacion, Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


def validar_clave(clave: str, reglas: list[ReglaValidacion]):
    for regla in reglas:
        try:
            Validador.es_valida(clave)
        except NoCumpleLongitudMinimaError:
            if regla is ReglaValidacionGanimedes:
                print("Error: ReglaValidacionGanimedes: La clave debe tener una longitud de más de 8 caracteres")
            elif regla is ReglaValidacionCalisto:
                print("Error: ReglaValidacionCalisto: La clave debe tener una longitud de más de 6 caracteres")
        except NoTieneLetraMayusculaError:
            print("Error: ReglaValidacionGanimedes: La clave debe tener al menos una letra mayúscula")
        except NoTieneLetraMinusculaError:
            print("Error: ReglaValidacionGanimedes: La clave debe tener al menos una letra minúscula")
        except NoTieneNumeroError:
            if regla is ReglaValidacionGanimedes:
                print("Error: ReglaValidacionGanimedes: La clave debe tener al menos un número")
            elif regla is ReglaValidacionCalisto:
                print("Error: ReglaValidacionCalisto: La clave debe tener al menos un número")
        except NoTieneCaracterEspecialError:
            print("Error: ReglaValidacionGanimedes: La clave debe tener al menos un caracter especial (@, _, #, $ o %).")
        except NoTienePalabraSecretaError:
            print("Error: ReglaValidacionCalisto: La palabra calisto debe estar escrita con al menos dos letras en mayúscula")
        else:
            print("La clave es válida!")

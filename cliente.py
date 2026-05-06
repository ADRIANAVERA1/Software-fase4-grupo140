from excepciones import ClienteError

class Cliente:
    def __init__(self, nombre, documento):

        # Validamos el nombre
        if not nombre or not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        # Validamos el documento (solo números y mínimo 5 dígitos)
        if not str(documento).isdigit() or len(str(documento)) < 5:
            raise ClienteError("Documento inválido")

        self.__nombre = nombre
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

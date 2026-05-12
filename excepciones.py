class ErrorSoftwareFJ(Exception):
    """Clase base para todos los errores del sistema Software FJ"""
    pass

class ClienteError(ErrorSoftwareFJ):
    """Se lanza cuando hay problemas con los datos del cliente"""
    pass

class ServicioError(ErrorSoftwareFJ):
    """Se lanza cuando un servicio no está disponible o es inválido"""
    pass

class ReservaError(ErrorSoftwareFJ):
    """Se lanza cuando falla una reserva (ej: fecha ocupada)"""
    pass
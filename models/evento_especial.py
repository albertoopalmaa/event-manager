from evento import Evento


class EventoEspecial:
    def __init__(self, nombre, fecha, descripcion, ubicacion):
        super().__init__(nombre, fecha, descripcion)
        self.ubicacion = ubicacion

    def to_dic(self):
        datos = super().to_dic()
        datos["ubicacion"] = self.ubicacion
        return datos

    def __str__(self):
        return f"{self._nombre} - {self._fecha} : {self._descripcion} (Ubicación: {self._ubicacion})"

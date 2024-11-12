class Evento:
    def __init__(self, nombre, fecha, descripcion):
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion

    def to_dic(self):
        return {
            "nombre": self._nombre,
            "fecha": self._fecha,
            "description": self._descripcion,
        }

    def __str__(self):
        return f"{self.nombre} - {self.fecha} : {self.descripcion}"

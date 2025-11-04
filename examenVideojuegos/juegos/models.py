from django.db import models

class Estudio(models.Model):
    nombre = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()
    def __str__(self):
        return self.nombre

class Sede(models.Model):
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.ciudad} - {self.pais}"

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} ({self.fabricante})"

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    estudio_desarrollo = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    plataformas = models.ManyToManyField('Plataforma', through='VideojuegoPlataforma')
    def __str__(self):
        return self.titulo

class VideojuegoPlataforma(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.videojuego} - {self.plataforma}"

class Critico(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Analisis(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    critico = models.ForeignKey(Critico, on_delete=models.CASCADE)
    puntuacion = models.FloatField()
    fecha = models.DateField()
    def __str__(self):
        return f"{self.videojuego} - {self.puntuacion}"

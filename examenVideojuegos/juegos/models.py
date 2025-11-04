from django.db import models

class Estudio(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    anio_fundacion = models.IntegerField(null=True)
    def __str__(self):
        return self.nombre

class Sede(models.Model):
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, null=True)
    ciudad = models.CharField(max_length=100,null=True)
    pais = models.CharField(max_length=100,null=True)
    def __str__(self):
        return f"{self.ciudad} - {self.pais}"

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    fabricante = models.CharField(max_length=100,null=True)
    def __str__(self):
        return f"{self.nombre} ({self.fabricante})"

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100,null=True)
    estudio_desarrollo = models.ForeignKey(Estudio, on_delete=models.CASCADE, null=True)
    plataformas = models.ManyToManyField('Plataforma', through='VideojuegoPlataforma',null=True)
    def __str__(self):
        return self.titulo

class VideojuegoPlataforma(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE,null=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.videojuego} - {self.plataforma}"

class Critico(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.nombre

class Analisis(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE,null=True)
    critico = models.ForeignKey(Critico, on_delete=models.CASCADE, null=True)
    puntuacion = models.FloatField(null=True)
    fecha = models.DateField(null=True)
    def __str__(self):
        return f"{self.videojuego} - {self.puntuacion}"

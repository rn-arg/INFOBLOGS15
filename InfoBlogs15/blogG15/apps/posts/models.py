from django.db import models
from django.utils import timezone

# Create your models here.


#Colaborador
class Colaborador(models.Model):
    correo = models.CharField(max_length=40, null=False)
    username = models.CharField(max_length=25, null=False)
    contrasenia = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.username

#Usuario Registrado
class Usuario(models.Model):
    correo = models.CharField(max_length=40, null=False)
    username = models.CharField(max_length=25, null=False)
    contrasenia = models.CharField(max_length=30, null=False)
    administrado = models.ManyToManyField(Colaborador, blank=True, through='ADMINxUSUARIO')

    def __str__(self):
        return self.username

#Comentario
class Comentario(models.Model):
    texto = models.TextField(null=False)
    usuario_FK = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    valoraciones = models.IntegerField(null=True)
    administrado = models.ManyToManyField(Colaborador, blank=True, through='ADMINxCOMENTARIO')


#Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null= False)

    def __str__(self):
        return self.nombre

#Post
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    usuario_FK = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='sin categoría')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    administrado = models.ManyToManyField(Colaborador, blank=True, through='ADMINxPOST')

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()

#Tablas intermedias -> Modelos para los campos ManyToMany de los modelos Usuario, Comentario y Post
class ADMINxUSUARIO(models.Model):
    id_colaborador_FK = models.ForeignKey(Colaborador, on_delete=models.CASCADE, blank=True, null=True)
    id_usuario_FK = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    accion = models.CharField(max_length=20, null=True)
    descripcion = models.TextField(null=True)

class ADMINxPOST(models.Model):
    id_colaborador_FK = models.ForeignKey(Colaborador, on_delete=models.CASCADE, blank=True, null=True)
    id_post_FK = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    accion = models.CharField(max_length=20, null=True)
    descripcion = models.TextField(null=True)

class ADMINxCOMENTARIO(models.Model):
    id_colaborador_FK = models.ForeignKey(Colaborador, on_delete=models.CASCADE, blank=True, null=True)
    id_comentario_FK = models.ForeignKey(Comentario, on_delete=models.CASCADE, blank=True, null=True)
    accion = models.CharField(max_length=20, null=True)
    descripcion = models.TextField(null=True)
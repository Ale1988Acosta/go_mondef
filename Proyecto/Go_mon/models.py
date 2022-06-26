from django.db import models

#Creación de tablas Go_mon
class Region(models.Model):
    id_Region = models.AutoField(primary_key=True, verbose_name='Id de la Region')
    nombreRegion = models.CharField(max_length=50, verbose_name='Nombre de la Region')

    def __str__(self):
        return self.nombreRegion

class Comuna(models.Model):
    id_Comuna = models.AutoField(primary_key=True, verbose_name='Id de la Comuna')
    nombreComuna = models.CharField(max_length=50, verbose_name='Nombre de la Comuna')
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreComuna

class Sexo (models.Model):
    id_Sexo = models.AutoField(primary_key=True, verbose_name='Id del Sexo')
    nombre = models.CharField(max_length=15, verbose_name='Nombre del Sexo')

    def __str__(self):
        return self.nombre 

class Cuidador(models.Model):
    rut_cuidador = models.CharField(max_length=10,primary_key=True, verbose_name='Rut del cuidador')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del cuidador')
    p_apellido = models.CharField(max_length=50, verbose_name='Primer apellido del cuidador')
    s_apellido = models.CharField(max_length=50, null=True, blank=True, verbose_name='Segundo apellido del cuidador')
    fNacimiento = models.DateField(verbose_name='Fecha de nacimineto del cuidador')
    correo = models.CharField(max_length=100, verbose_name='correo electrónico del cuidador')
    celular = models.IntegerField( verbose_name='número teléfonico del cuidador')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción de parte de la cuidadora')
    tiempo_exp_lab = models.CharField(max_length=100, verbose_name='Experiencias del cuidador')
    tarifa = models.IntegerField(verbose_name='Precio del cuidador')
    foto = models.ImageField(upload_to="cuidador", null=True, blank=True)
    enlace_video = models.CharField(max_length=50,null=True, blank=True ,verbose_name='enlace de video del cuidador opcional')
    sexo = models.ForeignKey(Sexo,on_delete= models.CASCADE, verbose_name='Género u sexo del cuidador')
    
    def __str__(self):
        return self.nombre

class Direc_Cuidador(models.Model):
    id_DirecCuid = models.AutoField(primary_key=True, verbose_name='Id de la direccion del cuidador')
    descripCuidador = models.CharField(max_length=50, verbose_name='Descripcion de la direccion del cuidador')
    deptoCuidador = models.CharField(max_length=6, verbose_name='Depto del cuidador', null=True, blank=True)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    rut_cuidador = models.ForeignKey(Cuidador,on_delete= models.CASCADE, verbose_name='Rut del cuidador Foranea')

    def __str__(self):
        return self.descripCuidador

class Apoderado (models.Model):
    rut_apoderado = models.CharField(max_length=10,primary_key=True, verbose_name='Rut del Apoderado')
    nombre = models.CharField(max_length=30, verbose_name='Nombre del Apoderado')
    p_apellido = models.CharField(max_length=50, verbose_name='Primer Apellido del Apoderado')
    s_apellido = models.CharField(max_length=50, verbose_name='Segundo Apellido del Apoderado', null=True, blank=True)    
    correo = models.CharField(max_length=50, verbose_name='Correo Electronico')
    celular = models.IntegerField(verbose_name="Numero de Celular")
    foto = models.ImageField(upload_to="Apoderado", null=True, blank=True)
    sexo = models.ForeignKey(Sexo,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Direc_Apoderado(models.Model):
    id_DirApod = models.AutoField(primary_key=True, verbose_name='Id de la direccion del apoderado')
    descripApoderado = models.CharField(max_length=50, verbose_name='Descripcion de la direccion del apoderado')
    deptoApoderado = models.CharField(max_length=6, verbose_name='Depto del apoderado', null=True, blank=True)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    rut_apoderado = models.ForeignKey(Apoderado,on_delete=models.CASCADE, verbose_name='Rut del apoderado Foranea')

    def __str__(self):
        return self.descripApoderado

class Habilidad(models.Model):
    id_habilidad = models.AutoField(primary_key=True, verbose_name='Id de la habilidad')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del cuidador')

    def __str__(self):
        return self.nombre

class Habil_cuid(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Id de la habilidad')
    rut_cuidador = models.ForeignKey(Cuidador,on_delete= models.CASCADE, verbose_name='Rut del cuidador Foranea')
    id_habilidad = models.ForeignKey(Habilidad,on_delete= models.CASCADE, verbose_name='Id de la habilidad Foranea')
    
class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True, verbose_name='Id del idioma')
    nombre = models.CharField(max_length=50, verbose_name='Idioma')

    def __str__(self):
        return self.nombre

class Idio_cuid(models.Model):
    id_idio_cuid = models.AutoField(primary_key=True, verbose_name='Id idioma del cuidador')
    rut_cuidador = models.ForeignKey(Cuidador,on_delete= models.CASCADE, verbose_name='Rut del cuidador Foranea')
    idioma = models.ForeignKey(Idioma, on_delete= models.CASCADE, verbose_name='idioma del cuidador')

class Dia(models.Model):
    id_Dia = models.AutoField(primary_key=True, verbose_name="ID autoincrementable de la Dia")
    nombreDia = models.CharField(max_length=10, verbose_name="Nombre del Dia")

    def __str__(self):
        return self.nombreDia

class Bloque(models.Model):
    id_Bloque = models.AutoField(primary_key=True, verbose_name="ID autoincrementable del bloque")
    hora = models.CharField(max_length=20, verbose_name="Intervalo de hora")

    def __str__(self):
        return self.hora

class Dia_Bloq(models.Model):
    id_Db = models.AutoField(primary_key=True, verbose_name="ID autoincrementable del dia y bloque")
    Dia = models.ForeignKey(Dia,on_delete=models.CASCADE)
    bloque = models.ForeignKey(Bloque,on_delete=models.CASCADE)

class Menor(models.Model):
    rut_Menor =  models.CharField(max_length=10,primary_key=True, verbose_name='Rut del Menor')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Menor')
    p_Apellido = models.CharField(max_length=50, verbose_name='Primer Apellido del Menor')
    s_Apellido = models.CharField(max_length=50, verbose_name='Segundo Apellido del Menor',null=True, blank=True)
    fNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")	
    sexo = models.ForeignKey(Sexo,on_delete=models.CASCADE)
    rut_apoderado = models.ForeignKey(Apoderado,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    id_Servicio = models.AutoField(primary_key=True, verbose_name="ID autoincrementable del servicio")
    fContrato = models.DateField(verbose_name="Fecha de contrato")
    estatus= models.CharField(max_length=2, verbose_name="estatus")
    fInicio = models.DateField(verbose_name="Fecha de inicio")
    fFinal = models.DateField(verbose_name="Fecha de Termino")
    costoH = models.IntegerField(verbose_name="Costo de hora")
    cantidadH = models.IntegerField(verbose_name="Cantidad de hora")
    rut_apoderado = models.ForeignKey(Apoderado,on_delete=models.CASCADE)
    rut_cuidador = models.ForeignKey(Cuidador,on_delete=models.CASCADE)

class Servi_Bloq (models.Model):
    id_Sb = models.AutoField(primary_key=True, verbose_name="ID autoincrementable del servicio y bloque")
    id_Db = models.ForeignKey(Dia_Bloq,on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)

class Rol (models.Model):
    id_Rol = models.AutoField(primary_key=True, verbose_name='Id del Rol')
    nombre = models.CharField(max_length=15, verbose_name='Nombre del Rol')

    def __str__(self):
        return self.nombre

class Usuario (models.Model):
    id_Usuario = models.AutoField(primary_key=True, verbose_name='Id del Ususario')
    correo = models.CharField(max_length=50, verbose_name='Correo del Usuario')
    clave = models.CharField(max_length=16, verbose_name='Clave del Usuario')
    estatus = models.CharField(max_length=2, verbose_name='Esta activo o no')
    rut = models.CharField(max_length=11, verbose_name='Rut del usuario')
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

    def __str__(self):
        return self.correo


# Generated by Django 4.0.4 on 2022-06-03 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('rut_apoderado', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut del Apoderado')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del Apoderado')),
                ('p_Apellido', models.CharField(max_length=50, verbose_name='Primer Apellido del Apoderado')),
                ('s_Apellido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Apellido del Apoderado')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo Electronico')),
                ('celular', models.IntegerField(verbose_name='Numero de Celular')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='Apoderado')),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id_Bloque', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable del bloque')),
                ('hora', models.IntegerField(verbose_name='Intervalo de hora')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_Comuna', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la Comuna')),
                ('nombreComuna', models.CharField(max_length=50, verbose_name='Nombre de la Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Cuidador',
            fields=[
                ('rut_cuidador', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut del cuidador')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del cuidador')),
                ('p_apellido', models.CharField(max_length=50, verbose_name='Primer apellido del cuidador')),
                ('s_apellido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo apellido del cuidador')),
                ('fNacimiento', models.DateField(verbose_name='Fecha de nacimineto del cuidador')),
                ('correo', models.CharField(max_length=100, verbose_name='correo electrónico del cuidador')),
                ('celular', models.IntegerField(verbose_name='número teléfonico del cuidador')),
                ('descripcion', models.CharField(max_length=60, verbose_name='Descripción de parte de la cuidadora')),
                ('tiempo_exp_lab', models.CharField(max_length=50, verbose_name='Experiencias del cuidador')),
                ('tarifa', models.IntegerField(verbose_name='Precio del cuidador')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='cuidador')),
                ('enlace_video', models.CharField(blank=True, max_length=50, null=True, verbose_name='enlace de video del cuidador opcional')),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id_Dia', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable de la Dia')),
                ('nombreDia', models.CharField(max_length=10, verbose_name='Nombre del Dia')),
            ],
        ),
        migrations.CreateModel(
            name='Dia_Bloq',
            fields=[
                ('id_Db', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable del dia y bloque')),
                ('Dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.dia')),
                ('bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.bloque')),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id_habilidad', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la habilidad')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del cuidador')),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id_idioma', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del idioma')),
                ('nombre', models.CharField(max_length=50, verbose_name='Idioma')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_Region', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la Region')),
                ('nombreRegion', models.CharField(max_length=50, verbose_name='Nombre de la Region')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_Rol', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del Rol')),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombre del Rol')),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id_Sexo', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del Sexo')),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombre del Sexo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_Usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del Ususario')),
                ('correo', models.CharField(max_length=50, verbose_name='Nombre del Usuario')),
                ('clave', models.CharField(max_length=10, verbose_name='Clave del Usuario')),
                ('estatus', models.CharField(max_length=2, verbose_name='Esta activo o no')),
                ('rut', models.CharField(max_length=11, verbose_name='Esta activo o no')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_Servicio', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable del servicio')),
                ('fContrato', models.DateField(verbose_name='Fecha de contrato')),
                ('estatus', models.CharField(max_length=2, verbose_name='estatus')),
                ('fInicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fFinal', models.DateField(verbose_name='Fecha de Termino')),
                ('costoH', models.IntegerField(verbose_name='Costo de hora')),
                ('cantidadH', models.IntegerField(verbose_name='Cantidad de hora')),
                ('emoji', models.IntegerField(verbose_name='emojis')),
                ('calificacion', models.IntegerField(verbose_name='Calificaciones')),
                ('comentario', models.CharField(max_length=250, verbose_name='Comentarios')),
                ('rut_apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.apoderado')),
                ('rut_cuidador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.cuidador')),
            ],
        ),
        migrations.CreateModel(
            name='Servi_Bloq',
            fields=[
                ('id_Sb', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable del servicio y bloque')),
                ('id_Db', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.dia_bloq')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Menor',
            fields=[
                ('rut_Menor', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut del Menor')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Menor')),
                ('p_Apellido', models.CharField(max_length=50, verbose_name='Primer Apellido del Menor')),
                ('s_Apellido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo Apellido del Menor')),
                ('fNacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('rut_apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.apoderado')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.sexo')),
            ],
        ),
        migrations.CreateModel(
            name='Idio_cuid',
            fields=[
                ('id_idio_cuid', models.AutoField(primary_key=True, serialize=False, verbose_name='Id idioma del cuidador')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.idioma', verbose_name='idioma del cuidador')),
                ('rut_cuidador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.cuidador', verbose_name='Rut del cuidador Foranea')),
            ],
        ),
        migrations.CreateModel(
            name='Habil_cuid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la habilidad')),
                ('id_habilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.habilidad', verbose_name='Id de la habilidad Foranea')),
                ('rut_cuidador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.cuidador', verbose_name='Rut del cuidador Foranea')),
            ],
        ),
        migrations.CreateModel(
            name='Direc_Cuidador',
            fields=[
                ('id_DirecCuid', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la direccion del cuidador')),
                ('descripCuidador', models.CharField(max_length=50, verbose_name='Descripcion de la direccion del cuidador')),
                ('deptoCuidador', models.IntegerField(verbose_name='Depto del cuidador')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.comuna')),
                ('rut_cuidador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.cuidador', verbose_name='Rut del cuidador Foranea')),
            ],
        ),
        migrations.CreateModel(
            name='Direc_Apoderado',
            fields=[
                ('id_DirApod', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la direccion del apoderado')),
                ('descripApoderado', models.CharField(max_length=50, verbose_name='Descripcion de la direccion del apoderado')),
                ('deptoApoderado', models.IntegerField(verbose_name='Depto del apoderado')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.comuna')),
                ('rut_apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.apoderado', verbose_name='Rut del apoderado Foranea')),
            ],
        ),
        migrations.AddField(
            model_name='cuidador',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.sexo', verbose_name='Género u sexo del cuidador'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.region'),
        ),
        migrations.AddField(
            model_name='apoderado',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Go_mon.sexo'),
        ),
    ]

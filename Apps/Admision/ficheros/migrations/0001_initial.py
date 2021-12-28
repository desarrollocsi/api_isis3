# Generated by Django 3.1.3 on 2021-04-22 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cie10',
            fields=[
                ('orden', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=6, unique=True)),
                ('descripcion', models.CharField(max_length=230)),
                ('capitulo', models.IntegerField(blank=True, null=True)),
                ('idgrupo', models.IntegerField(blank=True, null=True)),
                ('idcategoria', models.IntegerField(blank=True, null=True)),
                ('codigoexportacion', models.CharField(blank=True, max_length=5, null=True)),
                ('codigocie9', models.CharField(blank=True, max_length=5, null=True)),
                ('codigocie2004', models.CharField(blank=True, max_length=7, null=True)),
                ('gestacion', models.TextField(blank=True, null=True)),
                ('morbilidad', models.TextField(blank=True, null=True)),
                ('intrahospitalario', models.TextField(blank=True, null=True)),
                ('restriccion', models.TextField(blank=True, null=True)),
                ('edadmaxdias', models.IntegerField(blank=True, null=True)),
                ('edadmindias', models.IntegerField(blank=True, null=True)),
                ('idtiposexo', models.IntegerField(blank=True, null=True)),
                ('area', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'cie10',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Consultorios',
            fields=[
                ('co_codigo', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='co_codigo')),
                ('co_descorta', models.CharField(blank=True, max_length=4, null=True)),
                ('co_descripcion', models.CharField(blank=True, max_length=30, null=True)),
                ('co_tipo', models.IntegerField(blank=True, null=True)),
                ('co_user', models.CharField(blank=True, max_length=15, null=True)),
                ('co_fecpro', models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 22, 16, 20, 32, 769673), null=True)),
            ],
            options={
                'db_table': 'consultorios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('es_codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('es_descripcion', models.CharField(blank=True, max_length=40, null=True)),
                ('es_usuario', models.CharField(blank=True, max_length=15, null=True)),
                ('es_fecpro', models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 22, 16, 20, 32, 769673), null=True)),
                ('val_equivalencia', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'especialidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('me_codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('me_colegio', models.CharField(blank=True, max_length=5, null=True)),
                ('me_tipomedico', models.CharField(blank=True, max_length=3, null=True)),
                ('me_nombres', models.CharField(blank=True, max_length=120, null=True)),
                ('me_fechareg', models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 22, 16, 20, 32, 769673), null=True)),
                ('me_estado', models.CharField(blank=True, max_length=1, null=True)),
                ('me_usuario', models.CharField(blank=True, max_length=15, null=True)),
                ('me_ruc', models.CharField(blank=True, max_length=11, null=True)),
                ('me_direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('me_telefonofijo', models.CharField(blank=True, max_length=20, null=True)),
                ('me_telefonocelular', models.CharField(blank=True, max_length=20, null=True)),
                ('me_intervalo', models.IntegerField()),
                ('me_correo', models.CharField(blank=True, max_length=50, null=True)),
                ('me_tipo_func', models.IntegerField(blank=True, null=True)),
                ('me_docid', models.CharField(blank=True, max_length=15, null=True)),
                ('me_adicionales', models.IntegerField(blank=True, null=True)),
                ('me_extras', models.IntegerField(blank=True, null=True)),
                ('cmdco', models.DecimalField(blank=True, decimal_places=0, max_digits=18, null=True)),
                ('me_apaterno', models.CharField(blank=True, max_length=40, null=True)),
                ('me_amaterno', models.CharField(blank=True, max_length=40, null=True)),
                ('me_pnombre', models.CharField(blank=True, max_length=20, null=True)),
                ('me_snombre', models.CharField(blank=True, max_length=20, null=True)),
                ('me_domicilio', models.CharField(blank=True, max_length=80, null=True)),
                ('me_ubigeo', models.CharField(blank=True, max_length=8, null=True)),
                ('me_cpostal', models.CharField(blank=True, max_length=8, null=True)),
                ('me_telefonoficina', models.CharField(blank=True, max_length=20, null=True)),
                ('me_correo2', models.CharField(blank=True, max_length=40, null=True)),
                ('me_fecnac', models.DateField(blank=True, null=True)),
                ('me_ubigeonac', models.CharField(blank=True, max_length=8, null=True)),
                ('me_tpodocumento', models.CharField(blank=True, max_length=1, null=True)),
                ('me_nrodocumento', models.CharField(blank=True, max_length=12, null=True)),
                ('me_foto', models.CharField(blank=True, max_length=100, null=True)),
                ('me_rne', models.CharField(blank=True, max_length=20, null=True)),
                ('me_regdroga', models.CharField(blank=True, max_length=50, null=True)),
                ('me_anexo', models.CharField(blank=True, max_length=10, null=True)),
                ('me_colegioval', models.CharField(blank=True, max_length=1, null=True)),
                ('me_rutafoto', models.CharField(blank=True, max_length=150, null=True)),
                ('me_sexo', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'medicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('tu_codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('tu_horaini', models.CharField(blank=True, max_length=5, null=True)),
                ('tu_horafin', models.CharField(blank=True, max_length=5, null=True)),
                ('tu_tipoturno', models.CharField(blank=True, max_length=1, null=True)),
                ('tu_horas', models.CharField(blank=True, max_length=5, null=True)),
                ('tu_descripcion', models.CharField(blank=True, max_length=40, null=True)),
                ('tu_fechareg', models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 22, 16, 20, 32, 769673), null=True)),
                ('tu_usuario', models.CharField(blank=True, max_length=15, null=True)),
                ('tu_nhoraini', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('tu_nhorafin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('tu_horario', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'turnos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('an_tipo', models.IntegerField(blank=True, null=True)),
                ('an_destipo', models.CharField(blank=True, max_length=50, null=True)),
                ('an_codigo', models.IntegerField(blank=True, null=True)),
                ('an_descripcion', models.CharField(blank=True, max_length=100, null=True)),
                # ('created_at', models.DateTimeField(blank=True, null=True)),
                # ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'antecedentes',
                'managed': True,
            },
        ),
        # migrations.CreateModel(
        #     name='AntecedentesActoMedico',
        #     fields=[
        #         ('id', models.BigAutoField(primary_key=True, serialize=False)),
        #         ('idcita', models.IntegerField()),
        #         ('an_id', models.IntegerField()),
        #         ('an_valor', models.CharField(blank=True, max_length=50, null=True)),
        #         ('created_at', models.DateTimeField(blank=True, null=True)),
        #         ('updated_at', models.DateTimeField(blank=True, null=True)),
        #     ],
        #     options={
        #         'db_table': 'antecedentes_acto_medico',
        #         'managed': True,
        #     },
        # ),
    ]
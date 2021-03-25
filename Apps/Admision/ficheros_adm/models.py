from django.db import models

# Create your models here.

class Especialidades(models.Model):
    es_codigo = models.AutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='es_codigo',null=False)
    es_descripcion = models.CharField(max_length=40, blank=True, null=True)
    es_usuario = models.CharField(max_length=15, blank=True, null=True)
    es_fecpro = models.DateTimeField(blank=True, null=True)
    val_equivalencia = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidades'
    def __str__(self):
        return self.es_descripcion

    # def get_es_codigo(self, **kwargs):
    #     es_codigo = super(Especialidades, self).get_auto_code(**kwargs)
    #     codigo_str = str(self.id)
    #     es_codigo = self.es_codigo = codigo_str
    #     return es_codigo

class Consultorios(models.Model):
    co_codigo = models.AutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='co_codigo')
    co_descorta = models.CharField(max_length=4, blank=True, null=True)
    co_descripcion = models.CharField(max_length=30, blank=True, null=True)
    co_tipo = models.IntegerField(blank=True, null=True)
    co_user = models.CharField(max_length=15, blank=True, null=True)
    co_fecpro = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'consultorios'
    def __str__(self):
        return self.co_descripcion

class Medicos(models.Model):
    me_codigo = models.AutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='me_codigo',null=False)
    me_colegio = models.CharField(max_length=5, blank=True, null=True)
    me_tipomedico = models.CharField(max_length=3, blank=True, null=True)
    me_nombres = models.CharField(max_length=120, blank=True, null=True)
    me_fechareg = models.DateTimeField(blank=True, null=True)
    me_estado = models.CharField(max_length=1, blank=True, null=True)
    me_especialidad = models.ForeignKey('Especialidades', models.DO_NOTHING, db_column='me_especialidad', blank=True, null=True)
    me_usuario = models.CharField(max_length=15, blank=True, null=True)
    me_ruc = models.CharField(max_length=11, blank=True, null=True)
    me_direccion = models.CharField(max_length=50, blank=True, null=True)
    me_telefonofijo = models.CharField(max_length=20, blank=True, null=True)
    me_telefonocelular = models.CharField(max_length=20, blank=True, null=True)
    me_intervalo = models.IntegerField(null=False)
    me_correo = models.CharField(max_length=50, blank=True, null=True)
    me_tipo_func = models.IntegerField(blank=True, null=True)
    me_docid = models.CharField(max_length=15, blank=True, null=True)
    me_adicionales = models.IntegerField(blank=True, null=True)
    me_extras = models.IntegerField(blank=True, null=True)
    cmdco = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    me_apaterno = models.CharField(max_length=40, blank=True, null=True)
    me_amaterno = models.CharField(max_length=40, blank=True, null=True)
    me_pnombre = models.CharField(max_length=20, blank=True, null=True)
    me_snombre = models.CharField(max_length=20, blank=True, null=True)
    me_domicilio = models.CharField(max_length=80, blank=True, null=True)
    me_ubigeo = models.CharField(max_length=8, blank=True, null=True)
    me_cpostal = models.CharField(max_length=8, blank=True, null=True)
    me_telefonoficina = models.CharField(max_length=20, blank=True, null=True)
    me_correo2 = models.CharField(max_length=40, blank=True, null=True)
    me_fecnac = models.DateField(blank=True, null=True)
    me_ubigeonac = models.CharField(max_length=8, blank=True, null=True)
    me_tpodocumento = models.CharField(max_length=1, blank=True, null=True)
    me_nrodocumento = models.CharField(max_length=12, blank=True, null=True)
    me_foto = models.CharField(max_length=100, blank=True, null=True)
    me_rne = models.CharField(max_length=20, blank=True, null=True)
    me_regdroga = models.CharField(max_length=50, blank=True, null=True)
    me_anexo = models.CharField(max_length=10, blank=True, null=True)
    me_colegioval = models.CharField(max_length=1, blank=True, null=True)
    me_rutafoto = models.CharField(max_length=150, blank=True, null=True)
    me_sexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicos'

    def __str__(self):
        return self.me_nombres

class Turnos(models.Model):
    tu_codigo = models.AutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='tu_codigo',null=False)
    tu_horaini = models.CharField(max_length=5, blank=True, null=True)
    tu_horafin = models.CharField(max_length=5, blank=True, null=True)
    tu_tipoturno = models.CharField(max_length=1, blank=True, null=True)
    tu_horas = models.CharField(max_length=5, blank=True, null=True)
    tu_descripcion = models.CharField(max_length=40, blank=True, null=True)
    tu_fechareg = models.DateTimeField(blank=True, null=True)
    tu_usuario = models.CharField(max_length=15, blank=True, null=True)
    tu_nhoraini = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tu_nhorafin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tu_horario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turnos'
    def __str__(self):
        return self.tu_descripcion


class Cie10(models.Model):
    orden = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=6)
    descripcion = models.CharField(max_length=230)
    capitulo = models.IntegerField(blank=True, null=True)
    idgrupo = models.IntegerField(blank=True, null=True)
    idcategoria = models.IntegerField(blank=True, null=True)
    codigoexportacion = models.CharField(max_length=5, blank=True, null=True)
    codigocie9 = models.CharField(max_length=5, blank=True, null=True)
    codigocie2004 = models.CharField(max_length=7, blank=True, null=True)
    gestacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    morbilidad = models.TextField(blank=True, null=True)  # This field type is a guess.
    intrahospitalario = models.TextField(blank=True, null=True)  # This field type is a guess.
    restriccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    edadmaxdias = models.IntegerField(blank=True, null=True)
    edadmindias = models.IntegerField(blank=True, null=True)
    idtiposexo = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cie10'

class Antecedentes(models.Model):
    id = models.BigAutoField(primary_key=True)
    an_tipo = models.IntegerField(blank=True, null=True)
    an_destipo = models.CharField(max_length=50, blank=True, null=True)
    an_codigo = models.IntegerField(blank=True, null=True)
    an_descripcion = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antecedentes'


class AntecedentesActoMedico(models.Model):
    id = models.BigAutoField(primary_key=True)
    idcita = models.IntegerField()
    an_id = models.IntegerField()
    an_valor = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antecedentes_acto_medico'

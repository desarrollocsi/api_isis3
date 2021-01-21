# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Historias(models.Model):
    hc_numhis = models.CharField(primary_key=True, max_length=10)
    hc_apepat = models.CharField(max_length=50, blank=True, null=True)
    hc_apemat = models.CharField(max_length=50)
    hc_apecas = models.CharField(max_length=50, blank=True, null=True)
    hc_nombre = models.CharField(max_length=50)
    hc_tipohc = models.CharField(max_length=3)
    hc_estcivil = models.ForeignKey('EstadosCiviles', models.DO_NOTHING, db_column='hc_estcivil', blank=True, null=True)
    hc_tiposangre = models.ForeignKey('TiposDeSangre', models.DO_NOTHING, db_column='hc_tiposangre', blank=True, null=True)
    hc_tipoasegurado = models.CharField(max_length=5, blank=True, null=True)
    hc_aseguradora = models.CharField(max_length=3, blank=True, null=True)
    hc_contratante = models.CharField(max_length=6, blank=True, null=True)
    hc_condicion = models.ForeignKey('CondicionAsegurado', models.DO_NOTHING, db_column='hc_condicion', blank=True, null=True)
    hc_fecfiliacion = models.CharField(max_length=10, blank=True, null=True)
    hc_fecdesafiliacion = models.CharField(max_length=10, blank=True, null=True)
    hc_fecnac = models.CharField(max_length=10, blank=True, null=True)
    hc_sexo = models.CharField(max_length=1)
    hc_ubnacim = models.CharField(max_length=8, blank=True, null=True)
    hc_direccion = models.CharField(max_length=100, blank=True, null=True)
    hc_nacionalidad = models.ForeignKey('Paises', models.DO_NOTHING, db_column='hc_nacionalidad', blank=True, null=True)
    hc_telefono1 = models.CharField(max_length=25, blank=True, null=True)
    hc_ubdirec = models.CharField(max_length=8, blank=True, null=True)
    hc_telefono2 = models.CharField(max_length=25, blank=True, null=True)
    hc_ocupacion = models.ForeignKey('Ocupaciones', models.DO_NOTHING, db_column='hc_ocupacion')
    hc_raza = models.CharField(max_length=25, blank=True, null=True)
    hc_tipodoc = models.ForeignKey('TipoDocumentosPersonales', models.DO_NOTHING, db_column='hc_tipodoc', blank=True, null=True)
    hc_estser = models.CharField(max_length=1, blank=True, null=True)
    hc_titular = models.CharField(max_length=50, blank=True, null=True)
    hc_famparen = models.CharField(max_length=3, blank=True, null=True)
    hc_obs = models.CharField(max_length=100, blank=True, null=True)
    hc_famnom = models.CharField(max_length=75, blank=True, null=True)
    hc_famdir = models.CharField(max_length=100, blank=True, null=True)
    hc_estado = models.CharField(max_length=8)
    hc_tipopaciente = models.CharField(max_length=3, blank=True, null=True)
    hc_medicotrat = models.CharField(max_length=3, blank=True, null=True)
    hc_famtel = models.CharField(max_length=25, blank=True, null=True)
    hc_nunref = models.CharField(max_length=10, blank=True, null=True)
    hc_usuario = models.CharField(max_length=15)
    hc_ubarch = models.CharField(max_length=8, blank=True, null=True)
    hc_famubi = models.CharField(max_length=6, blank=True, null=True)
    hc_ruc = models.CharField(max_length=12, blank=True, null=True)
    hc_email = models.CharField(max_length=75, blank=True, null=True)
    hc_fecreg = models.DateTimeField()
    idpaciente = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    hc_codasepac = models.CharField(max_length=18, blank=True, null=True)
    hc_tipoafil = models.IntegerField(blank=True, null=True)
    hc_numref = models.CharField(max_length=10, blank=True, null=True)
    hc_numdoc = models.BinaryField(blank=True, null=True)
    hc_estadoreg = models.IntegerField(blank=True, null=True)
    hc_numdoc1 = models.CharField(max_length=50, blank=True, null=True)    

    class Meta:
        managed = False
        db_table = 'historias'
    def __str__(self):
        return f'{self.hc_numhis} {self.hc_apepat}'

class Medicos(models.Model):
    me_codigo = models.CharField(primary_key=True, max_length=3)
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
    me_intervalo = models.IntegerField()
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
    tu_codigo = models.CharField(primary_key=True, max_length=3)
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

class Programacion(models.Model):
    pr_numero = models.CharField(primary_key=True, max_length=8)
    pr_medico = models.ForeignKey('Medicos', models.DO_NOTHING, db_column='pr_medico', blank=True, null=True)
    pr_consultorio = models.ForeignKey('Consultorios', models.DO_NOTHING, db_column='pr_consultorio', blank=True, null=True)
    pr_servicio = models.ForeignKey('Especialidades', models.DO_NOTHING, db_column='pr_servicio', blank=True, null=True)
    pr_turno = models.ForeignKey('Turnos', models.DO_NOTHING, db_column='pr_turno', blank=True, null=True)
    pr_fecha = models.CharField(max_length=10, blank=True, null=True)
    pr_estado = models.CharField(max_length=1, blank=True, null=True)
    pr_cupos = models.IntegerField(blank=True, null=True)
    pr_minutos = models.IntegerField(blank=True, null=True)
    pr_tipo = models.CharField(max_length=1, blank=True, null=True)
    pr_fechareg = models.DateTimeField(blank=True, null=True)
    pr_usuario = models.CharField(max_length=15, blank=True, null=True)
    pr_observ = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programacion'

class Especialidades(models.Model):
    es_codigo = models.CharField(primary_key=True, max_length=3)
    es_descripcion = models.CharField(max_length=40, blank=True, null=True)
    es_usuario = models.CharField(max_length=15, blank=True, null=True)
    es_fecpro = models.DateTimeField(blank=True, null=True)
    val_equivalencia = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidades'
    def __str__(self):
        return self.es_descripcion

class Consultorios(models.Model):
    co_codigo = models.CharField(primary_key=True, max_length=3)
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

class Citas(models.Model):
    ci_idcita           = models.AutoField(primary_key=True)
    ci_cuenta           = models.CharField(max_length=10)
    ci_historia         = models.ForeignKey(Historias,models.DO_NOTHING, related_name='h_citas', db_column='ci_numhist', blank=True, null=True) # models.CharField(max_length=10)
    # ci_numhist        = models.ForeignKey('Historias', on_delete=models.CASCADE, null=True)
    # hc_numhist        = models.ForeignKey("Historias",verbose_name="Historia",on_delete=models.CASCADE, null=True, db_column='ci_numhist') 
    # ci_numhist        = models.ForeignKey(Historias, related_name='citas', on_delete=models.CASCADE, null=True)
    ci_fechacita        = models.DateTimeField(blank=True, null=True)
    ci_especialidad     = models.ForeignKey(Especialidades,models.DO_NOTHING,related_name='e_citas', db_column='ci_servicio', blank=True, null=True)
    ci_programacion     = models.ForeignKey(Programacion,models.DO_NOTHING,related_name='programacion', db_column='ci_programacion', blank=True, null=True)
    # ci_turno          = models.CharField(max_length=3, blank=True, null=True)
    ci_turno            = models.ForeignKey(Turnos,models.DO_NOTHING,related_name='t_citas', db_column='ci_turno', blank=True, null=True)
    # ci_medico         = models.CharField(max_length=3, blank=True, null=True)
    ci_medico           = models.ForeignKey(Medicos,models.DO_NOTHING,related_name='m_citas', db_column='ci_medico', blank=True, null=True)
    #ci_consultorio     = models.CharField(max_length=3, blank=True, null=True)
    ci_consultorio      = models.ForeignKey(Consultorios,models.DO_NOTHING,related_name='c_citas', db_column='ci_consultorio', blank=True, null=True)
    ci_orden            = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ci_horatencion      = models.CharField(max_length=5, blank=True, null=True)
    ci_observaciones    = models.CharField(max_length=50, blank=True, null=True)
    ci_indicatencion    = models.CharField(max_length=5, blank=True, null=True)
    ci_edad             = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ci_tipopac          = models.CharField(max_length=5, blank=True, null=True)
    ci_tipomov          = models.CharField(max_length=3, blank=True, null=True)
    ci_actividad        = models.CharField(max_length=3, blank=True, null=True)
    ci_estado           = models.CharField(max_length=1, blank=True, null=True)
    ci_facturada        = models.IntegerField(blank=True, null=True)
    ci_pagada           = models.IntegerField(blank=True, null=True)
    ci_atend            = models.TextField(blank=True, null=True)  # This field type is a guess.
    ci_terminal         = models.CharField(max_length=15, blank=True, null=True)
    ci_userterm         = models.CharField(max_length=15, blank=True, null=True)
    ci_usersisa         = models.CharField(max_length=15, blank=True, null=True)
    ci_fecpro           = models.DateTimeField(blank=True, null=True)
    ci_indatos          = models.IntegerField(blank=True, null=True)
    ci_dxcie            = models.CharField(max_length=6, blank=True, null=True)
    ci_dxcie2           = models.CharField(max_length=6, blank=True, null=True)
    ci_tarifaexamen     = models.CharField(max_length=2, blank=True, null=True)
    ci_tarifa           = models.CharField(max_length=3, blank=True, null=True)
    ci_contratante      = models.CharField(max_length=6, blank=True, null=True)
    ci_numfac           = models.CharField(max_length=12, blank=True, null=True)
    ci_coaseg           = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ci_cofarm           = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ci_coserv           = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ci_nroid            = models.CharField(max_length=12, blank=True, null=True)
    ci_paciente         = models.CharField(max_length=98, blank=True, null=True)
    ci_codsx            = models.CharField(max_length=1, blank=True, null=True)
    ci_coded            = models.IntegerField(blank=True, null=True)
    ci_tel1             = models.CharField(max_length=15, blank=True, null=True)
    ci_tel2             = models.CharField(max_length=15, blank=True, null=True)    

    class Meta:
        managed = False
        db_table = 'citas'
    def __str__(self):
        return f'{self.ci_cuenta} {self.ci_numhist}'



class TiposDeSangre(models.Model):
    ts_codigo = models.CharField(primary_key=True, max_length=3)
    ts_rh = models.CharField(max_length=25)
    ts_grupo = models.CharField(max_length=25, blank=True, null=True)
    ts_usuario = models.CharField(max_length=15, blank=True, null=True)
    ts_fecpro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tipos_de_sangre'

class TipoDocumentosPersonales(models.Model):
    td_codigo = models.CharField(primary_key=True, max_length=3)
    td_descripcion = models.CharField(max_length=45, blank=True, null=True)
    td_abv = models.CharField(max_length=3, blank=True, null=True)
    td_usuario = models.CharField(max_length=15, blank=True, null=True)
    td_fecpro = models.DateTimeField()
    td_abv2 = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documentos_personales'

class EstadosCiviles(models.Model):
    ec_codigo = models.CharField(primary_key=True, max_length=3)
    ec_descripcion = models.CharField(max_length=25, blank=True, null=True)
    ec_abv = models.CharField(max_length=3, blank=True, null=True)
    ec_usuario = models.CharField(max_length=15, blank=True, null=True)
    ec_fechareg = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estados_civiles'


class CondicionAsegurado(models.Model):
    cd_codi = models.CharField(primary_key=True, max_length=2)
    cd_descrip = models.CharField(max_length=25, blank=True, null=True)
    cd_estado = models.IntegerField(blank=True, null=True)
    cd_feca = models.DateTimeField(blank=True, null=True)
    cd_user = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condicion_asegurado'




class Paises(models.Model):
    pa_codigo = models.CharField(primary_key=True, max_length=3)
    pa_descripcion = models.CharField(max_length=25, blank=True, null=True)
    pa_usuario = models.CharField(max_length=15, blank=True, null=True)
    pa_nacionalidad = models.CharField(max_length=50)
    pa_fechareg = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'paises'


class Ocupaciones(models.Model):
    op_codigo = models.CharField(primary_key=True, max_length=3)
    op_descripcion = models.CharField(max_length=50, blank=True, null=True)
    op_abv = models.CharField(max_length=3, blank=True, null=True)
    op_usuario = models.CharField(max_length=15, blank=True, null=True)
    op_fechareg = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ocupaciones'
## ----------------------------------------------------------------------------------------------------------------------
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
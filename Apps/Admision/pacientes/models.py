from django.db import models


from dateutil.relativedelta import relativedelta
from datetime import datetime
# from django.utils import timezone
# Create your models here.


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
    hc_fecreg = models.DateTimeField(default=datetime.now(),blank=False, null=False)
    idpaciente = models.IntegerField()
    # idpaciente = models.UUIDField()
    password = models.CharField(max_length=50, blank=True, null=True)
    hc_codasepac = models.CharField(max_length=18, blank=True, null=True)
    hc_tipoafil = models.IntegerField(blank=True, null=True)
    hc_numref = models.CharField(max_length=10, blank=True, null=True)
    hc_numdoc = models.BinaryField(blank=True, null=True)
    hc_estadoreg = models.IntegerField(blank=True, null=True)
    hc_numdoc1 = models.CharField(max_length=50, blank=True, null=True)
    hc_fecnac_i3 = models.DateField(null=True)

    class Meta:
        managed = True
        db_table = 'historias'
    def __str__(self):
        return f'{self.hc_numhis} {self.hc_apepat}'

    def getEdad(self):
        # return int((datetime.now().date() - datetime.strptime(self.hc_fecnac, '%d/%m/%Y').date()).days / 365.25)
        edad = relativedelta(datetime.now(), datetime.strptime(self.hc_fecnac, '%d/%m/%Y'))
        return f"{edad.years}a/ {edad.months}m/  {edad.days}d"
    def getNombreCompleto(self):
        return  self.hc_apepat +' ' + self.hc_apemat + ', ' + self.hc_nombre
    # @property
    # def age(self):
    #     return timezone.now().year - self.hc_fecnac.year


class TiposDeSangre(models.Model):
    ts_codigo = models.CharField(primary_key=True, max_length=3)
    ts_rh = models.CharField(max_length=25)
    ts_grupo = models.CharField(max_length=25, blank=True, null=True)
    ts_usuario = models.CharField(max_length=15, blank=True, null=True)
    ts_fecpro = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tipos_de_sangre'


class TipoDocumentosPersonales(models.Model):
    td_codigo = models.CharField(primary_key=True, max_length=3)
    td_descripcion = models.CharField(max_length=45, blank=True, null=True)
    td_abv = models.CharField(max_length=3, blank=True, null=True)
    td_usuario = models.CharField(max_length=15, blank=True, null=True)
    td_fecpro = models.DateTimeField()
    td_abv2 = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_documentos_personales'


class Ocupaciones(models.Model):
    op_codigo = models.CharField(primary_key=True, max_length=3)
    op_descripcion = models.CharField(max_length=50, blank=True, null=True)
    op_abv = models.CharField(max_length=3, blank=True, null=True)
    op_usuario = models.CharField(max_length=15, blank=True, null=True)
    op_fechareg = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'ocupaciones'


class Paises(models.Model):
    pa_codigo = models.CharField(primary_key=True, max_length=3)
    pa_descripcion = models.CharField(max_length=25, blank=True, null=True)
    pa_usuario = models.CharField(max_length=15, blank=True, null=True)
    pa_nacionalidad = models.CharField(max_length=50)
    pa_fechareg = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'paises'

class EstadosCiviles(models.Model):
    ec_codigo = models.CharField(primary_key=True, max_length=3)
    ec_descripcion = models.CharField(max_length=25, blank=True, null=True)
    ec_abv = models.CharField(max_length=3, blank=True, null=True)
    ec_usuario = models.CharField(max_length=15, blank=True, null=True)
    ec_fechareg = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'estados_civiles'


class CondicionAsegurado(models.Model):
    cd_codi = models.CharField(primary_key=True, max_length=2)
    cd_descrip = models.CharField(max_length=25, blank=True, null=True)
    cd_estado = models.IntegerField(blank=True, null=True)
    cd_feca = models.DateTimeField(blank=True, null=True)
    cd_user = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'condicion_asegurado'


class PlanesHistoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    pl_numhist = models.CharField(max_length=10, blank=True, null=True)
    pl_codaseg = models.IntegerField(blank=True, null=True)
    pl_desaseg = models.CharField(max_length=75, blank=True, null=True)
    pl_rucaseg = models.CharField(max_length=16, blank=True, null=True)
    pl_telaseg = models.CharField(max_length=20, blank=True, null=True)
    pl_codplan = models.IntegerField(blank=True, null=True)
    pl_desplan = models.CharField(max_length=75, blank=True, null=True)
    pl_codcont = models.IntegerField(blank=True, null=True)
    pl_descont = models.CharField(max_length=75, blank=True, null=True)
    pl_codparen = models.IntegerField(blank=True, null=True)
    pl_desparen = models.CharField(max_length=25, blank=True, null=True)
    pl_codafilseg = models.CharField(max_length=22, blank=True, null=True)
    pl_fecpro = models.DateTimeField(blank=True, null=True)
    pl_user = models.CharField(max_length=15, blank=True, null=True)
    pl_estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planes_historia'


class TipoAsegurado(models.Model):
    ta_codi = models.CharField(primary_key=True, max_length=8)
    ta_desc = models.CharField(max_length=100, blank=True, null=True)
    ta_tarifa = models.CharField(max_length=3)
    ta_acredita = models.IntegerField(blank=True, null=True)
    ta_cofar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ta_defar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ta_defarho = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ta_flag = models.CharField(max_length=1, blank=True, null=True)
    ta_feca = models.DateTimeField(blank=True, null=True)
    ta_usra = models.CharField(max_length=15, blank=True, null=True)
    ta_coaseguro = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ta_deducible = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ta_coser = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ta_deser = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ta_contratante = models.CharField(max_length=6, blank=True, null=True)
    ta_aseguradora = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_asegurado'
        unique_together = (('ta_codi', 'ta_tarifa'),)
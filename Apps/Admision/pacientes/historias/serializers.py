from rest_framework import serializers
##-------		MODELOS	--------------
from ..models import Historias
from datetime import datetime
from dateutil.relativedelta import relativedelta

class HistorasSearchSerializer(serializers.ModelSerializer):
    # historia = serializers.CharField(source='hc_numhis')
    # nombre_completo	= serializers.CharField(source='getNombreCompleto')
    # nombre_completo =serializers.SerializerMethodField()
    # def get_nombre_completo(self,obj):
    #     return '{} {} {}'.format(self.hc_apepat,self.hc_apemat,self.hc_nombre)
    # sexo    = serializers.CharField(source='hc_sexo')
    edad = serializers.SerializerMethodField() 
    # edad 	= serializers.ReadOnlyField(source='getEdad()')   
    class Meta:
        model = Historias
        fields = ['hc_numhis', 'hc_apepat', 'hc_apemat', 'hc_nombre', 'hc_tipohc','hc_estcivil',
        'hc_fecnac_i3', 'hc_sexo','hc_ubnacim','hc_direccion', 'hc_nacionalidad', 'hc_telefono1',
        'hc_ubdirec', 'hc_telefono2','hc_ocupacion','hc_raza', 'hc_tipodoc',   'hc_obs','hc_numdoc1',
        'hc_estado','hc_estadoreg','idpaciente','edad']
        # fields = ['hc_numhis','sexo','hc_apepat','hc_apemat','hc_nombre','hc_fecnac','edad']
    def get_edad(self, instance):
        # edad = relativedelta(datetime.now(), datetime.strptime(instance.hc_fecnac, '%d/%m/%Y'))
        edad = relativedelta(datetime.now(), instance.hc_fecnac_i3)
        return edad.years # f"{edad.years}"

class HistoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historias
        fields = ['hc_numhis', 'hc_apepat', 'hc_apemat', 'hc_nombre', 'hc_tipohc','hc_estcivil',
        'hc_fecnac_i3', 'hc_sexo','hc_ubnacim','hc_direccion', 'hc_nacionalidad', 'hc_telefono1',
        'hc_ubdirec', 'hc_telefono2','hc_ocupacion','hc_raza', 'hc_tipodoc',   'hc_obs','hc_numdoc1','hc_estado','hc_estadoreg','idpaciente']
        extra_kwargs = {'hc_numhis': {'required': False},'hc_estadoreg': {'required': False},'idpaciente': {'required': False}}
        # ['hc_numhis', 'hc_apepat', 'hc_apemat', 'hc_apecas', 'hc_nombre', 'hc_tipohc',
        # 'hc_estcivil','hc_tiposangre', 'hc_tipoasegurado', 'hc_aseguradora', 'hc_contratante',
        # 'hc_condicion', 'hc_fecfiliacion', 'hc_fecdesafiliacion','hc_fecnac', 'hc_sexo','hc_ubnacim',
        # 'hc_direccion', 'hc_nacionalidad', 'hc_telefono1', 'hc_ubdirec', 'hc_telefono2','hc_ocupacion',
        # 'hc_raza', 'hc_tipodoc', 'hc_estser', 'hc_titular', 'hc_famparen', 'hc_obs', 'hc_famnom',
        # 'hc_famdir', 'hc_estado', 'hc_tipopaciente', 'hc_medicotrat', 'hc_famtel', 'hc_nunref', 'hc_usuario',
        # 'hc_ubarch','hc_famubi', 'hc_ruc', 'hc_email', 'hc_fecreg', 'idpaciente', 'password', 'hc_codasepac',
        # 'hc_tipoafil','hc_numref', 'hc_numdoc', 'hc_estadoreg', 'hc_numdoc1']
        # extra_kwargs = {'hc_numhis': {'required': False},'hc_numdoc1': {'required': False},'hc_estadoreg': {'required': False},
        # 'hc_numdoc': {'required': False},'hc_numref': {'required': False},'hc_tipoafil': {'required': False},
        # 'hc_codasepac': {'required': False},'password': {'required': False},'idpaciente': {'required': False},
        # 'hc_fecreg': {'required': False},'hc_email': {'required': False},'hc_ruc': {'required': False},
        # 'hc_famubi': {'required': False},'hc_ubarch': {'required': False},'hc_usuario': {'required': False},
        # 'hc_nunref': {'required': False},'hc_famtel': {'required': False},'hc_medicotrat': {'required': False},
        # 'hc_tipopaciente': {'required': False},'hc_famdir': {'required': False},'hc_famnom': {'required': False},
        # 'hc_obs': {'required': False},'hc_famparen': {'required': False},'hc_titular': {'required': False},
        # 'hc_estser': {'required': False},'hc_raza': {'required': False},'hc_titular': {'required': False},
        # 'hc_tipoasegurado': {'required': False},'hc_aseguradora': {'required': False},'hc_contratante': {'required': False},
        # 'hc_condicion': {'required': False},'hc_fecfiliacion': {'required': False},'hc_fecdesafiliacion': {'required': False},}


# class HistoriasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Historias
#         fields = '__all__'

# class HistoriasSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Historias
# 		fields = ['hc_numhis', 'hc_apepat', 'hc_apemat', 'hc_apecas', 'hc_nombre', 'hc_tipohc',
#             'hc_estcivil','hc_tiposangre', 'hc_tipoasegurado', 'hc_aseguradora', 'hc_contratante',
#             'hc_condicion', 'hc_fecfiliacion', 'hc_fecdesafiliacion','hc_fecnac', 'hc_sexo','hc_ubnacim',
#             'hc_direccion', 'hc_nacionalidad', 'hc_telefono1', 'hc_ubdirec', 'hc_telefono2','hc_ocupacion',
#             'hc_raza', 'hc_tipodoc', 'hc_estser', 'hc_titular', 'hc_famparen', 'hc_obs', 'hc_famnom',
#             'hc_famdir', 'hc_estado', 'hc_tipopaciente', 'hc_medicotrat', 'hc_famtel', 'hc_nunref', 'hc_usuario',
#             'hc_ubarch','hc_famubi', 'hc_ruc', 'hc_email', 'hc_fecreg', 'idpaciente', 'password', 'hc_codasepac',
#             'hc_tipoafil','hc_numref', 'hc_numdoc', 'hc_estadoreg', 'hc_numdoc1']
        # extra_kwargs = {'hc_numhis': {'required': False},}
    # def __init__(self, *args, **kwargs):
    #     self.fields['hc_usuario'] = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    #     self.fields['hc_estadoreg'] = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    #     return super(HistoriasSerializer, self).__init__(*args, **kwargs)
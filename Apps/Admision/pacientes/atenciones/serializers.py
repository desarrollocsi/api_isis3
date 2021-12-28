from rest_framework import serializers
from ...citas.models import Citas
from ...ficheros.models import Especialidades,Medicos,Consultorios
from ..models import *

class CitasSerializer(serializers.ModelSerializer):
    # especialidad    = EspecialidadesSerializer(source="ci_especialidad")
    # medico          = MedicosSerializer(source="ci_medico")
    # consultorio     = ConsultorioSerializer(source="ci_consultorio")

    medico 		= serializers.ReadOnlyField(source='ci_medico.me_nombres')
    consultorio = serializers.ReadOnlyField(source='ci_consultorio.co_descripcion')
    especialidad = serializers.ReadOnlyField(source='ci_especialidad.es_descripcion')
    paciente	= serializers.ReadOnlyField(source='ci_numhist.getNombreCompleto')
    class Meta:
        model = Citas
        fields= ['ci_idcita',
                'ci_numhist',
                'paciente',
                'ci_programacion',
                'ci_fechacita',
                'ci_horatencion',
                'ci_estado',
                'especialidad',
                'medico',
                'consultorio',
                'actomedico_id']

# class HistoriasLisSerializer(serializers.ModelSerializer):
#     cita = CitasLisSerializer(source="ci_numhist",many=True)
#     class Meta:
#         model = Historias
#         fields = ('hc_nombre', 'hc_numhis','cita')

class CitasLisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields= ['ci_idcita','ci_numhist' ]
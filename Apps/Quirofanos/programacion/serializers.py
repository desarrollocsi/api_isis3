from rest_framework import serializers
from ..models.programacion import *

class ProgramacionDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionParticipantesModel
        fields = '__all__'
        extra_kwargs = {'id': {'validators': []},}



class EquiposMedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionEquiposMedicosModel
        fields = '__all__'
        extra_kwargs = {'id': {'validators': []},}


class ProgramacionSerializer(serializers.ModelSerializer):
    participantes = ProgramacionDetalleSerializer(many=True)
    equiposMedicos = EquiposMedicosSerializer(many=True)
    cq_fecha =  serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ProgramacionModel
        fields = ('cq_numope', 'sa_codsal', 'cq_fecha', 'cq_hoinpr', 'cq_hofipr', 'cq_indrep', 'cq_hoinre', 
                'cq_hofire', 'cq_hoinej', 'cq_hofiej', 'se_codigo', 'cq_codiqx', 'an_tipane', 'cq_cuenta', 
                'cq_numhis', 'cq_tipcon', 'cq_cama', 'cq_estado', 'cq_indfac', 'cq_paciente', 'cq_pedido', 
                'cq_usuario', 'cq_fecpro', 'cq_edad', 'cq_glosa_repro', 'cq_num_petito', 'cq_es_emer', 
                'cq_orden_cq', 'cq_usua_mod_est', 'cq_fecha_mod_est', 'cq_orden_rqx', 'cq_numsema', 
                'cq_areapre', 'cq_codiqx2', 'cq_estd_suspendida', 'cq_es_adelan', 'cq_enfer', 'cq_antibio', 
                'cq_kg', 'cq_btb', 'cq_reing', 'cq_estancia', 'cq_codiqx3', 'cq_motivo_suspen', 'cq_hg',
                'equiposMedicos','participantes')

    #create
    def create(self, validated_data):
        equiposMedicos = validated_data.pop('equiposMedicos')    
        participantes = validated_data.pop('participantes')

        '''Programacion'''
        programacion = ProgramacionModel.objects.create(**validated_data)

        '''Participantes '''
        for participantes in participantes:
            ProgramacionParticipantesModel.objects.create(cq_numope=programacion, **participantes)
        
        '''Equipos Medicos'''
        for equiposMedicos in equiposMedicos:
            ProgramacionEquiposMedicosModel.objects.create(de_numope=programacion, **equiposMedicos)
        return programacion

    #update
    def update(self, instance,validated_data):

        participantes = validated_data.pop('participantes')
        participantes_queryset = (instance.participantes).all()
        detalleDeParticipantes = list(participantes_queryset) 

        equiposMedicos = validated_data.pop('equiposMedicos')
        equiposMedicos_queryset = (instance.equiposMedicos).all()



        ''' Programacion '''
        #Actualiza la programacion
        instance.cq_numope=validated_data.get('cq_numope',instance.cq_numope)
        instance.sa_codsal=validated_data.get('sa_codsal',instance.sa_codsal)
        instance.cq_fecha=validated_data.get('cq_fecha',instance.cq_fecha)
        instance.cq_hoinpr=validated_data.get('cq_hoinpr',instance.cq_hoinpr)
        instance.cq_hofipr=validated_data.get('cq_hofipr',instance.cq_hofipr)
        instance.cq_indrep=validated_data.get('cq_indrep',instance.cq_indrep)
        instance.cq_hoinre=validated_data.get('cq_hoinre',instance.cq_hoinre)
        instance.cq_hofire=validated_data.get('cq_hofire',instance.cq_hofire)
        instance.cq_hoinej=validated_data.get('cq_hoinej',instance.cq_hoinej)
        instance.cq_hofiej=validated_data.get('cq_hofiej',instance.cq_hofiej)
        instance.se_codigo=validated_data.get('se_codigo',instance.se_codigo)
        instance.cq_codiqx=validated_data.get('cq_codiqx',instance.cq_codiqx)
        instance.an_tipane=validated_data.get('an_tipane',instance.cq_codiqx)
        instance.cq_cuenta=validated_data.get('cq_cuenta',instance.cq_cuenta)
        instance.cq_numhis=validated_data.get('cq_numhis',instance.cq_numhis)
        instance.cq_tipcon=validated_data.get('cq_tipcon',instance.cq_tipcon)
        instance.cq_cama=validated_data.get('cq_cama',instance.cq_cama)
        instance.cq_estado=validated_data.get('cq_estado',instance.cq_estado)
        instance.cq_indfac=validated_data.get('cq_indfac',instance.cq_indfac)
        instance.cq_paciente=validated_data.get('cq_paciente',instance.cq_paciente)
        instance.cq_pedido=validated_data.get('cq_pedido',instance.cq_pedido)
        instance.cq_usuario=validated_data.get('cq_usuario',instance.cq_usuario)
        instance.cq_fecpro=validated_data.get('cq_fecpro',instance.cq_fecpro)
        instance.cq_edad=validated_data.get('cq_edad',instance.cq_edad)
        instance.cq_glosa_repro=validated_data.get('cq_glosa_repro',instance.cq_glosa_repro)
        instance.cq_num_petito=validated_data.get('cq_num_petito',instance.cq_num_petito)
        instance.cq_es_emer=validated_data.get('cq_es_emer',instance.cq_es_emer)
        instance.cq_orden_cq=validated_data.get('cq_orden_cq',instance.cq_orden_cq)
        instance.cq_usua_mod_est=validated_data.get('cq_usua_mod_est',instance.cq_usua_mod_est)
        instance.cq_fecha_mod_est=validated_data.get('cq_fecha_mod_est',instance.cq_fecha_mod_est)
        instance.cq_orden_rqx=validated_data.get('cq_orden_rqx',instance.cq_orden_rqx)
        instance.cq_numsema=validated_data.get('cq_numsema',instance.cq_numsema)
        instance.cq_areapre=validated_data.get('cq_areapre',instance.cq_areapre)
        instance.cq_codiqx2=validated_data.get('cq_codiqx2',instance.cq_codiqx2)
        instance.cq_estd_suspendida=validated_data.get('cq_estd_suspendida',instance.cq_estd_suspendida)
        instance.cq_es_adelan=validated_data.get('cq_es_adelan',instance.cq_es_adelan)
        instance.cq_enfer=validated_data.get('cq_enfer',instance.cq_enfer)
        instance.cq_antibio=validated_data.get('cq_antibio',instance.cq_antibio)
        instance.cq_kg=validated_data.get('cq_kg',instance.cq_kg)
        instance.cq_btb=validated_data.get('cq_btb',instance.cq_btb)
        instance.cq_reing=validated_data.get('cq_reing',instance.cq_reing)
        instance.cq_estancia=validated_data.get('cq_estancia',instance.cq_estancia)
        instance.cq_codiqx3=validated_data.get('cq_codiqx3',instance.cq_codiqx3)
        instance.cq_motivo_suspen=validated_data.get('cq_motivo_suspen',instance.cq_motivo_suspen)
        instance.cq_hg=validated_data.get('cq_hg',instance.cq_hg)
        instance.save()
        
        ''' Equipos medicos '''
        #Elimina todo el detale de equipos medicos
        equiposMedicos_queryset.delete()
        for equiposMedicos in equiposMedicos:
            ProgramacionEquiposMedicosModel.objects.create(**equiposMedicos)

        ''' Participantes'''
        #Elimina todo el detale de equipos medicos
        participantes_queryset.delete()
        for participantes in participantes:
            ProgramacionParticipantesModel.objects.create(**participantes)
        return instance
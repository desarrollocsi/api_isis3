from rest_framework import serializers
# from ..models import ProgramacionSOAP


# class ProgramacionSOAPSerializer(serializers.Serializer):
#     cq_numope = serializers.CharField(max_length=10)
#     diahora = serializers.CharField(max_length=50)
#     sala = serializers.CharField(max_length=2)
#     paciente = serializers.CharField(max_length=100)
#     intervencion= serializers.CharField(max_length=50)
#     cirujano = serializers.CharField(max_length=80)
#     anestesia = serializers.CharField(max_length=30)
#     cama = serializers.CharField(max_length=6)
#     pedido = serializers.CharField(max_length=199)
#     cq_fecha = serializers.CharField(max_length=80)
#     cq_hoinpr = serializers.DateTimeField()
#     cq_hofipr = serializers.DateTimeField()
#     cq_hoinej =serializers.DateTimeField()
#     cq_hofiej = serializers.DateTimeField()
#     cq_numhis = serializers.CharField(max_length=10)
#     cq_estado = serializers.CharField(max_length=1)
#     edad = serializers.IntegerField()
#     semanas = serializers.CharField(max_length=10)
#     tiempo = serializers.IntegerField()
#     inf_ope = serializers.BooleanField()
#     cq_indrep = serializers.CharField(max_length=1)








    # class Meta:
    #     model = ProgramacionSOAP
    #     fields = ('diahora',
    #             'sala',
    #             'paciente',
    #             'intervencion',
    #             'cirujano',
    #             'anestesia',
    #             'cama',
    #             'pedido',
    #             'cq_numope',
    #             'cq_fecha',
    #             'cq_hoinpr',
    #             'cq_hofipr',
    #             'cq_hoinej',
    #             'cq_hofiej',
    #             'cq_numhis',
    #             'cq_estado',
    #             'edad',
    #             'semanas',
    #             'tiempo',
    #             'inf_ope',
    #             'cq_indrep')
    #     read_only_fields = fields
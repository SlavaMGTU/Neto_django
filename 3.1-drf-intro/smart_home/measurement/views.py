# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status': 'OK'})


# class DemoView(APIView):
#     def get(self, request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status': 'OK'})


# class DemoView(ListAPIView):
#     queryset = Weapon.objects.all()
#     serializer_class = WeaponSerializer
#
#     def post(self, request):
#         return Response({'status': 'OK'})
#
#
# class WeaponView(RetrieveAPIView):
#     queryset = Weapon.objects.all()
#     serializer_class = WeaponSerializer
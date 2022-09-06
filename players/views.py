from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import PlayersSerializer, PowersSerializer
from .models import Power, Player
from .utils import narration

# Create your views here.
class PowersApiView(APIView):
    """View List and Create of Powers models"""

    def get(self, request, format=None):
        obj = Power.objects.all()
        serializer = PowersSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PowersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

class PowerDetailApiView(APIView):
    """View Detail of Power model."""

    def get_object(self, pk):
        try:
            return Power.objects.get(pk=pk)
        except Power.DoesNotExist:
            raise Http404   

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = PowersSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = PowersSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlayersApiView(APIView):
    """View List and Create of Players models"""

    def get(self, request, format=None):
        obj = Player.objects.all()
        serializer = PlayersSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlayersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

class PlayerDetailApiView(APIView):
    """View Detail of Player model."""

    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404   

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = PlayersSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = PlayersSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GameApiView(APIView):
    """Game and result of that"""

    def post(self, request, format=None):
        data = request.data
        try:
            #GET usernames of fighters
            players = list(data.keys())
            #GET data detail of each fighter
            player_1 = data[players[0]]
            player_2 = data[players[1]]

            #use list comprehension to join 'movimientos' and 'golpes'
            comb_1 = [
                player_1['movimientos'][x] + player_1['golpes'][x] 
                for x in range(len(player_1['movimientos']))
            ]
            comb_2 = [
                player_2['movimientos'][x] + player_2['golpes'][x] 
                for x in range(len(player_2['movimientos']))
            ]

            all_narration = []
            life_1 = 6
            life_2 = 6
            for n in range(max(len(comb_1),len(comb_2))):
                print(n)
                #Player 1
                if n < len(comb_1):
                    n1 = narration(comb_1[n],players[0],players[1])
                    all_narration.append(n1[0])
                    life_2 -= n1[1]
                    if life_2 <= 0:
                        all_narration.append(
                            f"{players[0]} Gana la pelea y aun le queda {life_1} de energía"
                        )
                        return Response(
                            {"relato": all_narration}, 
                            status=status.HTTP_200_OK
                        )

                #Player 1
                if n < len(comb_2):
                    n2 = narration(comb_2[n],players[1],players[0])
                    all_narration.append(n2[0])
                    life_1 -= n2[1]
                    if life_1 <= 0:
                        all_narration.append(
                            f"{players[1]} Gana la pelea y aun le queda {life_2} de energía"
                        )
                        return Response(
                            {"relato": all_narration}, 
                            status=status.HTTP_200_OK
                        )

            return Response(
                {"relato": all_narration}, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {"message":str(e)}, 
                status = status.HTTP_400_BAD_REQUEST
            ) 
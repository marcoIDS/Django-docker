from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from django.http import Http404

class ListSongsView(APIView):

    def get(self, request, format=None):
        song = Songs.objects.all()
        serializer = SongsSerializer(song, many=True)
        return Response({"songs": serializer.data})
    
    def post(self, request, format=None):
        song = request.data.get('song')
        # Create an article from the above data
        serializer = SongsSerializer(data=song)
        if serializer.is_valid(raise_exception=True):
            song_saved = serializer.save()
            datas = serializer.data
            response = datas
            return Response(response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response(response, status=status.HTTP_404_BAD_REQUEST)
        #return Response({"success": "SONG '{}' created successfully".format(song_saved.id)})

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)   
        instance.save()
        return instance
    
    def put(self, request, pk):
        saved_song = get_object_or_404(Songs.objects.all(), pk=pk)
        data = request.data.get('song')
        serializer = SongsSerializer(instance=saved_song, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            song_saved = serializer.save()
        return Response({"success": "song '{}' updated successfully".format(song_saved.title)})

    def delete(self, request, pk):
        # Get object with this pk
        song = get_object_or_404(Songs.objects.all(), pk=pk)
        song.delete()
        return Response({"message": "SONG with id `{}` has been deleted.".format(pk)},status=204)
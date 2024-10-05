from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .models import Breeds, Cats
from .serializers import CatsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
    permission_classes=[IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]

    @action(methods=['get'],detail=False)
    def breed(self,request):
        breeds= Breeds.objects.all()
        return Response({'breeds':[b.breed for b in breeds]})
    
    @action(methods=['get'],detail=False)
    def breed_name(self,request):
        breed_ids = request.query_params.getlist('breed_id')
        
        if not breed_ids:
            return Response({'error': 'No breed IDs provided'}, status=400)
        
        cats = Cats.objects.filter(breed__id__in=breed_ids)
        if not cats.exists():
            return Response({'error': 'No cats found for the provided breeds'}, status=404)
        
        serializer = CatsSerializer(cats, many=True)
        return Response({'cats': serializer.data})
    
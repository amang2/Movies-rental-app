from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.generics import get_object_or_404


class UserCreateListView(ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        queryset= self.get_queryset()
        obj = get_object_or_404(queryset,public_id=self.kwargs['user_id'])
        return obj
    
    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.put(request, *args, **kwargs)

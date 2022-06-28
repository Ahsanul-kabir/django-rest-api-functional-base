from .models import Info
from .serializers import InfoSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class InfoList (GenericAPIView, ListModelMixin):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class InfoCreate (GenericAPIView, CreateModelMixin):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class InfoRetrieve (GenericAPIView, RetrieveModelMixin):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class InfoUpdate (GenericAPIView, UpdateModelMixin):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class InfoDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

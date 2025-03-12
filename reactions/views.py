from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from reactions.models import Reaction
from reactions.serializers import ReactionSerializer


class ReactionList(generics.ListCreateAPIView):
    """
    List Reactions or create a Reaction if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReactionDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a Reaction or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()
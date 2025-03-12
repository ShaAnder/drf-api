from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "welcome": "Welcome to my social media drf api here you can find a working backend for building a social media application, with profiles, posts, commenting, reacting, following and followers",
        "urls": "/profile, /comments /reactions /followers",
        "documentation": "to come",
    })
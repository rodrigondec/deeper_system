from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='hello')
def howdy_view(request):
    return Response('Howdy!!')

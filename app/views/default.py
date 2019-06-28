from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults
from mongoengine.errors import DoesNotExist

from app.models import Video, Theme


@view_defaults(renderer='../templates/home.jinja2')
class DefaultViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        context = {'videos': Video.objects}
        return context

    @view_config(route_name='add_video')
    def add_video(self):
        name = self.request.params.get('name', None)
        theme_name = self.request.params.get('theme', None)
        if name and theme_name:
            try:
                theme = Theme.objects.get(name=theme_name)
            except DoesNotExist:
                theme = Theme(name=theme_name)
                theme.save()
            video = Video(name=name, theme=theme)
            video.save()
            Theme.objects(id=theme.id).update_one(push__videos=video)
        return HTTPFound(location='/')

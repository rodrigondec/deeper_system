from pyramid.view import view_config, view_defaults

from app.models import Theme


@view_defaults(renderer='../templates/ranking.jinja2')
class ThemeViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='ranking')
    def ranking(self):
        themes = sorted(Theme.objects(), key=lambda x: x.rating)
        context = {'themes': themes}
        return context

from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def home_view(request):
    return {'project': 'deeper_system'}

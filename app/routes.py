def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('add_video', '/add_video')
    config.add_route('up', '/up')
    config.add_route('down', '/down')
    config.add_route('ranking', '/ranking')

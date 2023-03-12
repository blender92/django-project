def navbar(request):
    navbar_items = [
        {'label': 'Home', 'url': '/'},
        {'label': 'About Me', 'url': '/aboutme/'},
        {'label': 'Contact', 'url': '/aboutme/contact'},
    ]
    return {'navbar_items': navbar_items}

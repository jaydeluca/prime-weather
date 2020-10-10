def register_routes(api, app, root="api"):
    from .controller import api as weather_api

    api.add_namespace(weather_api, path=f"/{root}")
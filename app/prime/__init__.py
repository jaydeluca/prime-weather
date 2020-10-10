def register_routes(api, app, root="api"):
    from .controller import api as prime_api

    api.add_namespace(prime_api, path=f"/{root}")

def register_routes(api, app, root="api"):
    from app.prime import register_routes as attach_prime

    attach_prime(api, app)
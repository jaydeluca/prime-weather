def register_routes(api, app, root="api"):
    from app.prime import register_routes as attach_prime
    from app.weather import register_routes as attach_weather

    attach_prime(api, app)
    attach_weather(api, app)
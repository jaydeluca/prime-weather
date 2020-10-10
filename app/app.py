from flask import Flask, jsonify, render_template
import logging, sys

from flask_restx import Api


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask("app")
    app.config.from_object(config_by_name[env or "test"])
    register_errorhandlers(app)
    configure_logger(app)
    api = Api(app, title="test", version="0.1.0")
    register_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
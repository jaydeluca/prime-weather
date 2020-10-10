from flask import Flask, jsonify, render_template
import logging, sys, json_logging
import pkg_resources
from elasticapm.contrib.flask import ElasticAPM

from flask_restx import Api


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app_version = pkg_resources.require("app")[0].version
    app_info = {
        "name": __name__.split(".")[1],
        "version": app_version
    }

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])

    api = Api(app, title=__name__, version=app_version)
    register_routes(api, app)

    # Telemetry
    app.config['ELASTIC_APM'] = {
        'SERVICE_NAME': app.config["SERVICE_NAME"],
        'SECRET_TOKEN': app.config["SECRET_TOKEN"],
    }
    apm = ElasticAPM(app)
    register_errorhandlers(app)
    configure_logger(app)

    @app.route("/health")
    def health():
        return jsonify(app_info)

    @app.route("/version")
    def version():
        return jsonify({"version": app_version})

    register_routes(api, app)

    return app


def configure_logger(app):
    """Configure loggers."""
    json_logging.init_flask(enable_json=True)
    json_logging.init_request_instrument(app)

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
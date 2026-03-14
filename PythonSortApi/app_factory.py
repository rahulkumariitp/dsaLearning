"""
Main Flask application factory and setup
Initializes the application and configures extensions
"""

from flask import Flask
from flask_cors import CORS
from config import Config
from routes import sort_bp


def create_app(config: Config = None) -> Flask:
    """
    Application factory function
    Creates and configures the Flask application
    
    Args:
        config: Config object (uses environment config if not provided)
        
    Returns:
        Configured Flask application
    """
    # Use provided config or create from environment
    if config is None:
        config = Config.from_env()
    
    # Create Flask app
    app = Flask(__name__)
    
    # Configure app
    app.config["DEBUG"] = config.DEBUG
    app.config["ENV"] = config.FLASK_ENV
    
    # Enable CORS
    CORS(app, resources={r"/sort/*": {"origins": config.CORS_ORIGINS}})
    
    # Register blueprints
    app.register_blueprint(sort_bp)
    
    # Store config in app context
    app.config["APP_CONFIG"] = config
    
    return app


def create_app_with_custom_config(
    host: str = "0.0.0.0",
    port: int = 5002,
    debug: bool = True,
    cors_origins: str = "*"
) -> Flask:
    """
    Create app with custom configuration
    
    Args:
        host: Server host
        port: Server port
        debug: Debug mode
        cors_origins: CORS origins
        
    Returns:
        Configured Flask application
    """
    config = Config(
        HOST=host,
        PORT=port,
        DEBUG=debug,
        CORS_ORIGINS=cors_origins
    )
    return create_app(config)

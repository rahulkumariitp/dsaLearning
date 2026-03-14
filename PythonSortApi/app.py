"""
Python Sorting API Entry Point
Main application runner
"""

from config import Config
from app_factory import create_app

# Load configuration from environment
config = Config.from_env()

# Create and configure the Flask application
app = create_app(config)

if __name__ == '__main__':
    print(f"Starting Sorting API Server...")
    print(f"Configuration: {config.to_dict()}")
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

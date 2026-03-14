"""
Configuration file for Flask application
Manages all configuration settings and environment variables
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Application configuration settings"""
    
    # Flask settings
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # Server settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "5002"))
    
    # CORS settings
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "*")
    
    # API settings
    API_PREFIX: str = "/sort"
    API_VERSION: str = "v1"
    
    @classmethod
    def from_env(cls) -> "Config":
        """Create config from environment variables"""
        return cls()
    
    def to_dict(self) -> dict:
        """Convert config to dictionary"""
        return {
            "flask_env": self.FLASK_ENV,
            "debug": self.DEBUG,
            "host": self.HOST,
            "port": self.PORT,
            "cors_origins": self.CORS_ORIGINS
        }

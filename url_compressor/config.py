import os
import sys
import random
import logging

LOGGER = logging.getLogger(__name__)

class Config:
    DEBUG = False
    TESTING = False
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}


from django.apps import AppConfig
from importlib import import_module


class ControlConfig(AppConfig):
    name = 'control'

    def ready(self):
        import_module('control.signals')

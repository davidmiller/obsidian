"""
obsidian - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'obsidian.schema'
    flow_module   = 'obsidian.flow'
    javascripts   = [
        'js/obsidian/routes.js',
        'js/opal/controllers/discharge.js'
    ]
    styles = [
        'css/obsidian.css'
    ]

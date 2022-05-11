from flask import render_template
from python_framework import ResourceManager
from queue_manager_api import QueueManager

import ModelAssociation
from config import TheNewsConfig


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL, managerList=[
    QueueManager()
])
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route(f'{app.api.baseUrl}')
def home():
    return render_template(TheNewsConfig.TODAYS_NEWS_FILE_NAME, staticUrl=ResourceManager.getApiStaticUrl(app))

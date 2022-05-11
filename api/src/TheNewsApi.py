from flask import render_template
from python_framework import ResourceManager
from queue_manager_api import QueueManager

import ModelAssociation


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL, managerList=[
    QueueManager()
])
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route(f'{app.api.baseUrl}')
def home():
    try:
        return render_template(
            app.api.resource.service.theNews.getTodayNewsHtmlFileName(),
            staticUrl=ResourceManager.getApiStaticUrl(app)
        )
    except Exception as exception:
        print(exception)
    return {'message', 'Today news not found'}, 404

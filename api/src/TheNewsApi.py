from flask import render_template, send_from_directory
from python_helper import Constant as c
from python_helper import log, EnvironmentHelper
from python_framework import ResourceManager, FlaskUtil, LogConstant
from queue_manager_api import QueueManager

import ModelAssociation


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL, managerList=[
    QueueManager()
])


app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route(f'/the-news')
def todayNews():
    log.info(todayNews, f'{LogConstant.CONTROLLER_SPACE}{FlaskUtil.safellyGetVerb()}{c.SPACE_DASH_SPACE}{FlaskUtil.safellyGetUrl()}')
    try:
        return render_template(
            app.api.resource.service.theNews.getTodayNewsHtmlFileName(),
            staticUrl=ResourceManager.getApiStaticUrl(app).replace('studies', 'cdn')
        )
    except Exception as exception:
        MESSAGE_KEY = 'message'
        responseDto = {MESSAGE_KEY: 'Today news not found'}
        log.error(todayNews, responseDto.get(MESSAGE_KEY), exception=exception)
    return responseDto, 404


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        EnvironmentHelper.OS.path.join(app.root_path, f'static{EnvironmentHelper.OS_SEPARATOR}images'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

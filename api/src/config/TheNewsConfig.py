from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

from python_helper import EnvironmentHelper

from constant import NewsConstant


FOLDER_NAME = f'api{EnvironmentHelper.OS_SEPARATOR}src{EnvironmentHelper.OS_SEPARATOR}view'
TODAY_NEWS_FILE_PREFIX_NAME = NewsConstant.FILE_PREFIX_NAME
TODAY_NEWS_FILE_EXTENSION = NewsConstant.FILE_EXTENSION
TODAY_NEWS_EMAIL_AMOUNT = 1
TODAY_NEWS_PUBLIC_URL = globalsInstance.getSetting('public-the-news-api.today-news.url')

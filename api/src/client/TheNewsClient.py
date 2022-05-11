import os

from python_helper import log
from python_framework import Client, ClientMethod, WebBrowser

from config import TheNewsConfig


class FileManager:

    def __init__(self, config):
        self.config = config

    def writeContent(self, filename, fileUri, content, operation):
        # uri = os.path.join(self.config.FOLDER_NAME, fileUri)
        uri = self.config.FOLDER_NAME
        if not os.path.isdir(uri):
            os.mkdir(uri)
        filepath = os.path.join(uri, filename)
        try:
            open(filepath, operation).write(content)
        except Exception as exception:
            log.failure(self.writeContent, f'Not possible to write content. Content: {content}, operation: {operation}, exception: {exception}')
        # WebBrowser.openUrl(filepath)
        return filepath

@Client()
class TheNewsClient:

    manager = FileManager(TheNewsConfig)

    @ClientMethod()
    def writeContent(self, filename, fileUri, content, operation):
        self.manager.writeContent(filename, fileUri, content, operation)

from timeside.core import implements, interfacedoc
from timeside.core.provider import Provider
from timeside.core.api import IProvider
from timeside.core.tools.utils import slugify

import os
from requests import get


class DeezerPreview(Provider):
    """Deezer Plugin to retrieve deezer's 30 seconds tracks preview"""
    implements(IProvider)

    @staticmethod
    @interfacedoc
    def id():
        return 'deezer_preview'

    @staticmethod
    @interfacedoc
    def name():
        return "Deezer Preview"

    @staticmethod
    @interfacedoc
    def ressource_access():
        return True

    @interfacedoc
    def get_source_from_id(self, external_id, path, download=False):
        request_url = 'https://api.deezer.com/track/' + external_id
        request_json = get(request_url).json()
        source_uri = request_json['preview']
        if download:
            file_name = request_json['artist']['name'] + '-' + request_json['title_short'] + '-' + external_id
            file_name = slugify(file_name) + '.mp3'
            file_path = os.path.join(path,file_name)
            r = get(source_uri)
            if not os.path.exists(path):
                os.makedirs(path)
            with open(file_path,'wb') as f:
                f.write(r.content)
                f.close()
            return file_path
        else:
            return source_uri

    @interfacedoc
    def get_source_from_url(self, url, path, download=False):
        deezer_track_id = self.get_id_from_url(url)
        return self.get_source_from_id(deezer_track_id, path, download)

    @interfacedoc
    def get_id_from_url(self, url):
        return url.split("/")[-1:][0]
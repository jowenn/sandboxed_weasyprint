import connexion
from swagger_server.models.body import Body
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from swagger_server.util import deserialize_date, deserialize_datetime
from weasyprint import HTML
import base64
import magic
import sys
from urllib.parse import urlparse

def html2pdf(body):
    """
    Convert html with addtional files to pdf
    
    :param body: data for conversion
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())

    extra_files={}
    for ef in body.extrafiles:
        data=base64.decodebytes(ef.content.encode("utf-8"))
        mime=magic.from_buffer(data,True)
        extra_files[ef.name]=dict(string=data,mime_type=mime)
    def my_data_fetcher(url:str):
        print("requested:",url,file=sys.stderr)
        parsed=urlparse(url)
        path=parsed.path
        while path.startswith("/"):
            path=path[1:]
        print("calculated path:",path,file=sys.stderr)
        item=extra_files.get(path, None)
        if item is None:
            print("element not found:",url,file=sys.stderr)
            raise ValueError("Data not found: %s" % path)
        return item
    print("starting to generate",file=sys.stderr)
    html=HTML(string=base64.decodebytes(body.basedocument.encode("utf-8")),
              url_fetcher=my_data_fetcher, base_url="internal:///renderit.html")
    return html.write_pdf()

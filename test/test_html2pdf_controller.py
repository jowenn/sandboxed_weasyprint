# coding: utf-8

from __future__ import absolute_import

from models.body import Body
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestHtml2pdfController(BaseTestCase):
    """ Html2pdfController integration test stubs """

    def test_html2pdf(self):
        """
        Test case for html2pdf

        Convert html with addtional files to pdf
        """
        body = Body()
        response = self.client.open('/v1/html2pdf',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

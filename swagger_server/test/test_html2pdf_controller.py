# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHtml2pdfController(BaseTestCase):
    """Html2pdfController integration test stubs"""

    def test_html2pdf(self):
        """Test case for html2pdf

        Convert html with addtional files to pdf
        """
        body = Body()
        response = self.client.open(
            '/v1/html2pdf',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

# coding: utf-8

from __future__ import absolute_import
#from swagger_server.models.binary import Binary
from models.html2pdf_extrafiles import Html2pdfExtrafiles
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from util import deserialize_model


class Body(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, basedocument: bytes=None, extrafiles: List[Html2pdfExtrafiles]=None):
        """
        Body - a model defined in Swagger

        :param basedocument: The basedocument of this Body.
        :type basedocument: Binary
        :param extrafiles: The extrafiles of this Body.
        :type extrafiles: List[Html2pdfExtrafiles]
        """
        self.swagger_types = {
            'basedocument': bytes,
            'extrafiles': List[Html2pdfExtrafiles]
        }

        self.attribute_map = {
            'basedocument': 'basedocument',
            'extrafiles': 'extrafiles'
        }

        self._basedocument = basedocument
        self._extrafiles = extrafiles

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.
        :rtype: Body
        """
        return deserialize_model(dikt, cls)

    @property
    def basedocument(self) -> bytes:
        """
        Gets the basedocument of this Body.

        :return: The basedocument of this Body.
        :rtype: Binary
        """
        return self._basedocument

    @basedocument.setter
    def basedocument(self, basedocument: bytes):
        """
        Sets the basedocument of this Body.

        :param basedocument: The basedocument of this Body.
        :type basedocument: Binary
        """
        if basedocument is None:
            raise ValueError("Invalid value for `basedocument`, must not be `None`")

        self._basedocument = basedocument

    @property
    def extrafiles(self) -> List[Html2pdfExtrafiles]:
        """
        Gets the extrafiles of this Body.

        :return: The extrafiles of this Body.
        :rtype: List[Html2pdfExtrafiles]
        """
        return self._extrafiles

    @extrafiles.setter
    def extrafiles(self, extrafiles: List[Html2pdfExtrafiles]):
        """
        Sets the extrafiles of this Body.

        :param extrafiles: The extrafiles of this Body.
        :type extrafiles: List[Html2pdfExtrafiles]
        """

        self._extrafiles = extrafiles


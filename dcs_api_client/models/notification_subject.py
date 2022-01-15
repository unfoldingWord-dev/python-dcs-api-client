# coding: utf-8

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.15.10+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_api_client.configuration import Configuration


class NotificationSubject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'latest_comment_url': 'str',
        'state': 'StateType',
        'title': 'str',
        'type': 'NotifySubjectType',
        'url': 'str'
    }

    attribute_map = {
        'latest_comment_url': 'latest_comment_url',
        'state': 'state',
        'title': 'title',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, latest_comment_url=None, state=None, title=None, type=None, url=None, _configuration=None):  # noqa: E501
        """NotificationSubject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._latest_comment_url = None
        self._state = None
        self._title = None
        self._type = None
        self._url = None
        self.discriminator = None

        if latest_comment_url is not None:
            self.latest_comment_url = latest_comment_url
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def latest_comment_url(self):
        """Gets the latest_comment_url of this NotificationSubject.  # noqa: E501


        :return: The latest_comment_url of this NotificationSubject.  # noqa: E501
        :rtype: str
        """
        return self._latest_comment_url

    @latest_comment_url.setter
    def latest_comment_url(self, latest_comment_url):
        """Sets the latest_comment_url of this NotificationSubject.


        :param latest_comment_url: The latest_comment_url of this NotificationSubject.  # noqa: E501
        :type: str
        """

        self._latest_comment_url = latest_comment_url

    @property
    def state(self):
        """Gets the state of this NotificationSubject.  # noqa: E501


        :return: The state of this NotificationSubject.  # noqa: E501
        :rtype: StateType
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NotificationSubject.


        :param state: The state of this NotificationSubject.  # noqa: E501
        :type: StateType
        """

        self._state = state

    @property
    def title(self):
        """Gets the title of this NotificationSubject.  # noqa: E501


        :return: The title of this NotificationSubject.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NotificationSubject.


        :param title: The title of this NotificationSubject.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this NotificationSubject.  # noqa: E501


        :return: The type of this NotificationSubject.  # noqa: E501
        :rtype: NotifySubjectType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationSubject.


        :param type: The type of this NotificationSubject.  # noqa: E501
        :type: NotifySubjectType
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this NotificationSubject.  # noqa: E501


        :return: The url of this NotificationSubject.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NotificationSubject.


        :param url: The url of this NotificationSubject.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NotificationSubject, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationSubject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationSubject):
            return True

        return self.to_dict() != other.to_dict()

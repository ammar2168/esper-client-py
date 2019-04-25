# coding: utf-8

"""
    Esper Manage API

    # Introduction Esper Manage APIs for Cloud are a set of REST-based APIs that help you programmatically control and monitor your enterprise's dedicated Esper endpoint. Using these APIs, one can orchestrate & manage devices that have been provisioned against your endpoint. Furthermore, this API allows you to manage android applications that get installed on such devices. To read more about the various capabilities of Esper endpoints and Esper managed devices, please visit [esper.io](https://esper.io). This guide describes all the available APIs in detail, along with code samples for you to quickly ramp up to using them.  You can find out more about Esper at [https://esper.io](https://esper.io)  We've done our best to keep this document up to date, but if you find any issues, please reach out to us at developer@esper.io.  # SDK    You are welcome to use your favorite HTTP/REST library for your programming language in order to use these APIs, or you can use our official SDK (currently available in [python](https://github.com/esper-io/esper-client-py)) to do so.   # Authentication Client needs to send authentication details to access APIs. Following authentication schemes are supported:  #### Basic Authentication Client can use username and password to authenticate. These are your developer account credentials. For example, the client sends HTTP requests with the Authorization header that contains the word `Basic` followed by a space and a base64-encoded string `username:password`. ##### Base64 encoding Bash  ``` echo 'username:password' | base64 ```  Powershell  ``` [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes(\"username:password\")) ```  **Example request** ```bash curl -X GET \\   https://DOMAIN.shoonyacloud.com/api/enterprise/<enterprise_id>/device/ \\   -H 'Authorization: Basic cl0ZWFkbWluOnNpdG1pbjEyMyQ=' \\   -H 'Content-Type: application/json' \\ ``` You can read more about basic authentication scheme  [here](https://swagger.io/docs/specification/authentication/basic-authentication/)  # Errors The API uses standard HTTP status codes to indicate success or failure. All error responses will have a JSON body in the following format  ``` {   \"errors\": [],   \"message\": \"error message\",   \"status\": 400 } ``` * `errors` -  List of error details * `message` - Error description * `status` - HTTP status code   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@esper.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from esperclient.models.device_custom import DeviceCustom  # noqa: F401,E501


class DeviceStatusTiles(object):
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
        'id': 'int',
        'device': 'DeviceCustom',
        'network_info': 'str',
        'model': 'str',
        'location': 'str',
        'battery_level': 'float',
        'security_state': 'int',
        'security_reason': 'int',
        'security_advise': 'int',
        'wifi_ssid': 'str',
        'updated_on': 'datetime',
        'created_on': 'datetime',
        'is_active': 'bool',
        'is_gms': 'bool',
        'enterprise': 'str'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'network_info': 'networkInfo',
        'model': 'model',
        'location': 'location',
        'battery_level': 'battery_level',
        'security_state': 'security_state',
        'security_reason': 'security_reason',
        'security_advise': 'security_advise',
        'wifi_ssid': 'wifi_ssid',
        'updated_on': 'updated_on',
        'created_on': 'created_on',
        'is_active': 'is_active',
        'is_gms': 'is_gms',
        'enterprise': 'enterprise'
    }

    def __init__(self, id=None, device=None, network_info=None, model=None, location=None, battery_level=None, security_state=None, security_reason=None, security_advise=None, wifi_ssid=None, updated_on=None, created_on=None, is_active=None, is_gms=None, enterprise=None):  # noqa: E501
        """DeviceStatusTiles - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device = None
        self._network_info = None
        self._model = None
        self._location = None
        self._battery_level = None
        self._security_state = None
        self._security_reason = None
        self._security_advise = None
        self._wifi_ssid = None
        self._updated_on = None
        self._created_on = None
        self._is_active = None
        self._is_gms = None
        self._enterprise = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.device = device
        self.network_info = network_info
        if model is not None:
            self.model = model
        if location is not None:
            self.location = location
        if battery_level is not None:
            self.battery_level = battery_level
        if security_state is not None:
            self.security_state = security_state
        if security_reason is not None:
            self.security_reason = security_reason
        if security_advise is not None:
            self.security_advise = security_advise
        if wifi_ssid is not None:
            self.wifi_ssid = wifi_ssid
        if updated_on is not None:
            self.updated_on = updated_on
        if created_on is not None:
            self.created_on = created_on
        if is_active is not None:
            self.is_active = is_active
        if is_gms is not None:
            self.is_gms = is_gms
        self.enterprise = enterprise

    @property
    def id(self):
        """Gets the id of this DeviceStatusTiles.  # noqa: E501


        :return: The id of this DeviceStatusTiles.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceStatusTiles.


        :param id: The id of this DeviceStatusTiles.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """Gets the device of this DeviceStatusTiles.  # noqa: E501


        :return: The device of this DeviceStatusTiles.  # noqa: E501
        :rtype: DeviceCustom
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DeviceStatusTiles.


        :param device: The device of this DeviceStatusTiles.  # noqa: E501
        :type: DeviceCustom
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def network_info(self):
        """Gets the network_info of this DeviceStatusTiles.  # noqa: E501


        :return: The network_info of this DeviceStatusTiles.  # noqa: E501
        :rtype: str
        """
        return self._network_info

    @network_info.setter
    def network_info(self, network_info):
        """Sets the network_info of this DeviceStatusTiles.


        :param network_info: The network_info of this DeviceStatusTiles.  # noqa: E501
        :type: str
        """
        if network_info is None:
            raise ValueError("Invalid value for `network_info`, must not be `None`")  # noqa: E501

        self._network_info = network_info

    @property
    def model(self):
        """Gets the model of this DeviceStatusTiles.  # noqa: E501


        :return: The model of this DeviceStatusTiles.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DeviceStatusTiles.


        :param model: The model of this DeviceStatusTiles.  # noqa: E501
        :type: str
        """
        if model is not None and len(model) > 255:
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501
        if model is not None and len(model) < 1:
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `1`")  # noqa: E501

        self._model = model

    @property
    def location(self):
        """Gets the location of this DeviceStatusTiles.  # noqa: E501


        :return: The location of this DeviceStatusTiles.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DeviceStatusTiles.


        :param location: The location of this DeviceStatusTiles.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def battery_level(self):
        """Gets the battery_level of this DeviceStatusTiles.  # noqa: E501


        :return: The battery_level of this DeviceStatusTiles.  # noqa: E501
        :rtype: float
        """
        return self._battery_level

    @battery_level.setter
    def battery_level(self, battery_level):
        """Sets the battery_level of this DeviceStatusTiles.


        :param battery_level: The battery_level of this DeviceStatusTiles.  # noqa: E501
        :type: float
        """

        self._battery_level = battery_level

    @property
    def security_state(self):
        """Gets the security_state of this DeviceStatusTiles.  # noqa: E501

        Security state enum * SECURE = 1 * LOW_RISK = 10 * MEDIUM_RISK = 20 * HIGH_RISK = 30 * DEVICE_STATE_UNSPECIFIED = 100   # noqa: E501

        :return: The security_state of this DeviceStatusTiles.  # noqa: E501
        :rtype: int
        """
        return self._security_state

    @security_state.setter
    def security_state(self, security_state):
        """Sets the security_state of this DeviceStatusTiles.

        Security state enum * SECURE = 1 * LOW_RISK = 10 * MEDIUM_RISK = 20 * HIGH_RISK = 30 * DEVICE_STATE_UNSPECIFIED = 100   # noqa: E501

        :param security_state: The security_state of this DeviceStatusTiles.  # noqa: E501
        :type: int
        """

        self._security_state = security_state

    @property
    def security_reason(self):
        """Gets the security_reason of this DeviceStatusTiles.  # noqa: E501

        Security reason enum * BOOTLOADER_UNLOCKED = 1 * CUSTOM_ROM_INSTALLED_OR_BOOTLOADER_UNLOCKED= 10 * DEVICE_ROOTED_OR_TAMPERED = 20 * OUTDATED_SECURITY_PATCHES = 30 * ERROR_FETCHING_VALUES = 40 * NOT_APPLICABLE = 50   # noqa: E501

        :return: The security_reason of this DeviceStatusTiles.  # noqa: E501
        :rtype: int
        """
        return self._security_reason

    @security_reason.setter
    def security_reason(self, security_reason):
        """Sets the security_reason of this DeviceStatusTiles.

        Security reason enum * BOOTLOADER_UNLOCKED = 1 * CUSTOM_ROM_INSTALLED_OR_BOOTLOADER_UNLOCKED= 10 * DEVICE_ROOTED_OR_TAMPERED = 20 * OUTDATED_SECURITY_PATCHES = 30 * ERROR_FETCHING_VALUES = 40 * NOT_APPLICABLE = 50   # noqa: E501

        :param security_reason: The security_reason of this DeviceStatusTiles.  # noqa: E501
        :type: int
        """

        self._security_reason = security_reason

    @property
    def security_advise(self):
        """Gets the security_advise of this DeviceStatusTiles.  # noqa: E501

        Security advice enum * LOCK_BOOTLOADER = 1 * RESTORE_TO_FACTORY_ROM = 10 * UPDATE_SECURITY_PATCHES = 20 * NOT_APPLICABLE = 30   # noqa: E501

        :return: The security_advise of this DeviceStatusTiles.  # noqa: E501
        :rtype: int
        """
        return self._security_advise

    @security_advise.setter
    def security_advise(self, security_advise):
        """Sets the security_advise of this DeviceStatusTiles.

        Security advice enum * LOCK_BOOTLOADER = 1 * RESTORE_TO_FACTORY_ROM = 10 * UPDATE_SECURITY_PATCHES = 20 * NOT_APPLICABLE = 30   # noqa: E501

        :param security_advise: The security_advise of this DeviceStatusTiles.  # noqa: E501
        :type: int
        """

        self._security_advise = security_advise

    @property
    def wifi_ssid(self):
        """Gets the wifi_ssid of this DeviceStatusTiles.  # noqa: E501


        :return: The wifi_ssid of this DeviceStatusTiles.  # noqa: E501
        :rtype: str
        """
        return self._wifi_ssid

    @wifi_ssid.setter
    def wifi_ssid(self, wifi_ssid):
        """Sets the wifi_ssid of this DeviceStatusTiles.


        :param wifi_ssid: The wifi_ssid of this DeviceStatusTiles.  # noqa: E501
        :type: str
        """
        if wifi_ssid is not None and len(wifi_ssid) > 255:
            raise ValueError("Invalid value for `wifi_ssid`, length must be less than or equal to `255`")  # noqa: E501
        if wifi_ssid is not None and len(wifi_ssid) < 1:
            raise ValueError("Invalid value for `wifi_ssid`, length must be greater than or equal to `1`")  # noqa: E501

        self._wifi_ssid = wifi_ssid

    @property
    def updated_on(self):
        """Gets the updated_on of this DeviceStatusTiles.  # noqa: E501


        :return: The updated_on of this DeviceStatusTiles.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this DeviceStatusTiles.


        :param updated_on: The updated_on of this DeviceStatusTiles.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def created_on(self):
        """Gets the created_on of this DeviceStatusTiles.  # noqa: E501


        :return: The created_on of this DeviceStatusTiles.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceStatusTiles.


        :param created_on: The created_on of this DeviceStatusTiles.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def is_active(self):
        """Gets the is_active of this DeviceStatusTiles.  # noqa: E501


        :return: The is_active of this DeviceStatusTiles.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this DeviceStatusTiles.


        :param is_active: The is_active of this DeviceStatusTiles.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_gms(self):
        """Gets the is_gms of this DeviceStatusTiles.  # noqa: E501


        :return: The is_gms of this DeviceStatusTiles.  # noqa: E501
        :rtype: bool
        """
        return self._is_gms

    @is_gms.setter
    def is_gms(self, is_gms):
        """Sets the is_gms of this DeviceStatusTiles.


        :param is_gms: The is_gms of this DeviceStatusTiles.  # noqa: E501
        :type: bool
        """

        self._is_gms = is_gms

    @property
    def enterprise(self):
        """Gets the enterprise of this DeviceStatusTiles.  # noqa: E501


        :return: The enterprise of this DeviceStatusTiles.  # noqa: E501
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this DeviceStatusTiles.


        :param enterprise: The enterprise of this DeviceStatusTiles.  # noqa: E501
        :type: str
        """
        if enterprise is None:
            raise ValueError("Invalid value for `enterprise`, must not be `None`")  # noqa: E501

        self._enterprise = enterprise

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
        if issubclass(DeviceStatusTiles, dict):
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
        if not isinstance(other, DeviceStatusTiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

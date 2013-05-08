"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from os import path
from cafe.drivers.unittest.fixtures import BaseTestFixture
from cloudcafe.cloudkeep.barbican.client import VersionClient
from cloudcafe.cloudkeep.config import MarshallingConfig, CloudKeepConfig


class BarbicanFixture(BaseTestFixture):

    @classmethod
    def setUpClass(cls):
        super(BarbicanFixture, cls).setUpClass()
        cls.marshalling = MarshallingConfig()
        cls.cloudkeep = CloudKeepConfig()

    def get_id(self, request):
        """
        Helper function to extract the producer id from location header
        """
        self.assertEqual(request.status_code, 201, 'Invalid response code')
        location = request.headers.get('location')
        extracted_id = int(path.split(location)[1])
        return extracted_id


class VersionFixture(BarbicanFixture):

    @classmethod
    def setUpClass(cls):
        super(VersionFixture, cls).setUpClass()
        cls.client = VersionClient(
            url=cls.cloudkeep.base_url,
            serialize_format=cls.marshalling.serializer,
            deserialize_format=cls.marshalling.deserializer)

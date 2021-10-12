from rest_framework import status
from rest_framework.reverse import reverse

from tests.test_resource_tracker.test_api.base_test_api import BaseTestAPI


class TestAttributeDefinitionDelete(BaseTestAPI):

    def setUp(self):
        super(TestAttributeDefinitionDelete, self).setUp()
        self.url = reverse('api_attribute_definition_retrieve_update_delete',
                           args=[self.rg_physical_servers.id,
                                 self.rg_physical_servers_cpu_attribute.id])

    def test_attribute_definition_delete(self):
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_cannot_delete_attribute_definition_when_wrong_rg(self):
        url = reverse('api_attribute_definition_retrieve_update_delete',
                      args=[self.rg_ocp_projects.id,
                            self.rg_physical_servers_cpu_attribute.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
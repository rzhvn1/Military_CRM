from django.contrib.auth.models import User, Group
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from .models import Document
from .factory import populate_test_db_users, populate_test_db_docs
# Create your tests here.

class TestDocumentRulesGet(APITestCase):

    # fucntion for setting up
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('documents-list')
        # create user and group
        populate_test_db_users(User, Group)
        # create docs for users
        populate_test_db_docs(Document)

    # all the GET tests for common-user
    def test_get_common_permissions_public(self):
        self.client.login(username='common', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='public document', status_code=200)

    def test_get_common_no_permissions_private(self):
        self.client.login(username='common', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertNotContains(self.response, text='private document', status_code=200)

    def test_get_common_no_permissions_secret(self):
        self.client.login(username='common', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertNotContains(self.response, text='secret document', status_code=200)

    def test_get_common_no_permissions_top_secret(self):
        self.client.login(username='common', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertNotContains(self.response, text='top-secret document', status_code=200)

    # all the GET test for sergeant-user
    def test_get_sergeant_permissions_public(self):
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='public document', status_code=200)

    def test_get_sergeant_permissions_private(self):
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='private document', status_code=200)

    def test_get_sergeant_no_permissions_secret(self):
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertNotContains(self.response, text='secret document', status_code=200)

    def test_get_sergeant_no_permissions_top_secret(self):
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertNotContains(self.response, text='top-secret document', status_code=200)

    # all the GET tests for general-user
    def test_get_general_permissions_public(self):
        self.client.login(username='general', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='public document', status_code=200)

    def test_get_general_permissions_private(self):
        self.client.login(username='general', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='private document', status_code=200)

    def test_get_general_permissions_secret(self):
        self.client.login(username='general', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='secret document', status_code=200)

    def test_get_general_permissions_top_secret(self):
        self.client.login(username='general', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertNotContains(self.response, text='top-secret', status_code=200)

    # all the GET tests for president-user
    def test_get_president_permissions_public(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='public document', status_code=200)

    def test_get_president_permissions_private(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='private document', status_code=200)

    def test_get_president_permissions_secret(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='secret document', status_code=200)

    def test_get_president_permissions_top_secret(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response, text='top-secret document', status_code=200)


class TestDocumentRulesPost(APITestCase):

    # fucntion for setting up
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('documents-list')
        # create user and group
        populate_test_db_users(User, Group)
        # create docs for users
        populate_test_db_docs(Document)

    # all the POST test for common-user
    def test_post_common_permissions_public(self):
        self.client.login(username='common', password='123456')
        data = {
            'title':'title',
            'text':'text',
            'status':'active',
            'date_expired':'2020-06-06',
            'document_root':'public'
        }
        self.response = self.client.post(self.url,data)
        print(self.response.json())
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_common_permissions_private(self):
        self.client.login(username='common', password='123456')
        data = {
            'title':'title',
            'text':'text',
            'status':'active',
            'date_expired':'2020-06-06',
            'document_root':'private'
        }
        self.response = self.client.post(self.url,data)
        print(self.response.json())
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_common_permissions_secret(self):
        self.client.login(username='common', password='123456')
        data = {
            'title':'title',
            'text':'text',
            'status':'active',
            'date_expired':'2020-06-06',
            'document_root':'secret'
        }
        self.response = self.client.post(self.url,data)
        print(self.response.json())
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_common_permissions_top_secret(self):
        self.client.login(username='common', password='123456')
        data = {
            'title':'title',
            'text':'text',
            'status':'active',
            'date_expired':'2020-06-06',
            'document_root':'top-secret'
        }
        self.response = self.client.post(self.url,data)
        print(self.response.json())
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    # all the POST tests for sergeant-user
    def test_post_sergeant_permissions_public(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'public'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_sergeant_permissions_private(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'private'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_sergeant_permissions_secret(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'secret'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_sergeant_permissions_top_secret(self):
        self.client.login(username='sergeant', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'top_secret'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertNotEqual(self.response.status_code, status.HTTP_201_CREATED)


    # all the POST tests for general-user
    def test_post_general_permissions_public(self):
        self.client.login(username='general', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'public'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_general_permissions_private(self):
        self.client.login(username='general', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'private'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_general_permissions_secret(self):
        self.client.login(username='general', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'secret'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_general_permissions_top_secret(self):
        self.client.login(username='general', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'top-secret'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertContains(self.response, text="You have no permission!", status_code=400)

    # all the POST tests for president-user
    def test_post_president_permissions_public(self):
        self.client.login(username='president', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'public'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_president_permissions_private(self):
        self.client.login(username='president', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'private'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_president_permissions_secret(self):
        self.client.login(username='president', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'secret'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_president_permissions_top_secret(self):
        self.client.login(username='president', password='123456')
        data = {
            'title': 'title',
            'text': 'text',
            'status': 'active',
            'date_expired': '2020-06-06',
            'document_root': 'top-secret'
        }
        self.response = self.client.post(self.url, data)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

#TODO
class TestDateExpiredDoc(APITestCase):


    def setUp(self):
        self.client = APIClient()
        # self.url = reverse('documents-detail')
        Document.objects.create(title='not expired doc',
                                date_expired="2021-12-31",document_root='private')
        Document.objects.create(title='expired doc',
                                date_expired="2021-05-09", document_root='private',status='dead')
        populate_test_db_users(User, Group)

    def test_get_not_expired(self):
        self.client.login(username='general',password='123456')
        self.response = self.client.get("http://127.0.0.1:8000/doc/1/")
        print(self.response.json())
        self.assertContains(self.response,'active',status_code=200)

    def test_get_expired(self):
        self.client.login(username='general',password='123456')
        self.response = self.client.get("http://127.0.0.1:8000/doc/2/")
        print(self.response.json())
        self.assertContains(self.response,'Not found',status_code=404)

























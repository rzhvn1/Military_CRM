from django.contrib.auth.models import User, Group
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

# Create your tests here.

# Test for Registration
from accounts.models import Dossier, Car, Education, Warcraft


class TestRegistration(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register-list')
        User.objects.create_user(username='rzhvn', password="Erjan02D35s2km")
        Group.objects.create(name='sergeant')

    # all the tests for registration
    def test_user_create_successfully(self):
        data = {
            "username":"rzhvn1",
            "email":"erzhanmuratov99@gmail.com",
            "password":"Erjan02D35s2km",
            "check_password":"Erjan02D35s2km",
            "user_type":"military",
            "dossier": {
                "full_name": "Erzhan Muratov",
                "date_birth": "1999-06-02",
                "gender": "M",
                "cars": [
                    {
                        "id":1,
                        "mark": "Hyundai",
                        "car_model": "Avante",
                        "year": "2021-05-05",
                        "number": "01KG455AFV",
                        "color": "White",
                        "type": "Private"
                    }
                ],
                "educations": [
                    {
                        "id":2,
                        "start_date": "2021-05-04",
                        "end_date": "2021-06-04",
                        "school_name": "Osh military school",
                        "major": "Tank engineering"
                    }
                ],
                "warcrafts": [
                    {
                        "id":3,
                        "start_date": "2021-06-04",
                        "end_date": "2021-08-04",
                        "military_area": "Osh",
                        "major": "Tankist",
                        "start_pose": "sergeant",
                        "end_pose": "lieutenant"
                    }
                ]
            }
        }
        self.response = self.client.post(self.url, data, format='json')
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_user_create_already_exists(self):
        data = {
            "username": "rzhvn",
            "email": "erzhanmuratov99@gmail.com",
            "password": "Erjan02D35s2km",
            "check_password": "Erjan02D35s2km",
            "user_type": "military",
            "dossier": {
                "full_name": "Erzhan Muratov",
                "date_birth": "1999-06-02",
                "gender": "M",
                "cars": [
                    {
                        "id":1,
                        "mark": "Hyundai",
                        "car_model": "Avante",
                        "year": "2021-05-05",
                        "number": "01KG455AFV",
                        "color": "White",
                        "type": "Private"
                    }
                ],
                "educations": [
                    {
                        "id":2,
                        "start_date": "2021-05-04",
                        "end_date": "2021-06-04",
                        "school_name": "Osh military school",
                        "major": "Tank engineering"
                    }
                ],
                "warcrafts": [
                    {
                        "id":3,
                        "start_date": "2021-06-04",
                        "end_date": "2021-08-04",
                        "military_area": "Osh",
                        "major": "Tankist",
                        "start_pose": "sergeant",
                        "end_pose": "lieutenant"
                    }
                ]
            }
        }
        self.response = self.client.post(self.url, data, format='json')
        print(self.response.json())
        self.assertContains(self.response, text="already exists", status_code=400)

    def test_user_create_digit_password(self):
        data = {
            "username":"rzhvn1",
            "email":"erzhanmuratov99@gmail.com",
            "password":"12345678",
            "check_password":"12345678",
            "user_type":"military",
            "dossier": {
                "full_name": "Erzhan Muratov",
                "date_birth": "1999-06-02",
                "gender": "M",
                "cars": [
                    {
                        "id":1,
                        "mark": "Hyundai",
                        "car_model": "Avante",
                        "year": "2021-05-05",
                        "number": "01KG455AFV",
                        "color": "White",
                        "type": "Private"
                    }
                ],
                "educations": [
                    {
                        "id":2,
                        "start_date": "2021-05-04",
                        "end_date": "2021-06-04",
                        "school_name": "Osh military school",
                        "major": "Tank engineering"
                    }
                ],
                "warcrafts": [
                    {
                        "id":3,
                        "start_date": "2021-06-04",
                        "end_date": "2021-08-04",
                        "military_area": "Osh",
                        "major": "Tankist",
                        "start_pose": "sergeant",
                        "end_pose": "lieutenant"
                    }
                ]
            }
        }
        self.response = self.client.post(self.url, data, format='json')
        print(self.response.json())
        self.assertContains(self.response, text="number digit", status_code=400)

    def test_user_create_length_password(self):
        data = {
            "username":"rzhvn1",
            "email":"erzhanmuratov99@gmail.com",
            "password":"123456",
            "check_password":"123456",
            "user_type":"military",
            "dossier": {
                "full_name": "Erzhan Muratov",
                "date_birth": "1999-06-02",
                "gender": "M",
                "cars": [
                    {
                        "id":1,
                        "mark": "Hyundai",
                        "car_model": "Avante",
                        "year": "2021-05-05",
                        "number": "01KG455AFV",
                        "color": "White",
                        "type": "Private"
                    }
                ],
                "educations": [
                    {
                        "id":2,
                        "start_date": "2021-05-04",
                        "end_date": "2021-06-04",
                        "school_name": "Osh military school",
                        "major": "Tank engineering"
                    }
                ],
                "warcrafts": [
                    {
                        "id":3,
                        "start_date": "2021-06-04",
                        "end_date": "2021-08-04",
                        "military_area": "Osh",
                        "major": "Tankist",
                        "start_pose": "sergeant",
                        "end_pose": "lieutenant"
                    }
                ]
            }
        }
        self.response = self.client.post(self.url, data, format='json')
        print(self.response.json())
        self.assertContains(self.response, text="more than 8 characters", status_code=400)

    def test_user_create_lower_password(self):
        data = {
            "username":"rzhvn1",
            "email":"erzhanmuratov99@gmail.com",
            "password":"erjanmuratov",
            "check_password":"erjanmuratov",
            "user_type":"military",
            "dossier": {
                "full_name": "Erzhan Muratov",
                "date_birth": "1999-06-02",
                "gender": "M",
                "cars": [
                    {
                        "id":1,
                        "mark": "Hyundai",
                        "car_model": "Avante",
                        "year": "2021-05-05",
                        "number": "01KG455AFV",
                        "color": "White",
                        "type": "Private"
                    }
                ],
                "educations": [
                    {
                        "id":2,
                        "start_date": "2021-05-04",
                        "end_date": "2021-06-04",
                        "school_name": "Osh military school",
                        "major": "Tank engineering"
                    }
                ],
                "warcrafts": [
                    {
                        "id":3,
                        "start_date": "2021-06-04",
                        "end_date": "2021-08-04",
                        "military_area": "Osh",
                        "major": "Tankist",
                        "start_pose": "sergeant",
                        "end_pose": "lieutenant"
                    }
                ]
            }
        }
        self.response = self.client.post(self.url, data, format='json')
        print(self.response.json())
        self.assertContains(self.response, text="lowercase letter", status_code=400)

    def test_user_create_upper_password(self):
        data = {
            "username":"rzhvn1",
            "email":"erzhanmuratov99@gmail.com",
            "password":"ERJANMURATOV",
            "check_password":"ERJANMURATOV",
            "user_type":"military",
            "dossier": {
                "full_name": "Erzhan Muratov",
                "date_birth": "1999-06-02",
                "gender": "M",
                "cars": [
                    {
                        "id":1,
                        "mark": "Hyundai",
                        "car_model": "Avante",
                        "year": "2021-05-05",
                        "number": "01KG455AFV",
                        "color": "White",
                        "type": "Private"
                    }
                ],
                "educations": [
                    {
                        "id":2,
                        "start_date": "2021-05-04",
                        "end_date": "2021-06-04",
                        "school_name": "Osh military school",
                        "major": "Tank engineering"
                    }
                ],
                "warcrafts": [
                    {
                        "id":3,
                        "start_date": "2021-06-04",
                        "end_date": "2021-08-04",
                        "military_area": "Osh",
                        "major": "Tankist",
                        "start_pose": "sergeant",
                        "end_pose": "lieutenant"
                    }
                ]
            }
        }
        self.response = self.client.post(self.url, data, format='json')
        print(self.response.json())
        self.assertContains(self.response, text="uppercase", status_code=400)

    def test_user_create_space_password(self):
        data = {
            "username":"rzhvn1",
            "email":"erzhanmuratov99@gmail.com",
            "password":"Erjan 02D35s2km ",
            "check_password":"Erjan 02D35s2km ",
            "user_type":"military",
            "dossier": {
                "full_name": "Erzhan Muratov",
                "date_birth": "1999-06-02",
                "gender": "M",
                "cars": [
                    {
                        "id":1,
                        "mark": "Hyundai",
                        "car_model": "Avante",
                        "year": "2021-05-05",
                        "number": "01KG455AFV",
                        "color": "White",
                        "type": "Private"
                    }
                ],
                "educations": [
                    {
                        "id":2,
                        "start_date": "2021-05-04",
                        "end_date": "2021-06-04",
                        "school_name": "Osh military school",
                        "major": "Tank engineering"
                    }
                ],
                "warcrafts": [
                    {
                        "id":3,
                        "start_date": "2021-06-04",
                        "end_date": "2021-08-04",
                        "military_area": "Osh",
                        "major": "Tankist",
                        "start_pose": "sergeant",
                        "end_pose": "lieutenant"
                    }
                ]
            }
        }
        self.response = self.client.post(self.url, data, format='json')
        print(self.response.json())
        self.assertContains(self.response, text="spaces", status_code=400)

    def test_user_create_not_equal_password(self):
        data = {
            "username":"rzhvn1",
            "email":"erzhanmuratov99@gmail.com",
            "password":"Erjan02D35s2km",
            "check_password":"Erjan02d35s2km",
            "user_type":"military",
            "dossier": {
                "full_name": "Erzhan Muratov",
                "date_birth": "1999-06-02",
                "gender": "M",
                "cars": [
                    {
                        "id":1,
                        "mark": "Hyundai",
                        "car_model": "Avante",
                        "year": "2021-05-05",
                        "number": "01KG455AFV",
                        "color": "White",
                        "type": "Private"
                    }
                ],
                "educations": [
                    {
                        "id":2,
                        "start_date": "2021-05-04",
                        "end_date": "2021-06-04",
                        "school_name": "Osh military school",
                        "major": "Tank engineering"
                    }
                ],
                "warcrafts": [
                    {
                        "id":3,
                        "start_date": "2021-06-04",
                        "end_date": "2021-08-04",
                        "military_area": "Osh",
                        "major": "Tankist",
                        "start_pose": "sergeant",
                        "end_pose": "lieutenant"
                    }
                ]
            }
        }
        self.response = self.client.post(self.url, data, format='json')
        print(self.response.json())
        self.assertContains(self.response, text="don't match", status_code=400)

#TODO
class TestAuthorization(APITestCase):

    def setUp(self):
        self.url = reverse('authorization')
        User.objects.create(username='rzhvn', password="Erjan02D35s2km")
    #
    # def test_user_login_successfully(self):
    #     data = {
    #         "username":"rzhvn",
    #         "password":"Erjan02D35s2km"
    #     }
    #     self.response = self.client.post(self.url, data)
    #     print(self.response.json())
    #     self.assertEqual(self.response.status_code, status.HTTP_200_OK)


class TestDossier(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('dossier')
        self.user = User.objects.create_user(username='rzhvn', password='Erjan02D35s2km')
        self.dossier = Dossier.objects.create(user = self.user, full_name="Erzhan Muratov", date_birth="1999-06-02", gender="M")
        Car.objects.create(dossier=self.dossier, mark="Hyundai", car_model="Avante", year="2011",
                           number="01KG455AFV", color="White", type="Private")
        Education.objects.create(dossier=self.dossier, start_date="2020-04-03", end_date="2021-04-03",
                                 school_name="24 school", major="math")
        Warcraft.objects.create(dossier=self.dossier, start_date="2019-04-03", end_date="2020-04-03",
                                military_area="Batken", major="CS", start_pose='sergeant', end_pose="general")

    # def test_dossier_put(self):
    #     self.client.login(username='rzhvn', password='Erjan02D35s2km')
    #     data = {
    #         "id": 23,
    #         "full_name": "Erzhannnn Muratov",
    #         "date_birth": "2021-05-19",
    #         "gender": "M",
    #         "cars": [
    #             {
    #                 "id": 14,
    #                 "mark": "Hyundai",
    #                 "car_model": "Avante",
    #                 "year": "2011",
    #                 "number": "01KG455AFV",
    #                 "color": "White",
    #                 "type": "Private"
    #             }
    #         ],
    #         "educations": [
    #             {
    #                 "id": 9,
    #                 "start_date": "2020-04-03",
    #                 "end_date": "2021-04-03",
    #                 "school_name": "24 school",
    #                 "major": "math"
    #             }
    #         ],
    #         "warcrafts": [
    #             {
    #                 "id": 8,
    #                 "start_date": "2019-04-03",
    #                 "end_date": "2020-04-03",
    #                 "military_area": "Batken",
    #                 "major": "CS",
    #                 "start_pose": "sergeant",
    #                 "end_pose": "general"
    #             }
    #         ]
    #     }
    #     self.response = self.client.put(self.url, data)
    #     print(self.response.json())
    #     self.assertContains(self.response, text="Successfully updated!", status_code=200)

    def test_delete(self):
        self.client.login(username='rzhvn', password='Erjan02D35s2km')
        self.response = self.client.delete(self.url)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)






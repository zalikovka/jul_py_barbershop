import json
from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient

from worker_profile.models import WorkerProfile, WorkerCommunications


def _dict_key_quotes(text):
    """ Replaces first two occurrences of double quotes " to single quotes ' in every line
        Is used to print dictionaries formatted according to the project guidelines
        (dict key are in single quotes, texts are in double quotes)
    """
    return '\n'.join([l.replace('"', "'", 2) for l in text.split('\n')])


def dump(response):
    """ Print DRF response data
        Useful for debugging tests. Prints response code and indented JSON data
    :param response: server response provided by DRF testing client (APIClient)
    """

    print("\nURL:", response.request['PATH_INFO'])
    print("Method:", response.request['REQUEST_METHOD'])
    if response.request['QUERY_STRING']:
        print("Query:", response.request['QUERY_STRING'])
    print("\n")
    print("Status code:\n{}\n\nData:\n{}\n".format(
        response.status_code,
        _dict_key_quotes(json.dumps(response.data, indent=4, ensure_ascii=False))
        if hasattr(response, 'data') else None
    ))


class WorkerProfileDetailsAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='aa',
            password='aaa111',
            email='aaatt' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.worker = WorkerProfile.objects.create(first_name='test', second_name='test',position='testbarber',
                                                   phone_number='+111111111111', email='test@gmail.com', worker=self.user.username)

    def test_worker_profile_details(self):
        self.c.login(username='tt', password='111')

        response = self.c.get(
            '/worker_profile/worker_profile/1/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)

    class WorkerProfileDetailsAPITest(TestCase):

        def setUp(self):
            self.c = APIClient()
            user_kw1 = dict(
                username='aaa',
                password='aaa111',
                email='aaatt' + '.com'
            )
            user_kw1['password'] = make_password(user_kw1['password'])
            self.user1 = User.objects.create(**user_kw1)
            self.worker = WorkerProfile.objects.create(first_name='aaatest', second_name='aaatesttest', position='aaatestbarber',
                                                       phone_number='+111111111111', email='aaatest@gmail.com',
                                                       worker=self.user1.username)
            user_kw2 = dict(
                username='tt2',
                password='222',
                email='tt2' + '.com'
            )
            user_kw2['password'] = make_password(user_kw2['password'])
            self.user2 = User.objects.create(**user_kw2)
            self.worker2 = WorkerProfile.objects.create(first_name='test2', second_name='testtest2',
                                                       position='testbarber2',
                                                       phone_number='+222222222222', email='test2@gmail.com',
                                                       worker=self.user2.username)

    def test_worker_profile_details_permission(self):
        self.c.login(username='tt2', password='222')

        response = self.c.get(
            '/worker_profile/worker_profile/1/'
        )
        print('TYT'*20)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)
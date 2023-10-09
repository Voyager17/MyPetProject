
from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User
import requests


res = requests.get(SERVICE_URL)


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)


"""
{'meta': {'pagination': {'total': 2862, 'pages': 287, 'page': 1, 'limit': 10, 'links':
{'previous': None, 'current': 'https://gorest.co.in/public/v1/users?page=1', 'next': 'https://gorest.co.in/public/v1/users?page=2'}}},
 'data': [{'id': 3473466, 'name': 'Anuja Talwar', 'email': 'anuja_talwar@robel-monahan.test', 'gender': 'male', 'status': 'inactive'},
   {'id': 3473464, 'name': 'Fr. Sukanya Jain', 'email': 'sukanya_fr_jain@marquardt.example', 'gender': 'female', 'status': 'inactive'},
   {'id': 3473463, 'name': 'Abhaya Chopra JD', 'email': 'abhaya_jd_chopra@raynor.example', 'gender': 'male', 'status': 'inactive'},
   {'id': 3473462, 'name': 'Dhatri Mukhopadhyay', 'email': 'dhatri_mukhopadhyay@zboncak-schowalter.example', 'gender': 'female', 'status':
   'active'}, {'id': 3473460, 'name': 'Smriti Pillai', 'email': 'pillai_smriti@wisozk.test', 'gender': 'female', 'status': 'active'},
     {'id': 3473459, 'name': 'Manik Mehrotra', 'email': 'mehrotra_manik@fritsch.example', 'gender': 'female', 'status': 'inactive'},
       {'id': 3473458, 'name': 'Amb. Draupadi Naik', 'email': 'naik_draupadi_amb@kirlin.example', 'gender': 'female', 'status': 'active'},
       {'id': 3473456, 'name': 'Inder Adiga', 'email': 'adiga_inder@fay-haley.example', 'gender': 'female', 'status': 'inactive'},
         {'id': 3473455, 'name': 'Abhisyanta Mukhopadhyay Ret.', 'email': 'abhisyanta_ret_mukhopadhyay@bernhard-kreiger.example',
           'gender': 'male', 'status': 'active'}, {'id': 3473454, 'name': 'Mrs. Jagadish Gowda', 'email': 'mrs_gowda_jagadish@prosacco.test',
             'gender': 'male', 'status': 'active'}]
"""  # noqa: E501

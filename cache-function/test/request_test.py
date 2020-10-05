import unittest
import time
import request

BASE_URL = 'https://jsonplaceholder.typicode.com'
COMMENTS_URL = BASE_URL + '/comments'


class Tests(unittest.TestCase):

    def test_cache(self):
        self.assertGreater(_request_load_time(), 0.01)
        self.assertLess(_request_load_time(), 0.01)

    def test_method_get(self):
        self.assertTrue(len(request.get(COMMENTS_URL)))

    def test_method_post(self):
        body = {
            'name': 'Tester',
            'email': 'test@test.com',
            'body': 'lorem ipsum',
            'postId': 1
        }
        self.assertTrue(len(request.post(COMMENTS_URL, data=body)))

    def test_method_put(self):
        body = {
            'id': 1,
            'name': 'Test Eng',
            'email': 'tests@test.com',
            'body': 'lorem impsum impsum',
            'userId': 1
        }
        self.assertTrue(
            len(request.put(f'{COMMENTS_URL}/{body.get("id")}', data=body)))

    def test_method_patch(self):
        id = 1
        body = {
            'body': 'lorem impsum impsum lorem',
        }
        self.assertTrue(len(request.patch(f'{COMMENTS_URL}/{id}', data=body)))

    def test_delete_method(self):
        id = 1,
        self.assertDictEqual(request.delete(f'{COMMENTS_URL}/{id}'), {})


def _request_load_time():
    """ Returns request load time """
    initial = time.time()
    request.get(COMMENTS_URL)
    final = time.time()
    load_time = final - initial
    return load_time


if __name__ == '__main__':
    unittest.main()

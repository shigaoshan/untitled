import allure
import unittest
import warnings
from Lib.httpClient import HttpClient

class Weather(unittest.TestCase):
    def setUp(self) :
        #忽略警告
        warnings.simplefilter("ignore", ResourceWarning)
        super().setUp()
        self.host = 'http://www.weather.com.cn'
        self.ep_path = '/data/cityinfo'
        self.client = HttpClient()

    def test_1(self):
        city_code = '101280601'
        exp_city = '深圳'
        self._test(city_code,exp_city)

    def test_2(self):
        city_code = '101010100'
        exp_city = '北京'
        self._test(city_code,exp_city)

    def test_3(self):
        city_code = '101020100'
        exp_city = '上海'
        self._test(city_code,exp_city)

    def _test(self,city_code,exp_city):
        url = f'{self.host}{self.ep_path}/{city_code}.html'
        response = self.client.Get(url=url)
        act_city = response.json()['weatherinfo']['city']
        print(f'Expect city = {exp_city}, while actual city = {act_city}')
        self.assertEqual(exp_city,act_city,'Expect city = {exp_city}, while actual city = {act_city}')

if __name__ == '__main__':
        unittest.main()
import requests
from bs4 import BeautifulSoup as bs


class parseAuto:

    def __init__(self, cookie, useragent, x_csrf_token):
        self.config = {
            'headers': {
                'accept': '*/*',
                'cookie': cookie,
                'user-agent': useragent,
                'x-csrf-token': x_csrf_token
            },
            'urlListing': 'https://auto.ru/-/ajax/desktop/listing/',
            'cityCode': {
                'Moscow': 213,
                'Ryazan': 11,
                'Sankt-Peterburg': 2,
                'Russia': 225
            }
        }
        self.cars = []

    def request(self, params):
        r = requests.post(url=self.config['urlListing'],
                          data=params,
                          headers=self.config['headers'])
        self.cars.append(r.json()['offers'])
        return r.json()


if __name__ == '__main__':
    obj = parseAuto(cookie="suid=6f7dd7867261146e492a8e4e7509ddab.fb215959e7940d0354eaa2e31eca848f; _ym_uid=1615216201866918173; _ga=GA1.2.1155361267.1615934277; autoruuid=g60463e452st3aldlqlm0cgvunfk1hg8.df0e1e355ab68fb1f9bf77bd824981d0; gids=11; counter_ga_all7=1; yandexuid=9476882891553578318; my=YycCAAEA; autoru_sid=65808656%7C1623710403014.7776000.oEYYR-EVfvLMdX0MfmxkNA.jYi2ToVQ009r6f7h8OqMoOhD2_n0593jNLQ6-VE5z7k; _csrf_token=b61d62577b7d89b4434dd4bc67218403fc7cbbcc96166717; from=google-search; X-Vertis-DC=vla; yuidlt=1; salon_phone_utms=utm_medium%3Dcpc%26utm_source%3Dgoogle_adwords%26utm_campaign%3Did-_place-gsearch_geo-rus-r225_type-history-vin-knk-avtoru%26utm_content%3Didgr-_cat-history-vin-avtoru_obshie-z--proverka-vin_geo-rus-r225; _gid=GA1.2.1394062166.1628430047; _gac_UA-11391377-1=1.1628430047.CjwKCAjwgb6IBhAREiwAgMYKRtRepexXa3SvwxZJuMrrhx3Vj-gT72F_W89dPbWuGeFMVyaP0RQjpBoCdeAQAvD_BwE; hide-proauto-pimple=1; notification_offer_stat_fetched=true; gdpr=0; from_lifetime=1628430192537; _ym_d=1628430192; from=google-search; from_lifetime=1628430566018; Secure,X-Vertis-DC=vla; _ym_d=1628430566; _ym_uid=1615216201866918173",
                    useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                    x_csrf_token="b61d62577b7d89b4434dd4bc67218403fc7cbbcc96166717")
    p = obj.request(params={"catalog_filter": [{"mark": "MERCEDES"}],
                            "section": "all",
                            "category": "cars",
                            "output_type": "list",
                            "geo_radius": 200,
                            "geo_id": [11]})

    i = 2
    while i <= p['pagination']['total_page_count']:
        p = obj.request(params={"catalog_filter": [{"mark": "MERCEDES"}], "section": "all", "category": "cars",
                                "output_type": "list", "page": i, "geo_radius": 200, "geo_id": [11]})
        print(f"Страница { str(i) } обработана!")
import json
import re
from typing import Dict
from rapid_api.request import request_to_api


def search_city(city: str) -> int:
    """Функция поиска ID города по запросу пользователя"""

    request_1 = request_to_api("https://hotels4.p.rapidapi.com/locations/v2/search", {'query': city})
    pattern: str = r'(?<="CITY_GROUP",).+?[\]]'
    find = re.search(pattern, request_1)

    if find:
        data: Dict = json.loads(f"{{{find[0]}}}")

        for id_destination in data['entities']:
            if id_destination['type'] == 'CITY' and id_destination['name'].lower() == city.lower():
                destination_id = int(id_destination['destinationId'])
                return destination_id

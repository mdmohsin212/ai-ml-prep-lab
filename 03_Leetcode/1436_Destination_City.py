class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_count = {}

        for path in paths:
            city_a, city_b = path

            city_count[city_a] = city_count.get(city_a, 0) + 1
            city_count[city_b] = city_count.get(city_b, 0)

        
        for city in city_count:
            if city_count[city] == 0:
                return city
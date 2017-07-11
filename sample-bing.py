from py_ms_cognitive import PyMsCognitiveWebSearch
search_term = "Python Software Foundation"
search_service = PyMsCognitiveWebSearch('c6b756d3b3714362bb690e9520421879', search_term)
first_ten_result = search_service.search(limit=10, format='json')
for jsons in first_ten_result:
    print jsons.json

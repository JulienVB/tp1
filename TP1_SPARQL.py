from datetime import datetime as dt
from re import A
from SPARQLWrapper import SPARQLWrapper, JSON

date_format = "%Y-%m-%dT%H:%M:%SZ"

endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
sparql = SPARQLWrapper(endpoint)

statement = """
SELECT DISTINCT ?person ?personLabel ?dateBirth ?dateDeath WHERE {
    ?person wdt:P27 wd:Q31 .
    ?person wdt:P106 wd:Q116 .
    ?person wdt:P569 ?dateBirth .
    OPTIONAL {?person wdt:P570 ?dateDeath .}
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
}
ORDER BY ?dateBirth
"""

sparql.setQuery(statement)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

rows = results['results']['bindings']
print(f"\n{len(rows)} Belgian monarchs found\n")

for item in results['results']['bindings']:
    try:
        birth_date = dt.strptime(item['dateBirth']['value'], date_format)
        birth_year = birth_date.year
    except ValueError:
        birth_year = "????"
    try:
        death_date = dt.strptime(item['dateDeath']['value'], date_format)
        death_year = death_date.year
    except ValueError: # unknown death date
        death_year = "????"
    except KeyError: # still alive
        death_year = ""
    try:   
        display_monarch = item['personLabel']['value']
        print(display_monarch, birth_year, death_year)
    except ValueError:
        display_monarch = "????"

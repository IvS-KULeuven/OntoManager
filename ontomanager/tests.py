import unittest

from pyramid import testing

TESTQUERY = """SELECT ?company ?companyName ?m ?id ?comment (COUNT(?instance) AS ?count)
WHERE {
    ?m        rdf:type             elec:IoModuleType .
    ?m        man:hasId            ?id .
    ?m        man:isManufacturedBy ?company .
    ?company  org:hasLongName      ?companyName  .
    ?instance sys:realizes         ?m .
    OPTIONAL { ?m rdfs:comment ?comment }
}
GROUP BY ?id
ORDER BY ASC(?id)"""


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

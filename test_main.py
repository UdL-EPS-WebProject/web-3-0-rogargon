from unittest import TestCase
from rdflib import Graph


def print_graph(g):
    import re
    output = g.serialize(format="turtle", encoding="utf-8")
    output = str(output).replace("b\'", "").replace("\\n", "\n")
    output = re.sub(r"(?m)^\@prefix.*\n?", "", output)
    print(output)


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.g = Graph()
        with open("index.html", "r", encoding="utf-8") as f:
            cls.g.parse(f, format="html")
            f.close()
        print_graph(cls.g)

    def test_at_least_10_triples(self):
        print("The document contains {} triples".format(len(self.g)))
        assert len(self.g) > 10, "The document should include at least 10 triples"

    def test_more_than_20_triples(self):
        print("The document contains {} triples".format(len(self.g)))
        assert len(self.g) > 20, "The document includes more than 20 triples"

    def test_more_than_3_different_types(self):
        qres = self.g.query("""
            SELECT DISTINCT ?type
            WHERE { ?s a ?type }
            """)
        print("Types of resources included in the document: ")
        for row in qres:
            print("Type %s" % row)
        assert len(qres) > 3, "The document includes more than 3 types of resources"

    def test_graph_depth_3_or_more(self):
        qres = self.g.query("""
            ASK { ?s1 ?p1 ?o1 . ?o1 ?p2 ?o2 . ?o2 ?p3 ?o4 }
            """)
        assert qres, "The document includes relationship with depth 3 or more"

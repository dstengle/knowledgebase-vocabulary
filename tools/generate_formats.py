#!/usr/bin/env python3
"""
Generate multiple serialization formats from Turtle
"""

from rdflib import Graph
from pathlib import Path

def convert_vocabulary():
    """Convert vocabulary to multiple formats"""
    g = Graph()
    g.parse("vocabulary/kb.ttl", format="turtle")
    
    # Generate RDF/XML
    with open("vocabulary/kb.rdf", "w") as f:
        f.write(g.serialize(format="xml"))
    
    # Generate JSON-LD with context
    context = {
        "kb": "http://example.org/kb/vocab#",
        "dcterms": "http://purl.org/dc/terms/",
        "schema": "http://schema.org/",
        "foaf": "http://xmlns.com/foaf/0.1/",
        "skos": "http://www.w3.org/2004/02/skos/core#"
    }
    
    with open("vocabulary/kb.jsonld", "w") as f:
        f.write(g.serialize(format="json-ld", context=context))
    
    print("Generated RDF/XML and JSON-LD formats")

if __name__ == "__main__":
    convert_vocabulary()

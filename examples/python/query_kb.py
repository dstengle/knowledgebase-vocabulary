#!/usr/bin/env python3
"""
Example: Query KB using SPARQL
"""

from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

# Namespaces
KB = Namespace("http://example.org/kb/vocab#")
BASE = Namespace("http://example.org/kb/")

def query_todos(graph):
    """Find all open todos"""
    query = prepareQuery("""
        SELECT ?todo ?text WHERE {
            ?todo a kb:TodoItem ;
                  kb:rawText ?text ;
                  kb:isCompleted false .
        }
        """, 
        initNs={"kb": KB}
    )
    
    results = graph.query(query)
    for row in results:
        print(f"TODO: {row.text}")

def query_meetings_with_person(graph, person_uri):
    """Find all meetings with a specific person"""
    query = prepareQuery("""
        SELECT ?meeting ?title ?date WHERE {
            ?meeting a kb:Meeting ;
                     kb:hasAttendee ?person ;
                     dcterms:title ?title ;
                     dcterms:created ?date .
        }
        ORDER BY DESC(?date)
        """,
        initNs={"kb": KB, "dcterms": DCTERMS}
    )
    
    results = graph.query(query, initBindings={'person': person_uri})
    for row in results:
        print(f"{row.date}: {row.title}")

def find_stale_relationships(graph):
    """Find relationships with no recent interaction"""
    query = prepareQuery("""
        SELECT ?person ?other ?lastDate WHERE {
            GRAPH :inferred {
                ?person kb:hasRelationship ?rel .
                ?rel kb:withPerson ?other ;
                     kb:lastInteraction ?lastDate ;
                     kb:isStale true .
            }
        }
        ORDER BY ?lastDate
        """,
        initNs={"kb": KB}
    )
    
    results = graph.query(query)
    for row in results:
        print(f"{row.person} hasn't met {row.other} since {row.lastDate}")

if __name__ == "__main__":
    # Load your RDF data
    g = Graph()
    # g.parse("path/to/your/data.ttl", format="turtle")
    
    # Example queries
    print("Open Todos:")
    query_todos(g)
    
    print("\nMeetings with John Smith:")
    query_meetings_with_person(g, BASE["person/John_Smith"])
    
    print("\nStale Relationships:")
    find_stale_relationships(g)

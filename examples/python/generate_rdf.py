#!/usr/bin/env python3
"""
Example: Convert markdown front matter to RDF using KB vocabulary
"""

import yaml
import rdflib
from rdflib import Graph, Namespace, Literal, URIRef
from datetime import datetime
import re

# Namespaces
KB = Namespace("http://example.org/kb/vocab#")
BASE = Namespace("http://example.org/kb/")
DCTERMS = Namespace("http://purl.org/dc/terms/")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")

def parse_markdown_file(filepath):
    """Extract front matter and content from markdown file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract front matter
    if content.startswith('---'):
        _, fm, body = content.split('---', 2)
        front_matter = yaml.safe_load(fm)
    else:
        front_matter = {}
        body = content
    
    return front_matter, body

def create_document_rdf(filepath, front_matter, body):
    """Generate RDF for a document"""
    g = Graph()
    g.bind('kb', KB)
    g.bind('', BASE)
    g.bind('dcterms', DCTERMS)
    
    # Create document URI from filepath
    doc_uri = BASE[filepath.replace('.md', '').replace(' ', '_')]
    
    # Determine document type
    doc_type = front_matter.get('type', 'document')
    type_map = {
        'daily-note': KB.DailyNote,
        'group-meeting': KB.GroupMeeting,
        '1on1-meeting': KB.OneOnOneMeeting,
        'person': KB.PersonProfile,
        'book': KB.BookNote
    }
    
    # Add document triples
    g.add((doc_uri, rdflib.RDF.type, type_map.get(doc_type, KB.Document)))
    g.add((doc_uri, KB.filePath, Literal(filepath)))
    
    if 'title' in front_matter:
        g.add((doc_uri, DCTERMS.title, Literal(front_matter['title'])))
    
    if 'created' in front_matter:
        g.add((doc_uri, DCTERMS.created, 
               Literal(front_matter['created'], datatype=XSD.dateTime)))
    
    # Add tags
    if 'tags' in front_matter:
        tags = front_matter['tags'].split(', ')
        for tag in tags:
            tag_uri = BASE['tag/' + tag.replace('/', '/')]
            g.add((doc_uri, KB.hasTag, tag_uri))
    
    # Extract sections and links (simplified)
    sections = re.findall(r'^## (.+)$', body, re.MULTILINE)
    for section in sections:
        section_uri = URIRef(str(doc_uri) + '#' + section.replace(' ', '_'))
        g.add((doc_uri, KB.hasSection, section_uri))
        g.add((section_uri, rdflib.RDF.type, KB.Section))
        g.add((section_uri, KB.heading, Literal(section)))
    
    return g

if __name__ == "__main__":
    # Example usage
    filepath = "timeline/2024/11/15/daily.md"
    front_matter = {
        'type': 'daily-note',
        'title': 'Thursday Daily Note',
        'tags': 'bydate/2024/11/15, byweek/2024/46/Thu',
        'created': datetime.now().isoformat()
    }
    body = """## Morning Thoughts
Thinking about the [[Coffee Project]].

## Meetings
- 9am [[Team Standup]]
- 2pm 1:1 with [[Sarah Chen]]

## Todos
- [ ] Review PR
- [x] Send email
"""
    
    g = create_document_rdf(filepath, front_matter, body)
    print(g.serialize(format='turtle'))

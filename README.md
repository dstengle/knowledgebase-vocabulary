# KB Vocabulary - Personal Knowledge Base Ontology

A vocabulary for representing markdown-based personal knowledge management systems in RDF.

## Features
- Document-centric model with rich context preservation  
- Meeting notes, todos, and relationship tracking
- Hierarchical tagging with SKOS
- Built on established vocabularies (FOAF, Schema.org, Dublin Core)

## Quick Start

```turtle
@prefix kb: <http://example.org/kb/vocab#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

:timeline/2024/11/15/team-meeting a kb:GroupMeeting ;
    dcterms:title "Team Standup" ;
    kb:hasTag :tag/meetings/standup ;
    kb:hasAttendee :person/John_Smith .
```

See [documentation/quick-start.md](documentation/quick-start.md) for more.

## Documentation

- [Complete Reference](documentation/reference.md)
- [Quick Start Guide](documentation/quick-start.md)
- [SPARQL Cookbook](documentation/sparql-cookbook.md)
- [Design Decisions](documentation/design-decisions.md)

## Installation

### Using the vocabulary in your RDF:

```turtle
@prefix kb: <http://example.org/kb/vocab#> .

# Your RDF here
```

### For Python projects:

```python
from rdflib import Namespace
KB = Namespace("http://example.org/kb/vocab#")
```

## License

[Choose: MIT / Apache 2.0 / CC BY 4.0]

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

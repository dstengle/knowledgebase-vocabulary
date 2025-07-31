# KB Vocabulary Quick Start Guide

## Basic Concepts

The KB vocabulary represents your markdown knowledge base as RDF. Key concepts:

- **Documents** are markdown files
- **Links** are `[[wiki-style]]` references
- **Entities** (people, companies, books) can exist without documents
- **Inference** derives high-level facts from document structure

## Your First Document

```turtle
@prefix kb: <http://example.org/kb/vocab#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# A daily note
:timeline/2024/11/15/daily a kb:DailyNote ;
    dcterms:title "Thursday Daily Note" ;
    dcterms:created "2024-11-15T09:00:00"^^xsd:dateTime ;
    kb:filePath "timeline/2024/11/15/daily.md" ;
    kb:hasTag :tag/bydate/2024/11/15 .
```

## Representing Links

When your markdown contains `[[John Smith]]`:

```turtle
# The link itself
:timeline/2024/11/15/daily#Meeting_Notes/link/John_Smith a kb:WikiLink ;
    kb:target :person/John_Smith ;
    kb:linkText "[[John Smith]]" ;
    kb:inSection :timeline/2024/11/15/daily#Meeting_Notes .

# This creates/references a person entity
:person/John_Smith a kb:Person ;
    foaf:name "John Smith" ;
    kb:isPlaceholder true ;  # No dedicated document yet
    kb:mentionedIn :timeline/2024/11/15/daily .
```

## Todos

Markdown: `- [ ] Follow up with Sarah [[due:: 2024-11-20]]`

```turtle
# Raw todo item
:timeline/2024/11/15/daily#Action_Items/todo/Follow_up_with_Sarah a kb:TodoItem ;
    kb:rawText "- [ ] Follow up with Sarah [[due:: 2024-11-20]]" ;
    kb:isCompleted false .

# Inferred todo (in :inferred graph)
:timeline/2024/11/15/daily/todo/Follow_up_with_Sarah a kb:Todo ;
    kb:description "Follow up with Sarah" ;
    kb:due "2024-11-20"^^xsd:date ;
    kb:assignedTo :person/Me ;  # Or inferred from context
    kb:derivedFrom :timeline/2024/11/15/daily#Action_Items/todo/Follow_up_with_Sarah .
```

## Common Patterns

### Meeting with Attendees

```turtle
:timeline/2024/11/15/team-standup a kb:GroupMeeting ;
    kb:hasSection :timeline/2024/11/15/team-standup#Attendees .

# Links in Attendees section → hasAttendee
:timeline/2024/11/15/team-standup 
    kb:hasAttendee :person/John_Smith ,
                   :person/Sarah_Chen .
```

### Tag Hierarchy

```turtle
:tag/projects/web/frontend a kb:Tag ;
    skos:prefLabel "frontend" ;
    skos:broader :tag/projects/web ;
    skos:related :tag/topics/javascript .

# Document with this tag also matches parent tags
:my-doc kb:hasTag :tag/projects/web/frontend .
# Inferred: also has tags projects/web and projects
```

## Next Steps

1. Look at examples in `examples/documents/`
2. Try the SPARQL queries in `examples/queries/`
3. Read about [design decisions](design-decisions.md)
4. See the [complete reference](reference.md)

# KB Vocabulary Design Decisions

## Why RDF?

1. **Graph structure** matches the interconnected nature of knowledge
2. **Standards-based** enables tool reuse and future compatibility
3. **Inference capabilities** derive insights from raw data
4. **SPARQL** provides powerful querying

## Key Design Choices

### Documents as First-Class Citizens

**Decision**: Documents are entities, not just containers

**Rationale**: 
- Markdown files are the source of truth
- Preserves authoring context
- Enables document-level queries

### Semantic IRIs

**Decision**: Use meaningful IRIs like `:person/John_Smith`

**Rationale**:
- Human-readable in queries and debugging
- Natural uniqueness from content
- Hierarchical organization

### Three-Graph Architecture

**Decision**: Separate :original, :inferred, and :entities graphs

**Rationale**:
- Clear provenance tracking
- Different update patterns
- Query optimization

### Wiki Links as Entities

**Decision**: Reify links with context

**Rationale**:
- Preserves link location and surrounding text
- Enables context-aware inference
- Supports multiple mentions analysis

### Placeholder Entities

**Decision**: Create entities for all [[links]], even without documents

**Rationale**:
- Captures implicit knowledge
- Enables "broken link" analysis
- Supports gradual knowledge building

### SKOS for Tags

**Decision**: Use SKOS for tag taxonomy

**Rationale**:
- Standard hierarchical vocabulary
- Built-in synonym support
- Tool ecosystem

### Mixed Formality

**Decision**: Combine simple predicates with rich relationship objects

**Rationale**:
- Simple queries remain simple
- Complex analysis when needed
- Best of both worlds

## Alternative Approaches Considered

### 1. Document-as-Named-Graph

**Considered**: Each document as its own named graph

**Rejected because**:
- Complicates cross-document queries
- Loses document-as-entity benefits

### 2. Pure Property Graph

**Considered**: Neo4j-style property graph

**Rejected because**:
- Less standard tooling
- No built-in inference
- Harder to integrate vocabularies

### 3. Flat Tagging

**Considered**: Simple tag list without hierarchy

**Rejected because**:
- Loses organizational structure
- No parent/child relationships
- Harder to browse

## Future Considerations

### External Data Integration
- Design supports future email, web, calendar data
- Provenance tracking ready
- Entity reconciliation patterns

### NLP Enhancement
- Structure ready for NLP-extracted entities
- Confidence scores on inferences
- Sentiment analysis integration

### Versioning
- Document history tracking
- Change propagation
- Temporal queries

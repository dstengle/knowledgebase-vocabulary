# Contributing to KB Vocabulary

Thank you for your interest in contributing to the KB Vocabulary!

## Design Principles

1. **Reuse existing vocabularies** where appropriate
2. **Keep property names human-readable**
3. **Document all terms clearly**
4. **Include examples for new features**
5. **Maintain backward compatibility**

## Proposing Changes

1. **Open an issue** describing the proposed addition
2. **Include use cases** and examples
3. **Check existing terms** to avoid duplication
4. **Consider impact** on existing users

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-term`)
3. Update the vocabulary file (`vocabulary/kb.ttl`)
4. Add examples in `examples/`
5. Update documentation
6. Run validation: `python tools/validate.py`
7. Submit PR with clear description

## Adding New Terms

### For a new class:
```turtle
kb:YourClass a owl:Class ;
    rdfs:subClassOf kb:Document ;  # or appropriate parent
    rdfs:comment "Clear description of the class" .
```

### For a new property:
```turtle
kb:yourProperty a owl:ObjectProperty ;
    rdfs:domain kb:YourClass ;
    rdfs:range xsd:string ;
    rdfs:comment "What this property represents" .
```

## Testing

Run tests before submitting:
```bash
python -m pytest tests/
```

## Questions?

Open an issue for discussion!

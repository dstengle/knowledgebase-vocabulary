#!/usr/bin/env python3
"""
Validate KB vocabulary and examples
"""

import sys
from pathlib import Path
from rdflib import Graph, Namespace
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KB = Namespace("http://example.org/kb/vocab#")

def validate_vocabulary(vocab_file):
    """Validate the vocabulary file"""
    g = Graph()
    try:
        g.parse(vocab_file, format='turtle')
        logger.info(f"✓ Vocabulary file parsed successfully: {len(g)} triples")
    except Exception as e:
        logger.error(f"✗ Failed to parse vocabulary: {e}")
        return False
    
    # Check for required classes
    required_classes = [
        KB.Document, KB.WikiLink, KB.TodoItem, 
        KB.Person, KB.Tag
    ]
    
    for cls in required_classes:
        if (cls, None, None) not in g:
            logger.error(f"✗ Missing required class: {cls}")
            return False
    
    logger.info("✓ All required classes present")
    return True

def validate_examples(examples_dir):
    """Validate all example files"""
    example_files = Path(examples_dir).rglob("*.ttl")
    
    for file in example_files:
        g = Graph()
        try:
            g.parse(file, format='turtle')
            logger.info(f"✓ Valid example: {file.name} ({len(g)} triples)")
        except Exception as e:
            logger.error(f"✗ Invalid example {file.name}: {e}")
            return False
    
    return True

def main():
    """Run all validations"""
    vocab_file = Path("vocabulary/kb.ttl")
    examples_dir = Path("examples")
    
    if not vocab_file.exists():
        logger.error("Vocabulary file not found")
        sys.exit(1)
    
    # Validate vocabulary
    if not validate_vocabulary(vocab_file):
        sys.exit(1)
    
    # Validate examples
    if not validate_examples(examples_dir):
        sys.exit(1)
    
    logger.info("✓ All validations passed!")

if __name__ == "__main__":
    main()

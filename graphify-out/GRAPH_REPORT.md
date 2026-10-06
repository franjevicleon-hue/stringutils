# Graph Report - stringutils  (2026-10-06)

## Corpus Check
- Corpus is ~113 words - fits in a single context window. You may not need a graph.

## Summary
- 14 nodes · 23 edges · 3 communities (2 shown, 1 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.85)
- Token cost: 66,909 input · 0 output

## Community Hubs (Navigation)
- Palindrome Logic & Tests
- README Documentation
- Word Reversal & Module

## God Nodes (most connected - your core abstractions)
1. `is_palindrome()` - 8 edges
2. `reverse_words()` - 6 edges
3. `stringutils (String Helper Collection)` - 5 edges
4. `test_is_palindrome_true()` - 2 edges
5. `test_is_palindrome_false()` - 2 edges
6. `test_is_palindrome_with_spaces()` - 2 edges
7. `test_reverse_words()` - 2 edges
8. `Palindrome Check (case- and space-insensitive)` - 2 edges
9. `Word Order Reversal` - 2 edges
10. `pytest (Test Runner)` - 2 edges

## Surprising Connections (you probably didn't know these)
- `is_palindrome()` --implements--> `Palindrome Check (case- and space-insensitive)`  [EXTRACTED]
  stringutils.py → README.md
- `reverse_words()` --implements--> `Word Order Reversal`  [EXTRACTED]
  stringutils.py → README.md
- `stringutils (String Helper Collection)` --references--> `is_palindrome()`  [EXTRACTED]
  README.md → stringutils.py
- `stringutils (String Helper Collection)` --references--> `reverse_words()`  [EXTRACTED]
  README.md → stringutils.py
- `test_is_palindrome_false()` --calls--> `is_palindrome()`  [EXTRACTED]
  test_stringutils.py → stringutils.py

## Import Cycles
- None detected.

## Communities (3 total, 1 thin omitted)

### Community 0 - "Palindrome Logic & Tests"
Cohesion: 0.53
Nodes (4): is_palindrome(), test_is_palindrome_false(), test_is_palindrome_true(), test_is_palindrome_with_spaces()

### Community 1 - "README Documentation"
Cohesion: 0.50
Nodes (4): Palindrome Check (case- and space-insensitive), pytest (Test Runner), stringutils (String Helper Collection), Word Order Reversal

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `is_palindrome()` connect `Palindrome Logic & Tests` to `README Documentation`, `Word Reversal & Module`?**
  _High betweenness centrality (0.331) - this node is a cross-community bridge._
- **Why does `reverse_words()` connect `Word Reversal & Module` to `Palindrome Logic & Tests`, `README Documentation`?**
  _High betweenness centrality (0.248) - this node is a cross-community bridge._
- **Why does `stringutils (String Helper Collection)` connect `README Documentation` to `Palindrome Logic & Tests`, `Word Reversal & Module`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
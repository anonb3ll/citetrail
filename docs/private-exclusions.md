# Scope exclusions

Citetrail is a focused public slice, extracted from a larger private system its
maintainers run day to day. This page states what is **not** in this repository,
so you can tell a missing feature from a deliberate omission.

## Not included, and not planned for this repo

- **Private capture data.** No real browsing history, no real captures, no
  personal URLs. Every fixture here is synthetic.
- **The maintainers' operational deployment.** Host configuration, service
  definitions, tokens, and machine inventories.
- **Private knowledge-vault integration.** The personal note store the private
  system reads and writes.
- **Cross-agent memory and coordination planes** belonging to the private
  system.
- **Cognitive-load and attention telemetry.** The private system experiments
  with this; it is out of scope here and carries no clinical meaning.

## Deferred, and reconsidered only with evidence

- Cross-device sync and federated stores
- Mobile capture
- Broad personal-knowledge-management features
- Automatic summarization or learning from what you read
- Hosted or team operation
- Compliance certification of any kind

## Why the split exists

Citetrail is a public validation slice, not a private system with the names
changed. Local capture, bounded provenance, honest privacy states, and MCP
recall are the parts that might be generally useful. The rest is one person's
operational setup.

If you need a deferred item, open an issue describing the workflow it would
unblock. Use cases move this list; requests on their own do not.

# Citetrail

[![CI](https://github.com/anonb3ll/citetrail/actions/workflows/ci.yml/badge.svg)](https://github.com/anonb3ll/citetrail/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**Local, provenance-backed memory of what your browser saw — every recall
carries the URL, title, and timestamp it came from.**

Citetrail captures the pages you actually read, keeps them on your machine, and
makes them searchable — by you, and by your AI agents over
[MCP](https://modelcontextprotocol.io). When an agent uses something it found
there, it can cite exactly where it came from.

- **Status:** pre-release. See [Project status](#project-status) before
  installing.
- **License:** [Apache-2.0](LICENSE)
- **Local by default.** No account, no server, no upload. Blocked pages fail
  closed.

---

## The problem Citetrail solves

You read six tabs, closed them, and now your coding agent needs the thing in tab
four. Your options today are: paste it again, let the agent re-search the open
web and hope it lands on the same page, or accept an answer with no source.

Browser history knows you visited a URL. It does not know what the page said,
and it cannot tell your agent. Citetrail closes that gap:

| Browser history | Citetrail |
| --- | --- |
| A list of URLs | The content you actually read, captured |
| Search by title, roughly | Search by what the page said |
| Invisible to your tools | Queryable by agents over MCP |
| No notion of "why is this here" | Every entry carries its provenance |
| Everything, indiscriminately | Only allowed pages; blocklist fails closed |

## What "provenance-backed" means here

Every stored fragment keeps a **bounded reference**: source URL, page title,
capture timestamp, and the position within the page. Recall returns the
fragment *and* that reference together — they cannot be separated. An agent that
answers from Citetrail can always say where it got it, and you can always open
the original.

If the source is gone, Citetrail says the source is gone. It does not quietly
serve a fragment as if it were still live.

## Quickstart

```bash
git clone https://github.com/anonb3ll/citetrail
cd citetrail
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/citetrail init

# 2. Search the local store
.venv/bin/citetrail search "retry backoff"

# Optional: block a sensitive hostname before it can be stored
.venv/bin/citetrail block bank.example.test

# 3. Point an agent at the same local store over MCP
.venv/bin/citetrail mcp --stdio
```

The default store is `~/.local/share/citetrail`. Set `CITETRAIL_STORE` or pass
`--store PATH` to use a different local directory. See
[docs/extension.md](docs/extension.md) to load the unpacked Chromium adapter.

## Documentation

| Guide | Description |
| --- | --- |
| [docs/README.md](docs/README.md) | Documentation index |
| [docs/cli-reference.md](docs/cli-reference.md) | CLI commands and store layout |
| [docs/mcp.md](docs/mcp.md) | MCP tool schema and registration |
| [docs/extension.md](docs/extension.md) | Chromium extension setup |
| [docs/privacy.md](docs/privacy.md) | Blocklist and fail-closed behavior |
| [docs/integration-contract.md](docs/integration-contract.md) | Optional Runroom integration |

## Frequently asked questions

### How do I let my AI agent search my browsing history?

Run the local MCP server and register it with your agent. The agent queries
Citetrail like any other MCP tool and receives fragments with their sources
attached. It never gets raw access to your browser or your profile.

### Where is my data stored, and does anything get uploaded?

On your machine, in a local database you can delete at any time. Citetrail has
no server and performs no uploads. See [docs/privacy.md](docs/privacy.md).

### How do I stop it capturing my bank, my email, or my work intranet?

The blocklist. It is checked before capture, and it **fails closed** — if the
rules cannot be evaluated for a page, that page is not captured. Add a host
with `citetrail block bank.example.test`. Allowlist-only capture is deferred.

### Can an agent cite a source it did not actually read?

Not from Citetrail. The reference travels with the fragment; there is no API
that returns text without its provenance.

### What happens when I am offline, or a page is gone?

Recall works offline against what you already captured. If the original URL is
unreachable, results are marked as such rather than silently presented as
current. Unavailable and privacy-blocked states are reported honestly, not
hidden.

### Is this a note-taking app or a second brain?

No. Citetrail captures and recalls; it does not organize your thinking, build a
knowledge graph, or ask you to maintain anything. It is plumbing for tools that
need to know what you read.

### Does it work in any browser?

The extension targets Chromium-based browsers first. The native bridge between
the extension and the local service has real limits — see
[docs/limitations.md](docs/limitations.md).

## What Citetrail is not

- Not a hosted service and not a sync service. One machine, one store.
- Not a PKM or note system.
- Not a clinical, wellbeing, or attention-tracking tool. It makes no claim about
  your cognition.
- Not a scraper. It captures pages you visited yourself, under your rules.
- Not a mobile app.

See [docs/limitations.md](docs/limitations.md) and
[docs/private-exclusions.md](docs/private-exclusions.md).

## Related project

[Runroom](https://github.com/anonb3ll/runroom) coordinates handoffs between
AI agents and humans with review gates and an audit trail. The two projects are
independent and neither requires the other; an optional integration shows a
Citetrail reference feeding a governed Runroom task.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report vulnerabilities privately —
see [SECURITY.md](SECURITY.md).

## Project status

Pre-release, pre-1.0. Interfaces will change. Citetrail is published to find out
whether other people need this — if you try it, tell us what you were trying to
recall and whether you got it.

## License

[Apache License 2.0](LICENSE). Copyright 2026 The Citetrail Contributors.

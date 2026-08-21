# CLI reference

Global flag: `--store PATH` (default: `~/.local/share/citetrail`, overridable via
`CITETRAIL_STORE`).

## Commands

| Command | Purpose |
| --- | --- |
| `citetrail init [--store PATH]` | Create local SQLite store and policy file |
| `citetrail search QUERY [--store PATH]` | Search captures; prints JSON with status + matches |
| `citetrail block HOST [--store PATH]` | Add hostname to blocklist (fail-closed policy) |
| `citetrail mcp --stdio [--store PATH]` | Run MCP server on stdin/stdout |
| `citetrail native-host [--store PATH]` | Native-message endpoint for the Chromium extension |

## Search result shape

Every match includes **text and reference together**:

```json
{
  "status": "found",
  "matches": [
    {
      "text": "...",
      "reference": {
        "url": "https://...",
        "title": "...",
        "captured_at": "2026-08-20T12:00:00Z",
        "position": {"start": 0, "end": 53}
      }
    }
  ]
}
```

Honest statuses when nothing is returned: `not-found`, `offline`, `unavailable`,
`privacy-blocked`. These never collapse into a silent empty list.

## Store layout

```
~/.local/share/citetrail/
├── citetrail.sqlite3   # captures table
└── policy.json         # blocklist (optional)
```

Delete the directory to remove all local data. Nothing is uploaded.

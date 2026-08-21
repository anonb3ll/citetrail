# MCP server

Citetrail exposes one tool over [Model Context Protocol](https://modelcontextprotocol.io)
stdio transport.

## Start the server

```bash
citetrail init   # once
citetrail mcp --stdio
```

## Tool: `citetrail_search`

Search local captures. Every result includes inseparable provenance.

### Input schema

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `query` | string | yes | Substring search over captured text and titles |
| `source_state` | enum | no | `available` (default), `offline`, `unavailable`, `privacy-blocked` |

### Output

JSON text content with `status` and `matches[]`. Each match has `text` and `reference`
(`url`, `title`, `captured_at`, `position`).

There is **no API** that returns text without its reference.

## Register with an agent host

Example for a project-scoped MCP config (paths adjusted to your install):

```json
{
  "mcpServers": {
    "citetrail": {
      "command": "/path/to/venv/bin/citetrail",
      "args": ["mcp", "--stdio"],
      "env": {
        "CITETRAIL_STORE": "/home/you/.local/share/citetrail"
      }
    }
  }
}
```

The server handles `initialize`, `tools/list`, and `tools/call` for `citetrail_search`.

## Privacy

The MCP server reads only your local store. It makes no network requests. Blocklist
evaluation fails closed — if rules cannot be read, capture (and recall of blocked
hosts) follows the privacy policy documented in [privacy.md](privacy.md).

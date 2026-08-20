# Privacy and data handling

Privacy behavior is the product here, so this document is a specification, not
a disclaimer.

## Short version

Everything stays on your machine. Citetrail has no server, no account, and no
telemetry. It makes no outbound network requests of its own. Pages you exclude
are never captured, and the exclusion check fails closed.

## What is captured

Only pages you visit yourself, in a browser where you installed the extension,
that pass your rules. For each captured page: the text content, the URL, the
page title, and the capture timestamp.

## What is never captured

- Pages matching your blocklist.
- Citetrail currently supports explicit hostname blocks through the CLI.
  Allowlist-only capture is not implemented yet.
- Form fields, passwords, cookies, and credentials — the extension does not read
  them.
- Pages loaded in a private/incognito window. The content script refuses to
  send from an incognito extension context.
- Any page, if the rules cannot be evaluated. **Fail closed** is the default and
  cannot be turned off.

## Where it is stored

In a local store you create with `citetrail init`. Plain files and a local
database, on your disk, readable by your user account. Citetrail does not
encrypt the store — anyone with your user account can read it, which is the same
trust boundary as your browser profile.

## Network egress

None. Citetrail does not call home, does not check for updates, and does not
send usage data. If you ever observe an outbound request originating from
Citetrail, that is a security bug — see [SECURITY.md](../SECURITY.md).

Agents that query Citetrail over MCP have their own network access. Citetrail
cannot control what an agent does with a fragment after handing it over, and
does not pretend to.

## Retention and deletion

- Nothing expires by default; you decide what to keep.
- Delete the store directory to remove everything. There is no other copy and
  nothing to revoke elsewhere. Per-capture, domain, and time-range deletion
  are not implemented yet.

## Honest states

Recall distinguishes, and always reports, the difference between:

- **found** — captured content, with provenance;
- **privacy-blocked** — a matching page exists but your rules excluded it;
- **unavailable** — captured, but the original URL no longer resolves;
- **offline** — the original could not be verified right now;
- **not found** — nothing was captured.

These are never collapsed into a silent empty result.

## Sharing a capture

A capture is your reading. Review and redact before attaching one to an issue.

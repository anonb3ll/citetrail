# Security Policy

## Supported versions

Citetrail is pre-1.0. Only the latest commit on the default branch is
supported.

## Reporting a vulnerability

**Do not open a public issue.**

Report privately through GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
on this repository (Security → Advisories → New draft advisory, or the
"Report a vulnerability" button when enabled). Include what an attacker can
do, what access they need, the smallest reproduction you have, and the
affected commit.

If private reporting is unavailable on a fork or mirror, email the repository
owner through their GitHub profile contact options and use the subject line
`[SECURITY] Citetrail`.

Acknowledgement within 7 days. Please allow reasonable time for a fix before
public disclosure.

## In scope — including privacy defects

Privacy failures are security bugs in this project:

- Capture of a page that the blocklist should have excluded.
- The blocklist failing **open** rather than closed under any condition.
- A recall path that returns content without its provenance reference.
- Any outbound network request originating from Citetrail.
- Another local process reading the store or driving the MCP server without
  authorization.
- The browser extension exposing captured content to page scripts.
- Provenance that can be forged or silently altered.

## Out of scope

- Content you deliberately captured being present in your own store.
- Vulnerabilities in your browser, your OS, or the agents you connect.
- Anything requiring an attacker who already has your user account on your
  machine — Citetrail does not defend against that, and says so.
- Scanner output with no demonstrated impact.

## Threat model, briefly

Citetrail assumes your machine and your browser profile are trusted, and that
**web pages and connected agents are not**. A captured page may try to
manipulate an agent that later reads it; provenance exists so the agent and the
human can see where a claim came from. Citetrail makes no compliance or
certification claim.

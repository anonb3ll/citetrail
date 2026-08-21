# Contributing to Citetrail

Thanks for looking. Citetrail is pre-1.0 and released to find out whether the
problem it solves is a problem other people have — so a clear report of what you
tried to recall and failed to get is worth as much as a patch.

## Before you start

- Read [docs/privacy.md](docs/privacy.md). Privacy behavior is the product, not
  a setting.
- Read [docs/limitations.md](docs/limitations.md) and
  [docs/private-exclusions.md](docs/private-exclusions.md). Some gaps are
  deliberate; PRs that close them will be declined regardless of quality.
- For anything larger than a bug fix, open an issue first.

## Ground rules

1. **The blocklist fails closed.** No change may make capture proceed when the
   rules cannot be evaluated. This is not negotiable for performance.
2. **Provenance is inseparable from content.** Do not add an API that returns a
   fragment without its source reference.
3. **No egress.** Citetrail makes no outbound network requests. Code that opens
   a socket needs an explicit, documented, opt-in reason.
4. **Honest states.** Offline, unavailable, and privacy-blocked must be
   reported as themselves. Never degrade one into an empty result.
5. **No real captures in the repo.** Every fixture is synthetic. No personal
   URLs, no real page content, no secrets.
6. **Tests first for behavior changes.**

## Development setup

```bash
git clone https://github.com/citetrail/citetrail
cd citetrail
python3 -m venv .venv && .venv/bin/pip install -e .

.venv/bin/ruff check . && .venv/bin/ruff format --check . && .venv/bin/pytest -q
```

## Pull requests

- One logical change per PR.
- Include the commands you ran and their output — the output, not a summary.
- Say plainly what you did not test.
- Conventional Commit subject lines (`fix:`, `feat:`, `docs:`, `chore:`).

## Reporting bugs

What you expected, what happened, and the smallest reproduction. **Redact
before you paste** — captured content is your reading history.

## Security and privacy reports

Do not open a public issue. See [SECURITY.md](SECURITY.md). A privacy defect —
capture that should have been blocked, provenance that came back detached — is
a security report here, not a bug report.

## License

By contributing you agree that your contributions are licensed under the
[Apache License 2.0](LICENSE).

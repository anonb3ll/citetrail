# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-08-22

### Added
- Local SQLite capture store with hostname blocklist and fail-closed privacy
  evaluation.
- CLI: `init`, `search`, `block`, `mcp --stdio`, and `native-host`.
- MCP `citetrail_search` tool that returns text only with inseparable
  provenance.
- Chromium MV3 extension and native-messaging bridge with honest
  `unavailable` / `privacy-blocked` / `captured` states.
- Apache-2.0 license, security policy, code of conduct, contribution guide,
  privacy and limitations docs, issue/PR templates, and CI on Python
  3.11–3.13.

### Changed
- Packaging metadata, source distribution contents, and contributor setup for
  public GitHub release readiness.
- Native-host helper logs under private user state (`mode 700` / `600`) rather
  than `/tmp`.
- Build backend floor raised to setuptools 77 so SPDX license metadata is
  valid in isolated builds.

<!-- Pre-1.0: interfaces may change without deprecation cycles. -->

[Unreleased]: https://github.com/anonb3ll/citetrail/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/anonb3ll/citetrail/releases/tag/v0.1.0

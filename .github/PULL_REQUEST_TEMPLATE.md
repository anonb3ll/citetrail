## What this changes

<!-- One or two sentences. What behavior is different after this PR? -->

## Why

<!-- Link the issue, or describe what you could not recall without this. -->

## How a reviewer can check it

<!-- Exact commands. Paste the output, not a summary of the output. -->

```
```

## Privacy impact

<!-- Does this change what is captured, stored, or returned? If no, say "none"
     and why. If yes, describe it explicitly. -->

## What I did not test

## Checklist

- [ ] Tests cover the change, and they fail without it
- [ ] The blocklist still fails closed
- [ ] No recall path returns content without its provenance reference
- [ ] No new outbound network request
- [ ] No real captures, personal URLs, or secrets in code, tests, or fixtures
- [ ] Docs updated if behavior or interfaces changed

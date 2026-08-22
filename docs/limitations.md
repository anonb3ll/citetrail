# Limitations

## Not yet true

Citetrail is pre-release. It is not on PyPI, the extension is not in any web
store, interfaces will change without deprecation cycles, and there is no
upgrade path between pre-1.0 versions.

## Deliberate boundaries

- **One machine.** No sync, no cross-device recall, no shared store.
- **Capture, not comprehension.** Citetrail stores what a page said and where it
  came from. It does not summarize, rank by importance, or build a knowledge
  graph.
- **You maintain the rules.** The blocklist starts empty and protects exactly
  the hostnames you add. Fail-closed evaluation is built in; default blocked
  hosts are not. Citetrail cannot know which of your internal hostnames are
  sensitive.
- **No page-load interception.** Capture happens on rendered content in a tab
  you opened. Citetrail does not proxy, MITM, or fetch pages on your behalf.
- **Not encrypted at rest.** Same trust boundary as your browser profile; see
  [privacy.md](privacy.md).

## Native bridge limits

The extension talks to the local service through a native messaging bridge, and
that path has real constraints:

- It requires the local service to be installed and running. When it is not, the
  extension reports **unavailable** — it does not queue captures indefinitely.
- Message size is bounded by the browser's native messaging limits; very large
  pages are truncated at **50,000 characters** rather than silently dropped.
- Browsers may terminate the bridge on suspend or profile switch; capture
  resumes on the next page, and the gap is visible rather than hidden.
- Chromium-based browsers are the first target. Firefox support is untested.

## Known rough edges

- Dynamic single-page applications may be captured mid-render.
- Content behind an authenticated session is captured as you saw it — which
  means it can contain material you would not want in a shared bug report.
- Search quality on very large stores has not been tuned.

## Explicitly deferred

Cognitive-fatigue and attention modeling, mobile, cross-device sync, federated
or shared authority, broad PKM features, and any clinical or wellbeing claim.
Deferred until there is evidence people use the core recall workflow.

## No claims made

Citetrail makes no security, privacy, or compliance certification claim, and no
claim about adoption or traction.

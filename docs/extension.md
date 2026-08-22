# Chromium extension and local host

The extension lives in `extension/` and is loaded unpacked. It sends rendered
page text, URL, title, and capture time only to the local Citetrail native host.
It makes no network request.

## Load the extension

1. Run `citetrail init`.
2. Open `chrome://extensions`, enable **Developer mode**, select **Load
   unpacked**, then choose this repository's `extension/` directory.
3. Register the native-message host name `org.citetrail.capture` with your
   Chromium browser. The registration must point at an absolute path that runs
   `citetrail native-host`. From a git checkout you can use
   `scripts/citetrail-native-host` (make sure it is executable), or create a
   user-local wrapper that invokes your installed `citetrail` command.

The extension sets `"incognito": "not_allowed"` and the content script also
refuses to send from an incognito context.

The service worker records the last bridge result in extension-local storage:
`captured`, `privacy-blocked`, or `unavailable`. A bridge restart does not queue
old pages; it leaves a visible capture gap.

## Current installation boundary

Native-host manifest paths differ by browser and operating system. Citetrail
does not currently automate that privileged browser registration. Until it is
registered, the extension reports `unavailable`; it does not silently claim a
page was captured.

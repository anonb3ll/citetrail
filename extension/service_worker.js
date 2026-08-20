chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message.type !== "capture") return;
  chrome.runtime.sendNativeMessage("org.citetrail.capture", message, (response) => {
    const error = chrome.runtime.lastError?.message;
    const status = error ? "unavailable" : response.status;
    chrome.storage.local.set({
      lastCapture: { status, error: error ?? null, at: new Date().toISOString() },
    });
    sendResponse({ status });
  });
  return true;
});

if (!chrome.extension.inIncognitoContext && window.top === window) {
  chrome.runtime.sendMessage(
    {
      type: "capture",
      url: window.location.href,
      title: document.title,
      text: document.body?.innerText ?? "",
      captured_at: new Date().toISOString(),
    },
    () => void chrome.runtime.lastError
  );
}

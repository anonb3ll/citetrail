chrome.storage.local.get("lastCapture", ({ lastCapture }) => {
  if (!lastCapture) return;
  document.querySelector("#status").textContent = lastCapture.status;
  document.querySelector("#timestamp").textContent = lastCapture.at;
  document.querySelector("#error").textContent = lastCapture.error ?? "";
});

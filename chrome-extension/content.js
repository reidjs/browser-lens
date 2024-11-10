(async () => {
  // NOTE: htmlContent no longer used
  const htmlContent = document.documentElement.outerHTML;
  const url = document.location.href;

  try {
    await fetch("http://localhost:8000/save", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ html: htmlContent, url }),
    });
    console.log("HTML content sent to server.");
  } catch (error) {
    console.error("Error sending HTML content:", error);
  }
})();

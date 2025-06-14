

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("activation-form");
  const statusBox = document.getElementById("activation-status");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    
    const email = document.getElementById("email").value.trim();
    const key = document.getElementById("license").value.trim();

    statusBox.innerText = "🔄 Validating license...";
    statusBox.style.color = "blue";

    try {
      const response = await fetch("/validate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, key })
      });

      const data = await response.json();

      if (data.valid) {
        statusBox.innerText = "✅ License activated successfully!";
        statusBox.style.color = "green";
      } else {
        statusBox.innerText = "❌ Invalid license or email. Please try again.";
        statusBox.style.color = "red";
      }
    } catch (err) {
      statusBox.innerText = "⚠️ Error contacting server. Try again later.";
      statusBox.style.color = "orange";
    }
  });
});

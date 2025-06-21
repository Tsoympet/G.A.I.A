
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("activation-form");
    const message = document.getElementById("message");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const email = document.getElementById("email").value;
        const key = document.getElementById("license").value;

        const response = await fetch("/validate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: email, license_key: key })
        });

        const result = await response.json();
        message.textContent = result.message;
        message.style.color = result.success ? "green" : "red";
    });
});

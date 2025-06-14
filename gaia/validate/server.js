// server.js
const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');
const app = express();
const PORT = process.env.PORT || 3000;

// Dummy license store (you can use a real DB here)
let validLicenses = {
  "GAIA-1234-ABCD-5678": "user@example.com"
};

app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/validate', async (req, res) => {
  const { email, key } = req.body;

  if (validLicenses[key] === email) {
    await sendConfirmationEmail(email, key);
    return res.json({ valid: true });
  } else {
    return res.json({ valid: false });
  }
});

async function sendConfirmationEmail(email, licenseKey) {
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'your-email@gmail.com',         // Replace with your sender email
      pass: 'your-email-password'           // Use app password or secured method
    }
  });

  const mailOptions = {
    from: 'GAIA Activation <your-email@gmail.com>',
    to: email,
    subject: 'GAIA Activation Successful',
    html: `<h3>✅ Welcome to GAIA</h3>
           <p>Your license key <b>${licenseKey}</b> has been successfully activated.</p>
           <p>Thank you for joining the GAIA experience.</p>`
  };

  await transporter.sendMail(mailOptions);
}

app.listen(PORT, () => {
  console.log(`GAIA activation portal running on port ${PORT}`);
});

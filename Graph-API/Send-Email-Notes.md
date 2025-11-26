To Send Emails Using Microsoft Graph Explorer, Do the following:

Step 1: Log Into Your Microsoft Graph Explorer Port
Step 2: Set the Request Method to: GET | Version: v1.0 | URL: https://graph.microsoft.com/v1.0/me/microsoft.graph.sendMail
Step 3: Enter the sample below in the request body (and modify as required):
{
  "message": {
    "subject": "Test Email from Graph API",
    "body": {
      "contentType": "Text",
      "content": "Hello Chardelin, this is a test email sent via Microsoft Graph API!"
    },
    "toRecipients": [
      {
        "emailAddress": {
          "address": "your-email@yourdomain.com"
        }
      }
    ]
  }
}

# Install module if needed
# Install-Module Microsoft.Graph -Scope CurrentUser

# Connect to Graph with client credentials
$tenantId = "YOUR_TENANT_ID"
$clientId = "YOUR_CLIENT_ID"
$clientSecret = "YOUR_CLIENT_SECRET"

$secureSecret = ConvertTo-SecureString $clientSecret -AsPlainText -Force
$credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $clientId, $secureSecret

Connect-MgGraph -ClientId $clientId -TenantId $tenantId -ClientSecret $clientSecret -Scopes "Mail.Send"

# Send email
Send-MgUserMail -UserId "your-email@yourdomain.com" -Message @{
  Subject = "Graph API Email from PowerShell"
  Body = @{
    ContentType = "Text"
    Content = "This email was sent using Microsoft Graph and PowerShell."
  }
  ToRecipients = @(@{EmailAddress = @{Address = "your-email@yourdomain.com"}})
}

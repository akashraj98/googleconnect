# Google Calendar API Integration

This repository contains code for integrating with Google Calendar API using OAuth 2.0 authentication. The code is implemented in Django and provides two endpoints for the integration.

## Endpoints

### `/rest/v1/calendar/init/` - `GoogleCalendarInitView()`

This endpoint initiates the OAuth 2.0 flow for Google Calendar API. It prompts the user to provide their credentials.

#### Steps:
1. The user accesses this endpoint, triggering the initiation of the OAuth flow.
2. The user will be redirected to the Google authentication page, where they will be prompted to log in and grant permission for the application to access their Google Calendar data.
3. After successful authentication and authorization, the user will be redirected back to the `/rest/v1/calendar/redirect/` endpoint.

### `/rest/v1/calendar/redirect/` - `GoogleCalendarRedirectView()`

This endpoint handles the redirect request sent by Google after the user grants authorization. It performs two tasks:

1. Handles the redirect request and retrieves the authorization code from Google.
2. Uses the authorization code to obtain the access token for the user's Google Calendar.

#### Steps:
1. Google redirects the user to this endpoint with the authorization code.
2. The endpoint retrieves the authorization code from the request parameters.
3. Using the authorization code, the endpoint exchanges it for an access token by making a request to Google's token endpoint.
4. Upon successful retrieval of the access token, the endpoint can make subsequent requests to the Google Calendar API on behalf of the user.
5. The endpoint fetches the list of events from the user's calendar using the obtained access token.

## Getting Started

To get started with this repository, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/akashraj98/googleconnect.git
2. Install the required dependencies using pip:
3. ```shell
   pip install -r requirements.txt
5. Set up Google API credentials:
  Go to the Google Cloud Console.
  Create a new project (or select an existing one).
  Enable the Google Calendar API for the project.
  Create OAuth 2.0 credentials for the project.
  Download the credentials file (JSON format).
  Rename the downloaded file to credentials.json.
  Place the credentials.json file in the root directory of the repository.
  
  5.Start the Django development server:

  ```shell
  python manage.py runserver

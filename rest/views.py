from rest_framework.views import APIView
import google.oauth2.credentials
import google_auth_oauthlib.flow
from django.shortcuts import redirect
import googleapiclient.discovery
from django.http import (
    JsonResponse,
)

CLIENT_SECRETS_FILE = "credentials.json"
SCOPES = ['https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/userinfo.email']
REDIRECT_URL = 'http://127.0.0.1:8000/rest/v1/calendar/redirect'
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

# Create your views here.
class GoogleCalenderInit(APIView):
  def get(self,request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'client_secret.json',scopes=SCOPES)
    flow.redirect_uri(REDIRECT_URL)
    authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true')
    if 'error' in authorization_url:
      return JsonResponse({"status":False,"redirect_url":""},status=401)
    request.session['state'] = state
    return JsonResponse({"status":False,"redirect_url":authorization_url},status=200)


class GoogleCalendarRedirect(APIView):
  def get(self,request):
    state = request.session.get('state')
    # match state here
    if not state:
      return JsonResponse({"status":False,"message":"State is missing "},status=401)
    authorization_response = request.get_full_path()
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'client_secret.json',scopes=SCOPES)
    flow.redirect_uri(REDIRECT_URL)
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    request.session['credentials'] = {
      'token': credentials.token,
      'refresh_token': credentials.refresh_token,
      'token_uri': credentials.token_uri,
      'client_id': credentials.client_id,
      'client_secret': credentials.client_secret,
      'scopes': credentials.scopes
    }
    if 'credentials' not in request.session:
        return redirect('google_permission')
    credentials = google.oauth2.credentials.Credentials(
      **request.session['credentials'])
    calendar = googleapiclient.discovery.build(
      API_SERVICE_NAME, API_VERSION, credentials=credentials)
    events_result = calendar.events().list(calendarId='primary', maxResults=10).execute()
    events = events_result.get('items', [])
    data = []
    for event in events:
      data.append(event['summary'])
        
    return JsonResponse({
      "status": True, "message": "Events listed successfully", "data":data
    },status=200)
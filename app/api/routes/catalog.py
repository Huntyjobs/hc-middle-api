import json

import requests
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from settings import Settings

import google.auth.transport.requests
import google.oauth2.id_token

settings = Settings()
catalog_router = APIRouter(prefix=f"{settings.BASE_API_PREFIX}/catalog")

# https://stackoverflow.com/questions/64252736/google-cloud-build-fetch-identity-token
@catalog_router.post(
	"/",
	tags=["catalog"],
	status_code=status.HTTP_200_OK,

)
def request_to_catalog():
	try:
		service_url = settings.SERVICE_URL+"/"
		service_audience = settings.SERVICE_AUDIENCE_URL+"/"
		
		auth_req = google.auth.transport.requests.Request()
		id_token = google.oauth2.id_token.fetch_id_token(auth_req, service_audience)

		service_headers = {
			"Authorization":f"Bearer {id_token}"
		}

		print("url: " + service_url)
		print("audience: " + service_audience)
		print("headers: " + json.dumps(service_headers))

		response = requests.post(url=service_url, headers=service_headers)

		return response.json()

	except Exception:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="ERROR")




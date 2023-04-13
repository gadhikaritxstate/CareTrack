from rest_framework import status

from rest_framework import status

"""
HTTP status codes are three-digit codes, and are grouped into five
different classes.The class of a status code can be quickly identified
by its first digit:
    1xx: Informational
    2xx: Success
    3xx: Redirection
    4xx: Client Error
    5xx: Server Error
We will focus on identifying and troubleshooting the most commonly encountered
HTTP error codes,i.e. 4xx and 5xx status codes, from a developer’s perspective.
"""


OK = status.HTTP_200_OK

# This means the content has been successfully created.
CREATED = status.HTTP_201_CREATED

# This means the content has been successfully updated.
UPDATED = status.HTTP_206_PARTIAL_CONTENT

# This means that client-side input fails validation.
BAD_REQUEST = status.HTTP_400_BAD_REQUEST

# This means the user isn’t authorized to access a resource.
# It usually returns when the user isn’t authenticated..
UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED

#  This means the user is authenticated, but it’s not allowed
#  to access a resource.
FORBIDDEN = status.HTTP_403_FORBIDDEN

# Server unable to locate the requested file or resource.
NOT_FOUND = status.HTTP_404_NOT_FOUND

# The payload format or content type is in an unsupported format
UNSUPPORTED_MEDIA_TYPE = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

# The user agent is accidentally sending an incorrect HTTP method.
METHOD_NOT_ALLOWED = status.HTTP_405_METHOD_NOT_ALLOWED

# Server cannot process the request for an unknown reason.
# Missing package, packages not installed,server misconfiguration etc.
# Should not be thrown explicitly
INTERNAL_SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR

# This indicates an invalid response from an upstream server.
BAD_GATEWAY = status.HTTP_502_BAD_GATEWAY

# Server is overloaded or under maintenance.
# Not having enough CPU/memory resources to handle all of the incoming
# requests.
SERVICE_UNAVAILABLE = status.HTTP_503_SERVICE_UNAVAILABLE

# Server not receiving a response from the backend servers within
# the allowed time period
GATEWAY_TIMEOUT = status.HTTP_504_GATEWAY_TIMEOUT

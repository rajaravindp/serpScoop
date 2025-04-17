import httpx
import json

from typing import Dict, Type

# class NewsToolException(Exception):
#     """Base exception for news tools."""

# class InvalidWebsiteError(NewsToolException):
#     """Raised when an invalid website is provided."""

# class APIClientError(NewsToolException):
#     """Raised when an API client error occurs."""

EXCEPTION_HANDLERS: Dict[Type[Exception], str] = {
    json.JSONDecodeError: "JSON decode error occurred",
    AttributeError: "Parsing error occurred",
    httpx.HTTPError: "HTTP error occurred",
    httpx.RequestError: "Request error occurred",
    httpx.HTTPStatusError: "HTTP error occurred",
    httpx.TimeoutException: "Timeout error occurred",
    httpx.ConnectError: "Connection error occurred",
    httpx.NetworkError: "Network error occurred",
    httpx.TransportError: "Transport error occurred",
    httpx.ConnectTimeout: "Timed out while connecting to the host",
    httpx.ReadError: "Failed to receive data from the network",
    httpx.ReadTimeout: "Timed out while reading the response from the server",
    httpx.WriteError: "Failed to send data over the network",
    httpx.WriteTimeout: "Timed out while sending data to host",
    httpx.PoolTimeout: "Timed out waiting to acquire a connection from the pool",
    httpx.CloseError: "Failed to close the connection",
    httpx.ProtocolError: "Protocol violated",
    httpx.LocalProtocolError: "Protocol was violated by the client",
    httpx.RemoteProtocolError: "Protocol was violated by the server",
    httpx.ProxyError: "An error occurred while establishing a proxy connection",
    httpx.UnsupportedProtocol: "Attempted to make a request to an unsupported protocol",
    httpx.DecodingError: "Decoding of the response failed, due to a malformed encoding",
    httpx.TooManyRedirects: "Too many redirects occurred",
    httpx.InvalidURL: "URL is improperly formed or cannot be parsed",
    httpx.CookieConflict: "Attempted to lookup a cookie by name, but multiple cookies existed",
    httpx.StreamError: "The developer made an error in accessing the request stream in an invalid way",
    httpx.StreamConsumed: "Attempted to read or stream content, but the content has already been streamed",
    httpx.StreamClosed: "Attempted to read or stream response content, but the request has been closed",
    httpx.ResponseNotRead: "Attempted to access streaming response content, without having called read()",
    httpx.RequestNotRead: "Attempted to access streaming request content, without having called read()",
    Exception: "An unexpected error occurred",
}


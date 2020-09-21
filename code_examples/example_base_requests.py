"""
This module provides code examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place into method_arg's list dictionaries all args which would be provided in rqeuests.get|post|etc functions.

"""
import parallel_requests
from parallel_requests.session import extended_session

# Dynamic HTTP requests
parallel_requests.request(
    method_args=[
        {
            "url": "https://mysite.com",
            "headers": {"accept": "*/*"},
            "params": {"param": True},
            "method": "get",
        },
        {
            "url": "https://mysite2.com",
            "headers": {"accept": "*/*"},
            "data": {"data": True},
            "method": "post",
        },
        # ...
    ]
)


# GET HTTP request
parallel_requests.get(
    method_args=[
        {
            "url": "https://mysite.com",
            "headers": {"accept": "*/*"},
            "params": {"param": True},
        },
        {
            "url": "https://mysite2.com",
            "headers": {"accept": "*/*"},
            "params": {"param": True},
        },
        {
            "url": "https://mysite3.com",
            "headers": {"accept": "*/*"},
            "params": {"param": True},
        },
        # ...
    ]
)

# POST HTTP request
parallel_requests.post(
    method_args=[
        {
            "url": "https://mysite.com",
            "headers": {"accept": "*/*"},
            "data": {"data": True},
        },
        {
            "url": "https://mysite2.com",
            "headers": {"accept": "*/*"},
            "data": {"data": True},
        },
        {
            "url": "https://mysite3.com",
            "headers": {"accept": "*/*"},
            "data": {"data": True},
        },
        # ...
    ]
)
# Other request types uses same to this code


# Session with context manager
with extended_session() as session:
    response = session.parallel_request(
        method_args=[
            {
                "url": "https://mysite.com",
                "headers": {"accept": "*/*"},
                "params": {"param": True},
                "method": "get",
            },
            {
                "url": "https://mysite2.com",
                "headers": {"accept": "*/*"},
                "data": {"data": True},
                "method": "post",
            },
            # ...
        ]
    )
    # Other requests uses like default requests, just add parallel_ at start of method name


# Session without context manager
session = parallel_requests.Session()
response = session.parallel_request(
    method_args=[
        {
            "url": "https://mysite.com",
            "headers": {"accept": "*/*"},
            "params": {"param": True},
            "method": "get",
        },
        {
            "url": "https://mysite2.com",
            "headers": {"accept": "*/*"},
            "data": {"data": True},
            "method": "post",
        },
        # ...
    ]
)
session.close()

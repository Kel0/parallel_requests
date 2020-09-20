# async_requests

## Usage
POST HTTP request usage:
```
>>> import parallel_requests
>>> from typing import List
>>>
>>>
>>> responses: parallel_requests.ListResponse = parallel_requests.post(
>>>     method_args=[{"url": "https://www.python.org"}],
>>>     max_workers=10
>>> )
>>> responses
[<Response [200]>]
```

GET HTTP request usage
```
>>> import parallel_requests
>>> from typing import List
>>>
>>>
>>> responses: parallel_requests.ListResponse = parallel_requests.get(
>>>     method_args=[{"url": "https://www.python.org"}],
>>>     max_workers=10
>>> )
>>> responses
[<Response [200]>]
```

request function usage:
```
>>> import parallel_requests
>>> from typing import List
>>>
>>>
>>> responses: parallel_requests.ListResponse = parallel_requests.request(
>>>     method_args=[{"url": "https://www.python.org", "method": "post"}],
>>>     max_workers=10
>>> )
>>> responses
[<Response [200]>]
```
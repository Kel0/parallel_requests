# parallel_requests [![BCH compliance](https://bettercodehub.com/edge/badge/Kel0/parallel_requests?branch=master)](https://bettercodehub.com/)
## Installation
[pypi](https://pypi.org/project/parallel-requests/)
```
pip install parallel-requests
```
[github](https://github.com/Kel0/parallel_requests)
```
https://github.com/Kel0/parallel_requests.git
cd parallel_requests
pip install -e .
```
## Perfomance
See [benchmarks](https://github.com/Kel0/parallel_requests/tree/master/benchmarks)

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

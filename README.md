# parallel_requests [![Build Status](https://cloud.drone.io/api/badges/Kel0/parallel_requests/status.svg?branch=master)](https://cloud.drone.io/Kel0/parallel_requests/)
## Installation
[pypi](https://pypi.org/project/parallel-requests/)
```commandline
pip install parallel-requests
```
[github](https://github.com/Kel0/parallel_requests)
```commandline
https://github.com/Kel0/parallel_requests.git
cd parallel_requests
pip install -e .
```
## Perfomance
See [benchmarks](https://github.com/Kel0/parallel_requests/tree/master/benchmarks)

## Usage
POST HTTP request usage:
```python
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
```python
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
```python
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

# Commands
> For `robows.py`

```bash
$ curl http://localhost:8888/
{"stamp": "2022-11-27T17:54:30.658154"}
 
$ curl localhost:8888/
{"stamp": "2022-11-27T17:54:30.658154"}
 
$ curl -X POST localhost:8888/forward
{"status": "success"}
 
$ curl -X POST localhost:8888/backward
{"status": "success"}
 
$ curl -X POST localhost:8888/forward -d '{"speed": 1}'
{"status": "success"}
 
$ curl -X POST localhost:8888/forward -d '{"duration": 0.5, "speed": 1}'
{"status": "success"}
```
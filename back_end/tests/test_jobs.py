import requests

response = requests.get("http://localhost:8000")
print(response.status_code)
print(response.json())

response = requests.post("http://localhost:8000/api/jobs/create_job", data=dict(job_number="RBK904567"))
print(response.status_code)
print(response.json())

response_id = response.id

response = requests.post("http://localhost:8000/api/jobs/update_job", data=dict(id=response_id, job_number="RBK100000"))
print(response.status_code)
print(response.json())

response = requests.post("http://localhost:8000/api/jobs/read_job", data=dict(id=response_id))
print(response.status_code)
print(response.json())

response = requests.post("http://localhost:8000/api/jobs/delete_job", data=dict(id=response_id))

response = requests.post("http://localhost:8000/api/jobs/read_job", data=dict(id=response_id))
print(response.status_code)
print(response.json)
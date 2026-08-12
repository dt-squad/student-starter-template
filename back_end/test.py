import requests

response = requests.get("http://localhost:8000")
print(response.status_code)
print(response.json())

response = requests.post("http://localhost:8000/api/jobs/create_job", data=dict(job_number="RBK904567"))
print(response.status_code)
print(response.json())
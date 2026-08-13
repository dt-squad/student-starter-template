import requests


def test_get_jobs():
    response = requests.post("http://localhost:8000/api/jobs/read_job_all")
    print(response.status_code)
    print(response.json())

def test_create_job():
    response = requests.post("http://localhost:8000/api/jobs/create_job", data=dict(job_number="RBK904567"))
    
    response_dict = response.json()
    if response_dict.get("rc") == 0:
        print("Job created successfully.")
        # return "success"
    else:
        print("Job creation failed.")
        return "failure"
    if response_dict.get("job")["job_number"] == "RBK904567":
        print("Job number matches.")
        

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
print(response.json())

if __name__ == "__main__":
    passes = 0
    failures = 0
    tests_that_failed = []
    if test_get_jobs() == "success":
        passes += 1
    else:
        failures += 1
        tests_that_failed.append("test_get_jobs")

    if test_create_job() == "success":
        passes += 1
    else:
        failures += 1

    print(f"Tests passed: {passes}")
    print(f"Tests failed: {failures}")
    for test in tests_that_failed:
        print(f"Test failed: {test}")
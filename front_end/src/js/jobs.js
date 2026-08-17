export class Job_Service {
    constructor(domain_origin, notifyCallback = null) {
        this.domain_origin = domain_origin || "http://localhost:8003";
        this.notify = notifyCallback;
        this.new_job = {
            job_number: "",
            address: "",
            postcode: "",
            complaint_id: ""
        };
        this.jobs = [];
    }

    async create_job() {
        const rawComplaintId = this.new_job.complaint_id;
        const validComplaintId = (rawComplaintId && rawComplaintId.trim() !== '') ? rawComplaintId.trim() : null;

        const payload = {
            job_number: this.new_job.job_number,
            address: this.new_job.address,
            postcode: this.new_job.postcode,
            complaint_id: validComplaintId
        };

        const response = await fetch(`${this.domain_origin}/api/jobs/create`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const res = await response.json();
        if (this.notify) this.notify(res);
        return res;
    }

    async read_all_jobs() {
        const response = await fetch(`${this.domain_origin}/api/jobs/read_all`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
        });

        const res = await response.json();
        this.jobs = res.jobs || [];
        return this.jobs;
    }

    async delete_job(jobId) {
        const response = await fetch(`${this.domain_origin}/api/jobs/delete`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: jobId })
        });

        const res = await response.json();
        if (this.notify) this.notify(res);
        return res;
    }

    async update_job(editForm) {
        const rawComplaintId = editForm.complaint_id;
        const validComplaintId = (rawComplaintId && typeof rawComplaintId === 'string' && rawComplaintId.trim() !== '')
            ? rawComplaintId.trim()
            : null;

        const payload = {
            id: editForm.id,
            job_number: editForm.job_number,
            address: editForm.address,
            postcode: editForm.postcode,
            complaint_id: validComplaintId
        };

        const response = await fetch(`${this.domain_origin}/api/jobs/update`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const res = await response.json();
        if (this.notify) this.notify(res);
        return res;
    }

    async read_all_complaints() {
        const response = await fetch(`${this.domain_origin}/api/complaints/read_all`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                id: null,
                complaint_number: null,
                stage: null
            })
        });

        const res = await response.json();
        return res.complaints || res;
    }
}
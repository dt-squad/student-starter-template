export class Job_Service{
    constructor(domain_origin) {
        this.domain_origin = "http://localhost:8003"
        this.new_job = {
            job_number: "",
            address: "",
            postcode: "",
            complaint_id: ""
        }
        this.jobs=[]
        
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

        const response = await fetch(
            `${this.domain_origin}/api/jobs/create`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            }
        );

        if (!response.ok) {
            const errorData = await response.json();
            console.error("Validation error:", errorData);
            throw new Error("Failed to create job");
        }

        return await response.json();
    }

    async read_all_jobs() {
        const response = await fetch(
            `${this.domain_origin}/api/jobs/read_all`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({})
            }
        );
        this.jobs = await response.json();
        return this.jobs
    }

    async delete_job(jobId){
        const response = await fetch(
            `${this.domain_origin}/api/jobs/delete`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({id: jobId})
            }
        );
        return await response.json();
    }

    async update_job(editForm) {
        const rawComplaintId = editForm.complaint_id;
        const validComplaintId = (rawComplaintId && typeof rawComplaintId === 'string' && rawComplaintId.trim() !== '')
            ? rawComplaintId.trim()
            : null;

        const payload = {
            id: editForm.id, // Must be the string UUID only
            job_number: editForm.job_number,
            address: editForm.address,
            postcode: editForm.postcode,
            complaint_id: validComplaintId
        };

        const response = await fetch(`${this.domain_origin}/api/jobs/update`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error("Update failed:", errorData);
            throw new Error("Failed to update job");
        }

        return await response.json();
    }

    async read_all_complaints() {
        const response = await fetch(
            `${this.domain_origin}/api/complaints/read_all`,
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    id: null,
                    complaint_number: null,
                    stage: null
                })
            }
        );

        if (!response.ok) {
            console.error("Failed to fetch complaints:", response.statusText);
            return []; // Return empty array so Vue doesn't crash
        }

        return await response.json();
    }
}

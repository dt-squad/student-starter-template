export class Job_Service{
    constructor(domain_origin) {
        this.domain_origin = "http://localhost:8003"
        this.new_job = {
            job_number: "A",
            address: "B",
            postcode: "C",
            complaint_id: "708d0b90-5836-4dfb-a115-e9abf89d069c"
        }
        
    }

    async create_job(){
        const response = await fetch(
            `${this.domain_origin}/api/job/create`,
            {
                method: 'POST',
                ...(this.new_job ? { body: JSON.stringify(this.new_job) } : {}),
            },
        )
        return await response.json()
    }

    async read_all_jobs(filters = {}){
        const response = await fetch(
            `${this.domain_origin}/api/job/read_all`,
            {
                method: 'POST',
                ...(this.read_all_jobs ? {body: JSON.stringify(this.read_all_jobs)} : {}),
            },
        );
        return await response.json();
    }
}

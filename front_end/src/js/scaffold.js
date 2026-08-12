export class Scaffold_Service{
    constructor(domain_origin) {
        this.domain_origin = "http://localhost:8003"
        this.new_scaffold = {
            job_id: "f7b2a62f-0722-4db7-93ce-102b75d2ef0a",
            use: "Inspection",
            status: "REQUESTED",
            resource_id: "e0d0902b-08b6-424e-8942-7bcfe0a66a3e"
        }
        
    }

    async create_scaffold(){
        const response = await fetch(
            `${this.domain_origin}/api/scaffold/create/`,
            {
                method: 'POST',
                ...(this.new_scaffold ? { body: JSON.stringify(this.new_scaffold) } : {}),
            },
        )
        return await response.json()
    }


}
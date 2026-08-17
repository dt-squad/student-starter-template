<template>
    <h1 class="m-4"> Welcome to Job Tracker </h1>
    <div class="row d-flex justify-content-evenly mb-2">
        <div class="card col-6 shadow" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">Jobs</h5>
                <p class="card-text">View existing jobs, raise new jobs or edit and delete old jobs</p>
            </div>
            <div class="card-footer">    
                <button class="btn btn-success" type="button" @click="$router.push('/manage_jobs')">Go to Jobs</button>
            </div>
        </div>
        <div class="card col-6 shadow" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">Complaints</h5>
                <p class="card-text">View a list of complaints, all complaint jobs, add new complaints or update existing ones.</p>
            </div>
            <div class="card-footer">    
                <button class="btn btn-success" type="button"  aria-disabled="true">Go to Complaints</button>
            </div>
        </div>
    </div>

    <div class="row d-flex justify-content-evenly mb-2">
        <div class="card col-6 shadow" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">Scaffold</h5>
                <p class="card-text">Live tracker of all erected scaffolds, on going scaffold requests and a record of past erections.</p>
            </div>
            <div class="card-footer">    
                <button class="btn btn-success" type="button" aria-disabled="true">Go to Scaffold Requests</button>
            </div>
        </div>
        <div class="card col-6 shadow" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">Resources</h5>
                <p class="card-text">View contact details of resources, jobs assigned to them and KPIs.</p>
            </div>
            <div class="card-footer">
                <button class="btn btn-success" type="button"  aria-disabled="true">Go to Resources</button>
            </div>
        </div>        
    </div>

</template>

<script>
import Greeting from '../components/Greeting.vue';

export default{
    name: 'home',
    components: {
        Greeting,
    },
    
}
</script>

<style scoped>
.card-footer{
    background-color: unset;
}
</style>
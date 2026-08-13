<template>
  <button type="button" @click="$router.push('/manage_jobs')">Jobs</button>
  <RouterView :job_service="job_service" />
</template>

<script>
import { reactive } from "vue"
import { Job_Service } from "./js/jobs.js"


export default {
  name: 'App',
  data() {
    return {
      job_service: {}
    }
  },
  created() {
    let domain_origin = window.location.origin
    this.job_service = reactive(new Job_Service(domain_origin))
  }
}
</script>


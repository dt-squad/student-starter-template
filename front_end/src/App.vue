<template>
    <button type="button" @click="this.$router.push('/manage_jobs')">Jobs</button>
  <RouterView :job_service="job_service"/>
</template>

<script>
import {reactive} from "vue"
import { Job_Service } from "./js/jobs.js";
import router from "./router/index.js"

export default {
  name: 'App',
  data() {
    return {
      number:0,
      job_service:{

      }
    }
  },
  created(){
    let domain_origin = window.location.origin
    const job_service = reactive(new Job_Service(domain_origin))
    this.job_service = job_service
    }
}

</script>
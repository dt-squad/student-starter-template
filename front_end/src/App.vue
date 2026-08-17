<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Job Tracker</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <button class="nav-link" type="button" @click="$router.push('/')">Home</button>
          </li>
          <li class="nav-item">
            <button class="nav-link" type="button" @click="$router.push('/manage_jobs')">Jobs</button>
          </li>
          <li class="nav-item dropdown">
            <button class="nav-link disabled" type="button" aria-disabled="true">Scaffold</button>
          </li>
          <li class="nav-item">
            <button class="nav-link disabled" type="button"  aria-disabled="true">Complaints</button>
          </li>
          <li class="nav-item">
            <button class="nav-link disabled" type="button"  aria-disabled="true">Resources</button>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2 disabled" type="search" placeholder="Search" aria-label="Search"/>
          <button class="btn btn-outline-success disabled" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>

  <RouterView :job_service="job_service" />

  <div v-if="status.message" class="position-fixed bottom-0 end-0 m-3 alert alert-dismissible fade show pe-5" :class="status.isError ? 'alert-danger' : 'alert-success'" role="alert">
    <span>{{ status.message }}</span>
    <button type="button" class="btn-close" @click="status.message = ''" aria-label="Close"></button>
  </div>
</template>

<script>
import { reactive } from "vue"
import { Job_Service } from "./js/jobs.js"


export default {
  name: 'App',
  data() {
    return {
      job_service: {},
      status: {
        message: '',
        isError: false,
      }
    }
  },
  created() {
    let domain_origin = window.location.origin
    this.job_service = reactive(new Job_Service(domain_origin, this.toast))
  },
  methods: {
    toast(res) {
      if (!res || !res.message) return

      this.status.message = res.message
      this.status.isError = res.rc !== 0

      setTimeout(() => {
        this.status.message = ''
      }, 40000)
    }
  }
}
</script>


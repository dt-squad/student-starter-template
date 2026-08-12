<template>
  <div>
    <h2>Manage Jobs</h2>

    <!-- Create Job Form -->
    <div>
      <input type="text" name="job_number" v-model="job_service.new_job.job_number" />
      <button type="button" @click="handleCreateJob">Create Job</button>
    </div>

    <!-- Jobs List Table -->
    <table border="1" style="margin-top: 20px; width: 100%;">
      <thead>
        <tr>
          <th>Job Number</th>
          <th>Address</th>
          <th>Postcode</th>
          <th>Complaint ID</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="job in jobs" :key="job.id">
          <td>{{ job.job_number }}</td>
          <td>{{ job.address }}</td>
          <td>{{ job.postcode }}</td>
          <td>{{ job.complaint_id }}</td>
        </tr>
        <tr v-if="jobs.length === 0">
          <td colspan="4">No jobs found.</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ManageJobsView',
  props: ["job_service"],
  data() {
    return {
      jobs: []
    };
  },
  async mounted() {
    await this.fetchJobs();
  },
  methods: {
    async fetchJobs() {
      this.jobs = await this.job_service.read_all_jobs();
    },
    async handleCreateJob() {
      await this.job_service.create_job();
      await this.fetchJobs();
    }
  }
}
</script>
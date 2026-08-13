<template>
  <div>
    <h2>Manage Jobs</h2>

    <!-- Create Job Form -->
    <div class="row">
      <div class="column">
        <label for="job_number">Job Number</label>
        <input id="job_number" type="text" name="job_number" v-model="job_service.new_job.job_number" />
      </div>
      <div class="column">
        <label for="address">Address</label>
        <input type="text" name="address" v-model="job_service.new_job.address" />
      </div>
      <div class="column">
        <label for="postcode">Postcode</label>
        <input type="text" name="postcode" v-model="job_service.new_job.postcode" />
      </div>
      <div class="column">
        <label for="complaint_id">Complaint ID</label>
        <input type="text" name="complaint_id" v-model="job_service.new_job.complaint_id" />
      </div>
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
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="job in jobs" :key="job.id">
          <template v-if="editingJobId === job.id">
            <td><input type="text" v-model="editForm.job_number" /></td>
            <td><input type="text" v-model="editForm.address" /></td>
            <td><input type="text" v-model="editForm.postcode" /></td>
            <td><input type="text" v-model="editForm.complaint_id" /></td>
            <td>
              <button type="button" @click="handleSaveUpdate">Save</button>
              <button type="button" @click="cancelEdit">Cancel</button>
            </td>
          </template>

          <template v-else>
            <td>{{ job.job_number }}</td>
            <td>{{ job.address }}</td>
            <td>{{ job.postcode }}</td>
            <td>{{ job.complaint_id }}</td>
            <td>
              <button type="button" @click="startEdit(job)">Edit</button>
              <button type="button" @click="handleDeleteJob(job.id)">Delete</button>
            </td>
          </template>
        </tr>

        <tr v-if="jobs.length === 0">
          <td colspan="5">No jobs found.</td>
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
      jobs: [],
      editingJobId: null,
      editForm: {
        id: null,
        job_number: '',
        address: '',
        postcode: '',
        complaint_id: ''
      }
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
    },

    async handleDeleteJob(jobId) {
      await this.job_service.delete_job(jobId);
      await this.fetchJobs(); 
    },

    startEdit(job) {
      this.editingJobId = job.id;
      this.editForm = { ...job };
    },

    cancelEdit() {
      this.editingJobId = null;
      this.editForm = { id: null, job_number: '', address: '', postcode: '', complaint_id: '' };
    },

    async handleSaveUpdate() {
      await this.job_service.update_job(this.editForm);
      this.cancelEdit();
      await this.fetchJobs();
    }
  }
}
</script>

<style>
.row{
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  gap: 10px;
}

.column{
  display: flex;
  flex-direction: column;
  gap: 3px;
}
</style>
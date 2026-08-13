<template>
  <div>
    <h2>Manage Jobs</h2>

    <div class="row mb-3">
      <div class="col-3">
        <label for="job_number">Job Number</label>
        <input id="job_number" type="text" name="job_number" v-model="job_service.new_job.job_number" />
      </div>
      <div class="col-3">
        <label for="address">Address</label>
        <input type="text" name="address" v-model="job_service.new_job.address" />
      </div>
      <div class="col-3">
        <label for="postcode">Postcode</label>
        <input type="text" name="postcode" v-model="job_service.new_job.postcode" />
      </div>
      <div class="col-3">
        <label for="complaint_id">Complaint</label>
        <select id="complaint_id" v-model="job_service.new_job.complaint_id">
          <option :value="null">-- None --</option>
          <option v-for="complaint in complaints" :key="complaint.id" :value="complaint.id">
            {{ complaint.complaint_number || complaint.id }}
          </option>
        </select>
      </div>
      <button type="button" @click="handleCreateJob">Create Job</button>
    </div>

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
        <tr v-for="job in job_service.jobs" :key="job.id">
          <template v-if="editingJobId === job.id">
            <td><input type="text" v-model="editForm.job_number" /></td>
            <td><input type="text" v-model="editForm.address" /></td>
            <td><input type="text" v-model="editForm.postcode" /></td>
            <td>
              <select v-model="editForm.complaint_id">
                <option :value="null">-- None --</option>
                <option v-for="complaint in complaints" :key="complaint.id" :value="complaint.id">
                  {{ complaint.complaint_number || complaint.id }}
                </option>
              </select>
            </td>
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

        <tr v-if="job_service.jobs.length === 0">
          <td colspan="5">No jobs found.</td>
        </tr>

      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ManageJobsView',
  props: ["job_service", "complaint_service"],
  data() {
    return {
      complaints: [],
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
    await this.fetchComplaints();
  },
  methods: {
    async fetchJobs() {
      await this.job_service.read_all_jobs();
    },

    async fetchComplaints() {
      this.complaints = await this.job_service.read_all_complaints();
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
<template>
  <div>
    <h2 class="m-4">Manage Jobs</h2>

    <button type="button" class="shadow btn btn-primary" data-bs-toggle="modal" data-bs-target="#newJobModel">
      Add New Job
    </button>

    <table class="table" border="1" style="margin-top: 20px; width: 100%;">
      <thead>
        <tr>
          <th scope="col">Job Number</th>
          <th scope="col">Address</th>
          <th scope="col">Postcode</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="job in job_service.jobs" :key="job.id" class="align-middle">
          <template v-if="editingJobId === job.id">
            <th class="col-2 table-light" scope="row">
              <input class="form-control mb-2" type="text" v-model="editForm.job_number" />
              <select class="form-control" v-model="editForm.complaint_id">
                <option :value="null">-- None --</option>
                <option v-for="complaint in complaints" :key="complaint.id" :value="complaint.id">
                  {{ complaint.complaint_number || complaint.id }}
                </option>
              </select>
            </th>
            <td class="col-2 table-light">
              <input class="form-control" type="text" v-model="editForm.address" />
            </td>
            <td class="col-2 table-light">
              <input class="form-control" type="text" v-model="editForm.postcode" />
            </td>
            <td class="col-2 table-light">
              <button class="btn btn-success py-1 px-2 mx-2" type="button" @click="handleSaveUpdate">Save</button>
              <button class="btn btn-danger py-1 px-2 mx-2" type="button" @click="cancelEdit">Cancel</button>
            </td>
          </template>

          <template v-else>
            <td>
              <div class="fw-semibold">{{ job.job_number }}</div>
              <small class="text-muted d-block">{{ getComplaintNumber(job.complaint_id) }}</small>
            </td>
            <td >{{ job.address }}</td>
            <td >{{ job.postcode }}</td>
            <td >
              <button class="btn btn-warning py-1 px-2 mx-2" type="button" @click="startEdit(job)">Edit</button>
              <button class="btn btn-danger py-1 px-2 mx-2" type="button" @click="handleDeleteJob(job.id)">Delete</button>
            </td>
          </template>
        </tr>

        <tr v-if="job_service.jobs.length === 0">
          <td colspan="5">No jobs found.</td>
        </tr>

      </tbody>
    </table>
  </div>

<!-- Model for adding a job -->
<div class="modal" id="newJobModel" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Add New Job</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body col-12 mb-2">
        <div class="row">
          <div class="col-6">
            <label for="job_number">Job Number</label>
            <input id="job_number" type="text" name="job_number" v-model="job_service.new_job.job_number" />
          </div>
          <div class="col-6">
            <label for="complaint_id">Complaint</label>
            <select id="complaint_id" v-model="job_service.new_job.complaint_id">
              <option :value="null">-- None --</option>
              <option v-for="complaint in complaints" :key="complaint.id" :value="complaint.id">
                {{ complaint.complaint_number || complaint.id }}
              </option>
            </select>
          </div>
        </div>
        <div class="row">
          <div class="col-6">
            <label for="address">Address</label>
            <input type="text" name="address" v-model="job_service.new_job.address" />
          </div>
          <div class="col-6">
            <label for="postcode">Postcode</label>
            <input type="text" name="postcode" v-model="job_service.new_job.postcode" />
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button class="btn btn-primary" type="button" data-bs-dismiss="modal" @click="handleCreateJob">Create Job</button>
      </div>
    </div>
  </div>
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
    },
    getComplaintNumber(complaintId) {
      if (!complaintId) return '-- None --';
      const complaint = this.complaints.find(c => c.id === complaintId);
      return complaint ? (complaint.complaint_number || complaint.id) : '-- None --';
    },

  }
}
</script>
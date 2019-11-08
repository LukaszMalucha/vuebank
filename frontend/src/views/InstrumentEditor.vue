<template>
 <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="container text-center container-welcome">
          <div class="row">
            <h3>Add Instrument</h3>
          </div>
          <div class="row">
          <div class="col-md-4 plain-element"></div>
          <div class="col-md-4 plain-element">
            <form @submit.prevent="onSubmit">
              <textarea v-model="instrument_body" rows="2" class="form-control" placeholder="details"
              <br>
              <button type="submit" class="btn btn-success">
                Publish
              </button>
            </form>
            <p v-if="error" class="muted">{{ error }}</p>

          </div>
          <div class="col-md-4 plain-element"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { apiService } from "../common/api.service.js"

export default {
  name: "InstrumentEditor",
  data() {
    return {
      instrument_body: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (!this.instrument_body) {
        this.error = "Can't be empty"
      } else if (this.instrument_body.length > 255) {
        this.error = "Can't be longer than 255 characters"
      } else {
        let endpoint = "/portfolio/instruments/";
        let method = "POST";
        apiService(endpoint, method, {content: this.instrument_body })
          .then(instrument_data => {
            this.$router.push({ name: 'instrument', params: { slug: instrument_data.slug}
            })
          })
      }
    }
  },
  created() {
    document.title = "Instrument Editor";
  }
}
</script>
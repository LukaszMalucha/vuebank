<template>
 <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="container text-center container-welcome">
          <div class="row">
            <h3>Cash Transfer</h3>
          </div>
          <div class="row">
          <div class="col-md-4 plain-element"></div>
          <div class="col-md-4 plain-element">
            <form @submit.prevent="onSubmit">
              <textarea v-model="instrument_name" rows="1" class="form-control" placeholder="name">
              </textarea>
              <br>

              <button type="submit" class="btn btn-success">
                Cash Transfer
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
import { apiService } from "../common/api.service.js";

export default {
  name: "CashTransfer",
  data() {
    return {
      quantity: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
    if (!this.quantity) {
        this.error = "Can't be empty"
    } else if (
          this.instrument_quantity > 1000000) {
         this.error = "Quantity can't be larger than 1 million"
    } else {
      let endpoint = "/portfolio/cash-balance/";
      let method = "POST";
      apiService(endpoint, method, { quantity: this.quantity })
        .then(instrument_data => {
          this.$router.push({ name: 'buy'});
          console.log(data)
        })
      }
    }
  },
  created() {
    document.title = "Cash Transfer";
  }
}



</script>
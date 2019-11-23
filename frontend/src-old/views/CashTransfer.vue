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
              <input v-model="cash_quantity" type="number" placeholder="quantity" class="form-control">
              </input>
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
import { apiService } from "@/common/api.service.js";

export default {
  name: "CashTransfer",
  data() {
    return {
      cash_quantity: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
    if (!this.cash_quantity) {
        this.error = "Can't be empty";
    } else if (
          this.cash_quantity > 1000000) {
         this.error = "Quantity can't be larger than 1 million";
    } else {
      let endpoint = "/portfolio/cash-balance/";
      let method = "POST";
      apiService(endpoint, method, { quantity: this.cash_quantity, category: "Currency", price: 1.0 })
        .then(cash_data => {
          this.$router.push({
          name: 'cash-balance',
          })
        })
      }
    }
  },
  created() {
    document.title = "Cash Transfer";
  }
}



</script>
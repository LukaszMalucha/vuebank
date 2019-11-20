<template>
 <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="container text-center container-welcome">
          <div class="row">
            <h3>Buy Instrument</h3>
          </div>
          <div class="row">
          <div class="col-md-4 plain-element"></div>
          <div class="col-md-4 plain-element">
            <form @submit.prevent="onSubmit">
              <textarea v-model="instrument_name" rows="1" class="form-control" placeholder="name">
              </textarea>
              <br>
              <textarea v-model="instrument_symbol" rows="1" class="form-control" placeholder="symbol">
              </textarea>
              <br>
              <textarea v-model="instrument_category" rows="1" class="form-control" placeholder="category">
              </textarea>
              <br>
              <textarea v-model="instrument_price" rows="1" class="form-control" placeholder="price">
              </textarea>
              <br>
              <button type="submit" class="btn btn-success">
                Buy
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
  name: "Buy",
  data() {
    return {
      instrument_name: null,
      instrument_symbol: null,
      instrument_category: null,
      instrument_price: null,
      instrument_quantity: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
    if (!this.instrument_name || !this.instrument_symbol || !this.instrument_category || !this.instrument_quantity ||
          !this.instrument_price ) {
        this.error = "Can't be empty"
    } else if (
          this.instrument_quantity > 1000000) {
         this.error = "Quantity can't be larger than 1 million"
    } else {
      let endpoint = "/portfolio/buy/";
      let method = "POST";
      apiService(endpoint, method, {name: this.instrument_name, symbol: this.instrument_symbol,
                category: this.instrument_category, price: this.instrument_price, quantity: this.instrument_quantity })
        .then(instrument_data => {
          this.$router.push({ name: 'buy'});
          console.log(data)
        })
      }
    }
  },
  created() {
    document.title = "Buy Instrument";
  }
}
</script>
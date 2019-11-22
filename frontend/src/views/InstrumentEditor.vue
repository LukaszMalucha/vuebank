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
              <textarea v-model="instrument_name" rows="1" class="form-control" placeholder="name">
              </textarea>
              <br>
              <div class="input-field col s12">
                <select v-model="instrument_category">
                  <option v-for="option in options" :value="option">{{option}}</option>
                </select>
                <label>Materialize Select</label>
              </div>
              <br>
              <textarea v-model="instrument_symbol" rows="1" class="form-control" placeholder="symbol">
              </textarea>
              <br>
              <textarea v-model="instrument_price" rows="1" class="form-control" placeholder="price">
              </textarea>
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
import { apiService } from "@/common/api.service.js";

export default {
  name: "InstrumentEditor",
  data() {
    return {
      instrument_name: null,
      instrument_symbol: null,
      instrument_category: null,
      instrument_price: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (!this.instrument_name || !this.instrument_symbol || !this.instrument_category || !this.instrument_price ) {
        this.error = "Can't be empty"
      } else if (this.instrument_name.length > 255 ||
                 this.instrument_symbol.length > 255 ||
                 this.instrument_category.length > 255) {
        this.error = "Can't be longer than 255 characters"
      } else {
        let endpoint = "/portfolio/instruments/";
        let method = "POST";
        apiService(endpoint, method, {name: this.instrument_name, symbol: this.instrument_symbol, category: this.instrument_category, price: this.instrument_price })
          .then(instrument_data => {
            this.$router.push({ name: 'instruments'})
          })
      }
    }
  },
  created() {
    document.title = "Instrument Editor";
    this.options = ["Cryptocurrency", "Currency", "Stock", "Commodity"]
  }
}
</script>
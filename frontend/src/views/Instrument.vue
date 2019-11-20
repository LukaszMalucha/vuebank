<template>
  <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="row">
          <div class="col-md-4 plain-element"></div>
          <div class="col-md-4 plain-element">
            <div class="card card-instrument">
              <div class="card-header">
                <div class="row plain-element">
                  <div class="col-md-4 plain-element">
                    <div class="card-image">
                      <img alt="Currency" src="../assets/currency.png" class="img responsive"/>
                    </div>
                  </div>
                  <div class="col-md-8 plain-element">
                    <div class="card-title text-left">
                      <h5>{{ instrument.name }}</h5>
                        <table class="table table-company">
                          <tbody>
                            <tr>
                              <td>Category:</td>
                              <td><b>{{ instrument.category }}</b></td>
                            </tr>
                            <tr>
                              <td>Ticker:</td>
                              <td><b>{{ instrument.symbol }}</b></td>
                            </tr>
                            <tr>
                              <td>Current Price:</td>
                              <td><b>{{ instrument.price }} USD</b></td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
            <div class="card-content">
              <b class="instrument-website">
                <router-link :to="{ name: 'instrument', params: { slug: instrument.slug} }">
                    Buy
                </router-link>
              </b>
            </div>
          </div>
        </div>
        </div>
        <div class="row">
          <div class="col-md-4 plain-element"></div>
          <div class="col-md-4 plain-element">
            <div class="card text-center">
              <br>
              <form @submit.prevent="onSubmit">
                <br>
                <input v-model="assetQuantity" type="number" placeholder="quantity" class="form-control">
                </input>
                <br>
                <button type="submit" class="btn btn-success">
                  Buy
                </button>
              </form>
              <p v-if="error" class="muted">{{ error }}</p>
            </div>
          </div>
          <div class="col-md-4 plain-element"></div>
          </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js"

export default {
  name: 'Instrument',
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      instrument: {},
      assetQuantity: null,
      error: null,

    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getInstrumentData() {
      let endpoint = `/portfolio/instruments/${this.slug}/`;
      apiService(endpoint)
        .then(data => {
          this.instrument = data;
          this.setPageTitle(data.name)
        })
    },
    onSubmit() {
      console.log('XXX');
      let endpoint = "/portfolio/cash-balance/";
      let method = "POST";
      apiService(endpoint, method, { quantity: this.assetQuantity, category: "Currency", price: 1.0 })
        .then(cash_data => {
          this.$router.push({
          name: 'cash-balance',
          })
        })
      },
  },
  created() {
    this.getInstrumentData();
  }
}

</script>
<template>
<div id="page-index">
  <RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
    <h4>Buy  {{ instrument.name }}</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div v-if="instrument" class="dashboard-cards">
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
  <div v-else class="dashboard-cards">
    <div class="row">
      <div class="col-md-4 plain-element"></div>
      <div class="col-md-4 plain-element">
        <div class="card card-instrument">
          <div class="card-content">
            <h4> 404 - Page Not Found </h4>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</template>


<script>
import { apiService } from "@/common/api.service.js";
import RowHeaderComponent from "@/components/RowHeader.vue";

export default {
  name: 'BuyInstrument',
  components: {
    RowHeaderComponent,
  },
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
          if (data) {
            this.instrument = data;
            this.setPageTitle(data.name)
          } else {
            this.instrument = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    onSubmit() {
      let endpoint = "/portfolio/buy/";
      let method = "POST";
      apiService(endpoint, method, { quantity: this.assetQuantity, symbol: this.instrument.symbol, instrument: this.instrument.id })
        .then(data => {
          if (data) {
            console.log(data)
          }
//          this.$router.push({
//          name: 'cash-balance',
//          })
        })
      },
  },
  created() {
    this.getInstrumentData();
  }
}

</script>
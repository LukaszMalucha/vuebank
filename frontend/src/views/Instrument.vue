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
                    Buy/Sell
                </router-link>
              </b>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "../common/api.service.js"

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
      instrument: {}
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
    }
  },
  created() {
    this.getInstrumentData();
  }
}

</script>
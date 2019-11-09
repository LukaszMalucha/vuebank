<template>
 <div class="wrapper">
    <div id="page-index">
        <div class="dashboard-cards">
            <div class="container text-center container-welcome">
                <div class="row">
                    <h3>Available Instruments</h3>
                </div>
                <br>
                <div class="row">
                    <div v-for="instrument in instruments" :key="instrument.pk" class="col-md-4 text-center">
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
                <div class="row">
                  <div class="col-md-4 plain-element"></div>
                  <div class="col-md-4 plain-element">
                    <p v-show="loadingInstruments">...loading...</p>
                    <button v-show="next" @click="getInstruments" class="btn route">
                      Load More
                    </button>
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
  name: 'Instruments',
  data() {
    return {
        instruments: [],
        next: null,
        loadingInstruments: false
    }
  },
  methods: {
    getInstruments() {
    let endpoint = "/portfolio/instruments/";
    if (this.next) {
      endpoint = this.next;
    }
    this.loadingInstruments = true;
    apiService(endpoint)
      .then( data => {
          this.instruments.push(...data.results)
          this.loadingInstruments = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
     })
    }
  },
  created() {
    this.getInstruments();
    document.title = "Instruments";
  }
}
</script>
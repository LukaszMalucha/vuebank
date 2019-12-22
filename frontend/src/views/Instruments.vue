<template>
<div v-if="this.requestUser == 'undefined'" id="page-index">
<RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>Available Instruments</h4>
    </div>
    <div class="col-md-4 no-padding"></div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-error">
      <p v-if="error" class="muted error-message">{{ error }}</p>
    </div>
    <div class="row row-cards">
    <div class="row text-center">
          <h5>You have to login first:</h5>
    </div>
    <div class="row text-center">
          <button onclick="window.location.href='/user/login'"  type="submit" class="btn btn-confirm btn-login">
          Login
          </button>
    </div>
    </div>
  </div>
</div>
<div v-else id="page-index">
  <RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>Available Instruments</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
      <div class="col-md-10 col-lg-10 plain-element"></div>
      <div class="col-md-2 col-lg-2 plain-element">
        <div class="search-wrapper">
          <label> Search Asset:</label>
          <input type="text" v-model="search"/>
        </div>
      </div>
    </div>
    <div class="row row-cards">
      <table id="instrumentTable">
        <thead>
        <tr>
          <th onclick="sortTable(0)">Instrument</th>
          <th onclick="sortTable(1)" class="text-center">Symbol</th>
          <th onclick="sortTable(2)" class="text-center">Category</th>
          <th class="text-center">Price (USD)</th>
          <th colspan="2" class="text-center">Transaction</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="instrument in filteredList" :key="instrument.pk">
          <td>{{ instrument.name }}</td>
          <td class="text-center">{{ instrument.symbol }}</td>
          <td class="text-center">{{ instrument.category }}</td>
          <td class="text-center">{{ formatPrice(instrument.price) }}</td>
          <td class="text-center">
            <router-link :to="{ name: 'buy-instrument', params: { slug: instrument.slug} }">
              <button class="btn btn-transaction">Buy</button>
            </router-link>
          </td>
          <td class="text-center">
            <router-link :to="{ name: 'sell-instrument', params: { slug: instrument.slug} }">
              <button class="btn btn-transaction">Sell</button>
            </router-link>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js"
import RowHeaderComponent from "@/components/RowHeader.vue";


export default {
  name: 'Instruments',
  components: {
    RowHeaderComponent,
  },
  data() {
    return {
        search: '',
        instruments: [],
        requestUser: null,
        error: null,
    }
  },
  methods: {
    getInstruments() {
      if (this.requestUser !== "undefined") {
        let endpoint = "/portfolio/instruments/";
        apiService(endpoint)
          .then( data => {
          if (data) {
            this.instruments.push(...data.results)
          } else {
            this.error = "Something went wrong. We couldn't proceed with your request"
          }
         })
      } else {
        console.log("User has to login first.")
      }
    },
//  US price format
    formatPrice(value) {
      let val = (value/1).toFixed(2).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
  },
  computed: {
//  Search instruments function
    filteredList() {
      return this.instruments.filter(instrument => {
        return instrument.symbol.toLowerCase().includes(this.search.toLowerCase()) ||
                instrument.name.toLowerCase().includes(this.search.toLowerCase()) ||
                instrument.category.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.setRequestUser();
    this.getInstruments();
    document.title = "Trade Assets";

  }
}
</script>
<template>
<div v-if="this.requestUser == 'undefined'" id="page-index">
<RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>Transaction History </h4>
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
      <h4>Transaction History</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
      <div class="col-md-10 col-lg-10 plain-element"></div>
      <div class="col-md-2 col-lg-2 plain-element">
        <div class="search-wrapper">
          <label> Search Transactions:</label>
          <input type="text" v-model="search"/>
        </div>
      </div>
    </div>
    <div class="row row-cards">
      <table id="instrumentTable">
        <thead>
        <tr>
          <th onclick="sortTable(0)">Date & Time</th>
          <th onclick="sortTable(1)" class="text-center">Instrument</th>
          <th onclick="sortTable(2)" class="text-center">Buy/Sell</th>
          <th class="text-center">Quantity</th>
          <th class="text-center">Value (USD)</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="transaction in filteredList">
          <td>{{ formatDate (transaction.created_at) }}</td>
          <td class="text-center">{{ transaction.symbol }}</td>
          <td class="text-center capitalize">{{ formatSlug(transaction.slug) }}</td>
          <td class="text-center">{{ transaction.quantity }}</td>
          <td class="text-center">{{ formatPrice(transaction.value) }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";
import RowHeaderComponent from "@/components/RowHeader.vue";



export default {
  name: "TransactionHistory",
  components: {
    RowHeaderComponent,
  },
  data() {
    return {
      message: "Transaction History",
      transactions: [],
      search: '',
      requestUser: null,
      error: null,
    }
  },
  methods: {
    getBuyTransactions() {
      if (this.requestUser !== "undefined") {
        let endpoint = "/portfolio/buy/";
        apiService(endpoint)
        .then ( data =>{
          this.transactions.push(...data.results);
        })
      } else {
        console.log("User has to login first.")
      }
    },
    getSellTransactions() {
      if (this.requestUser !== "undefined") {
        let endpoint = "/portfolio/sell/";
        apiService(endpoint)
        .then ( data =>{
          this.transactions.push(...data.results);
//        Sort transactions by date
          this.transactions.sort((a, b) => (a.created_at < b.created_at) ? 1 : -1);
        })
      } else {
        console.log("User has to login first.")
      }
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
//  US price format
    formatPrice(value) {
      let val = (value/1).toFixed(2).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    },
//  Date converter
    formatDate(value) {
      let val = (value).replace('T', ' at ')
      return val.toString().slice(0, -8)
    },
//  Get buy/sell from transaction slug
    formatSlug(value) {
      let val = (value).replace('T', ' at ')
      return val.toString().split("-")[0]
    },
  },
  computed: {
//  Search transactions functionality
    filteredList() {
      return this.transactions.filter(transaction => {
        return transaction.symbol.toLowerCase().includes(this.search.toLowerCase()) ||
                transaction.created_at.toLowerCase().includes(this.search.toLowerCase()) ||
                transaction.slug.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.setRequestUser();
    this.getBuyTransactions();
    this.getSellTransactions();
  }
}
</script>
<template>
<div v-if="this.requestUser == 'undefined'" id="page-index">
<RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>Cash Transfer </h4>
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
      <h4>Cash Transfer</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div v-if="cash" class="dashboard-cards">
    <div class="row row-error">
      <p v-if="error" class="muted error-message">{{ error }}</p>
    </div>
    <div class="row row-cards">
      <div class="col-md-4 plain-element">
        <form @submit.prevent="onSubmit">
          <table class="table table-transaction">
            <tbody>
            <tr>
              <td>Cash Balance:</td>
              <td><b>{{ formatPrice(cash.quantity) }} USD</b></td>
            </tr>
            <tr class="transparent">
              <td>Transfer Amount:</td>
              <td class="cell-input">
                <input v-model="cash_quantity" type="number" placeholder="Specify amount..."
                       class="form-control form-control-transaction" id="quantityCounter" max="100000" min="1"/>
              </td>
            </tr>
            <br>
            </tbody>
          </table>
          <button type="submit" class="btn btn-confirm btn-success">Transfer</button>
        </form>
      </div>
    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";
import RowHeaderComponent from "@/components/RowHeader.vue";

export default {
  name: 'CashBalance',
  components: {
    RowHeaderComponent,
  },
  data() {
    return {
      cash: {},
      cash_quantity: null,
      error: null,
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
//  US price format
    formatPrice(value) {
      let val = (value/1).toFixed(2).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
    getCashData() {
      if (this.requestUser !== "undefined") {
        let endpoint = '/portfolio/cash-balance/';
        apiService(endpoint)
          .then(data => {
            if (data) {
              this.cash = data['results'][0];
            } else {
              this.instrument = null;
              this.setPageTitle("404 - Page Not Found")
            }
          })
      } else {
        console.log("User has to login first.")
      }
    },
    onSubmit() {
    if (!this.cash_quantity) {
        this.error = "Transfer amount field can't be empty";
    } else if (
         this.cash_quantity > 100000 ) {
         this.error = "Transfer amount can't be larger than 100k USD";
    } else if (
         this.cash_quantity < 1 ) {
         this.error = "Transfer amount can't be smaller than 1 USD";
    } else {
      let endpoint = "/portfolio/cash-balance/";
      let method = "POST";
      apiService(endpoint, method, { quantity: this.cash_quantity, category: "Currency", price: 1.0 })
        .then(data => {
          if (data) {
            this.$router.push({
            name: 'asset-manager',
            })
          }
          else {
            this.error = "Something went wrong. We couldn't proceed with your cash transfer"
          }
        })
      }
    }
  },
  created() {
    this.setRequestUser();
    this.getCashData();
    document.title = "Cash Transfer";
  }
}

</script>

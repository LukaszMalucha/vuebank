<template>
<div v-if="this.requestUser == 'undefined'" id="page-index">
<RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>Asset Portfolio </h4>
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
      <h4>Buy {{ instrument.name }} ({{instrument.symbol}})</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div v-if="instrument" class="dashboard-cards">
    <div class="row row-error">
      <p v-if="error" class="muted error-message">{{ error }}</p>
    </div>
    <div class="row row-cards">
      <div class="col-md-4 plain-element">
      <form @submit.prevent="onSubmit">
        <table class="table table-transaction">
          <tbody>
          <tr>
            <td>Instrument:</td>
            <td><b>{{ instrument.name }}</b></td>
          </tr>
          <tr>
            <td>Category:</td>
            <td><b>{{ instrument.category }}</b></td>
          </tr>
          <tr>
            <td>Ticker:</td>
            <td><b>{{ instrument.symbol }}</b></td>
          </tr>
          <tr>
            <td>Your Holdings:</td>
            <td><b>{{ instrument.user_holdings }}</b></td>
          </tr>
          <tr>
            <td>Cash On Hand:</td>
            <td><b>{{ formatPrice(instrument.cash_balance) }} USD</b></td>
          </tr>
          <tr>
            <td>Current Price:</td>
            <td><b>{{ formatPrice(instrument.price) }} USD</b></td>
          </tr>
          <tr>
            <td>Quantity:</td>
            <td class="cell-input">
              <input v-model="assetQuantity" type="number" placeholder="Specify quantity..."
                      class="form-control form-control-transaction" id="quantityCounter" max="1000000000"/>
            </td>
          </tr>
          <br>
          <tr>
          <td>Total:</td>
          <td><b>{{calcTotal()}}</b></td>
          </tr>
          </tbody>
        </table>

        <button type="submit" class="btn btn-confirm btn-success">Buy</button>
        </form>
      </div>
      <div class="col-md-4 plain-element">
      </div>
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
      assetQuantity: 0,
      cashBalance: 0,
      error: null,
    }
  },
  methods: {
//  Quick calculation for the website
    calcTotal: function() {
        if (this.assetQuantity < 1) {
          return 0 + " USD"
        }
        else if (this.assetQuantity > 1000000000) {
          return "Max. limit exceeded"
        }

        else {
          return this.formatPrice(((parseFloat(this.assetQuantity) ) * this.instrument.price).toFixed(2)) + " USD";
        }
    },
//  US price format
    formatPrice(value) {
      let val = (value/1).toFixed(2).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    },
    setPageTitle(title) {
      document.title = title;
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
    getInstrumentData() {
      let endpoint = `/portfolio/instruments/${this.slug}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.instrument = data;
            this.setPageTitle("Buy - "  + data.name);

          } else {
            this.instrument = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    onSubmit() {
    if (!this.assetQuantity) {
        this.error = "You have to specify amount you want to sell";
    } else if ( this.assetQuantity < 1 ) {
         this.error = "Transaction amount can't be smaller than 1";
    } else {
        let endpoint = "/portfolio/buy/";
        let method = "POST";
        apiService(endpoint, method, { quantity: this.assetQuantity, symbol: this.instrument.symbol, instrument: this.instrument.id })
        .then(data => {
          if (data.non_field_errors) {
              this.error = data.non_field_errors[0]
          } else if (!data) {
              console.log("Something went wrong. We couldn't proceed with your cash transfer")
          } else {
              this.$router.push({
              name: 'asset-manager',
              })
          }
        })
      }
    }
  },
  created() {
    this.getInstrumentData();
    this.setRequestUser();

  }
}

</script>
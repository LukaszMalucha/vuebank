<template>
<div id="page-index">
  <RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>Buy {{ instrument.name }} ({{instrument.symbol}})</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div v-if="instrument" class="dashboard-cards">
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
            <td>Current Price:</td>
            <td><b>{{ instrument.price }} USD</b></td>
          </tr>
          <tr>
            <td>Quantity:</td>
            <td class="cell-input">
              <input v-model="assetQuantity" type="number" placeholder="Specify quantity..."
                      class="form-control form-control-transaction" id="quantityCounter"/>
            </td>
          </tr>
          <br>
          <tr>
          <td>Total:</td>
          <td><b>200 USD</b></td>
          </tr>
          </tbody>
        </table>
        <p v-if="error" class="muted">{{ error }}</p>
        <button type="submit" class="btn btn-confirm btn-success">Buy</button>
        </form>
      </div>
      <div class="col-md-4 plain-element">
      <table>
        <thead>
        <td>Room Type</td>
        <td>Adult</td>
        <td>Children</td>
        <td>Total Price</td>
        </thead>
                <tbody>
                  <tr v-for="(row, index) in rows">
                    <td>
                      <select v-model="row.roomType">
                        <option v-for="room in rooms" v-bind:value="room.title">{{room.title}}</option>
                      </select>
                    </td>
                    <td>
                      <select v-model="row.adultCount">
                      <option value="1">1 Adult</option>
                      <option value="2">2 Adults</option>
                    </select>
                  </td>
                  <td>
                    <select v-model="row.childCount">
                    <option value="0">No Child</option>
                    <option value="1">1 Child</option>
                    <option value="2">2 Children</option>
                  </select>
                </td>
                <td>
                  {{calcRoomTotal(row)}}
                </td>
              </tr>
    </tbody>
  </table>
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
      assetQuantity: null,
      error: null,
      rows: [{
      roomType : "Standard Room",
      adultCount : 1,
      childCount : 0
      }],
      rooms: [
      {
          value:0,
          title: 'Standard Room'
      },
      {
          value:0,
          title: 'Deluxe Room'
      },
      ],
      items: [{
          price: 1000,
      }]
    }
  },
  methods: {
    addRoom: function() {
      this.rows.push({
      roomType : "Standard Room",
      adultCount : 1,
      childCount : 0
      });
    },

    removeRoom: function(index) {
      this.rows.splice(index, 1);
    },

    calcRoomTotal: function(row) {
        return (parseInt(row.adultCount) + parseInt(row.childCount)) * 1000;
    },

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
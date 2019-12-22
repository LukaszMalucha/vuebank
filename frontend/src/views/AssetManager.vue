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
      <h4 class="full-title"> Asset Portfolio - {{ this.requestUser }} </h4>
      <h4 class="short-title"> Asset Portfolio</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div v-if="assets.length == 1" class="dashboard-cards">
    <div class="row row-error">
      <p v-if="error" class="muted error-message">{{ error }}</p>
    </div>
    <div class="row row-cards">
          <div class="col-md-5 col-lg-4 plain-element">
            <table class="table table-transaction">
              <tbody>
              <tr>
                <td class="cash-cell">Cash on Hand:</td>
                <td v-for="asset in assets" v-if="asset.name == 'USD'" class="">
                  <b>{{ asset.quantity }} USD</b>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
    <div class="row row-cards">
      <div class="row text-center">
        <h5>No Assets in your Portfolio:</h5>
      </div>
      <div class="row text-center">
        <router-link :to="{ name: 'instruments'}">
          <button type="submit" class="btn btn-confirm btn-login">
            Trade Assets
          </button>
        </router-link>
      </div>
    </div>
  </div>
  <div v-else class="dashboard-cards">
    <div class="row row-error">
      <p v-if="error" class="muted error-message">{{ error }}</p>
    </div>
    <div class="row row-cards">
      <div class="col-md-8">
        <div class="row plain element">
          <div class="col-xs-5 col-sm-5 col-md-5 col-lg-4 plain-element">
            <table class="table table-transaction">
              <tbody>
                <tr>
                  <td class="cash-cell">Portfolio Value:</td>
                  <td >
                    <b>{{ formatPrice(this.totalValue) }} USD</b>
                  </td>
                </tr>
                <tr class="transparent">
                  <td class="cash-cell">Cash on Hand:</td>
                  <td v-for="asset in assets" v-if="asset.name == 'USD'" class="">
                    <b>{{ formatPrice(asset.quantity) }} USD</b>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="col-md-4 col-lg-5 plain-element"></div>
          <div class="col-md-3 col-lg-3 plain-element">
            <div class="search-wrapper">
              <label> Search Asset:</label>
              <input type="text" v-model="search"/>
            </div>
          </div>
        </div>
        <div class="row plain element">
          <table id="instrumentTable">
            <thead>
            <tr>
              <th onclick="sortTable(0)">Instrument</th>
              <th onclick="sortTable(1)" class="text-center">Symbol</th>
              <th onclick="sortTable(2)" class="text-center">Category</th>
              <th class="text-center">Quantity</th>
              <th class="text-center">Price (USD)</th>
              <th class="text-center">Total (USD)</th>
              <th colspan="2" class="text-center">Transaction</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="asset in filteredList" v-if="asset.name != 'USD'" :key="asset.pk">
              <td>{{ asset.name }}</td>
              <td class="text-center">{{ asset.symbol }}</td>
              <td class="text-center">{{ asset.category }}</td>
              <td class="text-center">{{ asset.quantity }}</td>
              <td class="text-center">{{ formatPrice(asset.price) }}</td>
              <td class="text-center">{{ formatPrice(asset.value) }}</td>
              <td class="text-center">
                <router-link :to="{ name: 'buy-instrument', params: {slug: asset.instrument_slug} }">
                  <button class="btn btn-transaction btn-transaction-small">Buy</button>
                </router-link>
              </td>
              <td class="text-center">
                <router-link :to="{ name: 'sell-instrument', params: { slug: asset.instrument_slug} }">
                  <button class="btn btn-transaction btn-transaction-small">Sell</button>
                </router-link>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="col-md-4">
        <div class="small">
          <pie-chart :options="options" :chart-data="datacollection"></pie-chart>
        </div>
      </div>
    </div>
  </div>
</div>

</template>

<script>
import { apiService } from "@/common/api.service.js";
import PieChart from '@/common/PieChart.js';
import RowHeaderComponent from "@/components/RowHeader.vue";


export default {
  name: "AssetManager",
  components: {
    RowHeaderComponent,
    PieChart,

  },
  data() {
    return {
      search: '',
      assets: [],
      portfolioComposition: [],
      datacollection: {},
      totalValue: 0,
      options: {},
      requestUser: null,
      error: null,
    }
  },
  mounted () {
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
    getAssetData() {
//      Check if user is logged in
      if (this.requestUser !== "undefined") {
        let endpoint = "/portfolio/asset-manager/";
        apiService(endpoint)
          .then(data => {
          if (data) {
            this.assets.push(...data);
//          Map-reduce to category-quantity
            this.portfolioComposition = data.reduce(function (r, o) {
                            (r[o.category])? r[o.category] += Math.floor(o.value) : r[o.category] = Math.floor(o.value);
                            return r;
                          }, {});
            window.localStorage.setItem("portfolio", JSON.stringify(this.portfolioComposition));
//          Send data to the chart
            this.fillData();
//          Get the total value of a portfolio
            this.totalValue = (Object.values(this.portfolioComposition)).reduce((a, b) => a + b, 0)
          } else {
              this.error = "Something went wrong. We couldn't proceed with your request"
            }
          })
      } else {
        console.log("User has to login first.")
      }
    },
    fillData () {
      var dataset = JSON.parse(window.localStorage.getItem("portfolio"))
//      Get Keys
      var dataLabels = Object.keys(dataset)
//      Get Values
      var dataValues = Object.values(dataset)
      this.options = {
//      Tootips options
        tooltips: {
          enabled: true,
          callbacks: {
            label: function(tooltipItem,data) {
              return data['datasets'][0]['data'][tooltipItem['index']] + " USD";
            },
          }
        }
      }
      this.datacollection = {
        hoverBackgroundColor: "red",
        hoverBorderWidth: 10,
        labels: dataLabels,
        datasets: [
          {
            label: 'Portfolio',
            backgroundColor: ["#72ad56", "#914881" , "#a8be5f", "#ba5d6f"],
            data: dataValues
          }
        ]
      }
    },
//  US price format
    formatPrice(value) {
      let val = (value/1).toFixed(2).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    },
  },
  computed: {
//  Search functionality
    filteredList() {
      return this.assets.filter(asset => {
        return asset.symbol.toLowerCase().includes(this.search.toLowerCase()) ||
                asset.name.toLowerCase().includes(this.search.toLowerCase()) ||
                asset.category.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.setRequestUser();
    this.getAssetData();
    this.setPageTitle("My Assets");
  }
}
</script>
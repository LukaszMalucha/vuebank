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
    <div class="row row-cards"></div>
    <div class="row row-cards">
    <div class="row text-center">
          <h5>You have to Login first:</h5>
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
  <div v-if="assets.length < 2" class="dashboard-cards">
    <div class="row row-cards"></div>
    <div class="row row-cards">
      <div class="row text-center">
        <h5>No Assets in your Portfolio yet:</h5>
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
    <div class="row row-cards">
      <div class="col-md-7 no-padding">
        <div class="row plain element">
          <div class="search-wrapper">
            <label> Search:</label>
            <input type="text" v-model="search"/>
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
              <th colspan="2" class="text-center">Transaction</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="asset in filteredList" v-if="asset.name != 'USD'" :key="asset.pk">
              <td>{{ asset.name }}</td>
              <td class="text-center">{{ asset.symbol }}</td>
              <td class="text-center">{{ asset.category }}</td>
              <td class="text-center">{{ asset.quantity }}</td>
              <td class="text-center">{{ asset.price }}</td>
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
        <div class="row plain element">
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
      </div>
      <div class="col-md-1"></div>
      <div class="col-md-4 plain-element">
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
import RowHeaderComponent from "@/components/RowHeader.vue";
import PieChart from '@/PieChart.js'




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
      requestUser: null,
    }
  },
  mounted () {
    this.fillData()
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("email");
    },
    getAssetData() {
      let endpoint = "/portfolio/asset-manager/";
      apiService(endpoint)
        .then(data => {
          this.assets.push(...data);
          this.setPageTitle("My Assets");
        })
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
  },
  computed: {
    filteredList() {
      return this.assets.filter(asset => {
        return asset.symbol.toLowerCase().includes(this.search.toLowerCase()) ||
                asset.name.toLowerCase().includes(this.search.toLowerCase()) ||
                asset.category.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.getAssetData()
    this.setRequestUser()

  }
}
</script>
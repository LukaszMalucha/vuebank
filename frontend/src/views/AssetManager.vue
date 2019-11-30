<template>
<div id="page-index">
  <RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
    <h4>Portfolio - {{ this.requestUser }}</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div class="dashboard-cards">
      <div class="container text-center container-welcome">
        <div class="search-wrapper">
           <label>Search:</label>
           <input type="text" v-model="search"/>
        </div>
    <div class="container text-center container-welcome">
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
          <tr v-for="asset in filteredList" :key="asset.pk">
            <td>{{ asset.name }}</td>
            <td  class="text-center">{{ asset.symbol }}</td>
            <td class="text-center">{{ asset.category }}</td>
            <td class="text-center">{{ asset.price }}</td>
            <td class="text-center">
            <router-link :to="{ name: 'buy-instrument', params: { slug: asset.slug} }">
                <button class="btn btn-transaction">Buy</button>
            </router-link>
            </td>
            <td class="text-center">
            <router-link :to="{ name: 'sell-instrument', params: { slug: asset.slug} }">
                <button class="btn btn-transaction">Sell</button>
            </router-link>
            </td>
          </tr>
       </tbody>
      </table>
    </div>
  </div>
</div>
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import RowHeaderComponent from "@/components/RowHeader.vue";

export default {
  name: "AssetManager",
  components: {
    RowHeaderComponent,
  },
  data() {
    return {
      search: '',
      assets: [],
      requestUser: null,
    }
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
          this.assets.push(...data)
          this.setPageTitle("My Assets");
        })
    }
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
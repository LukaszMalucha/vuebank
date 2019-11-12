<template>
 <div class="wrapper">
    <div id="page-index">
        <div class="dashboard-cards">
            <div class="container text-center container-welcome">
                <div class="row">
                    <h3>My Portfolio</h3>
                </div>
                <br>
                <div class="row">
                    <div v-for="asset in assets" :key="asset.pk" class="col-md-4 text-center">
                        <div class="card card-asset">
                            <div class="card-header">
                                <div class="row plain-element">
                                    <div class="col-md-4 plain-element">
                                        <div class="card-image">
                                            <img alt="Currency" src="../assets/currency.png" class="img responsive"/>
                                        </div>
                                    </div>
                                    <div class="col-md-8 plain-element">
                                        <div class="card-title text-left">
                                            <h5>{{ asset.name }}</h5>
                                            <table class="table table-company">
                                                <tbody>
                                                <tr>
                                                    <td>Category:</td>
                                                    <td><b>{{ asset.category }}</b></td>
                                                </tr>
                                                <tr>
                                                    <td>Ticker:</td>
                                                    <td><b>{{ asset.symbol }}</b></td>
                                                </tr>
                                                <tr>
                                                    <td>Current Price:</td>
                                                    <td><b>{{ asset.price }} USD</b></td>
                                                </tr>
                                                <tr>
                                                    <td>Quantity:</td>
                                                    <td><b>{{ asset.quantity }}</b></td>
                                                </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card-content">
                                <b class="asset-website">
                                    <router-link :to="{ name: 'asset', params: { slug: asset.slug} }">
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
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
  name: "AssetManager",
  data() {
    return {
      assets: {}
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getAssetData() {
      let endpoint = `/portfolio/asset-manager/`;
      apiService(endpoint)
        .then(data => {
          this.assets = data;
          this.setPageTitle("My Assets")
        })
    }
  },
  created() {
    this.getAssetData();
  }
}

</script>
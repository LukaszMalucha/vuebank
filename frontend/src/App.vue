<template>
    <div id="app">
      <router-view/>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
import RowHeaderComponent from "@/components/RowHeader.vue";
export default {
    name: "App",
    components: {
        RowHeaderComponent,
    },
    methods: {
      async setUserInfo() {
        const dataUser = await apiService("/portfolio/user/");
        const requestUser = dataUser["email"];
        window.localStorage.setItem("email", requestUser);
      },
      //    Prepare data for chart
      async setPortfolioData() {
  //    wait for data
          const dataPortfolio = await apiService("/portfolio/asset-manager/");
  //    mapper function for array -> summing values for asset categories
          const requestTotals = dataPortfolio.reduce(function (r, o) {
                          (r[o.category])? r[o.category] += Math.floor(o.value) : r[o.category] = Math.floor(o.value);
                          return r;
                        }, {});
  //    push to local storage
          window.localStorage.setItem("portfolio", JSON.stringify(requestTotals));
          console.log(requestTotals);
      },
    },

    created() {
        this.setUserInfo();
        this.setPortfolioData();
    }
}
</script>


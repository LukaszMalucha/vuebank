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

//  IF ELSE TUTAJ !!!!!!!!!!!!!!!!!!!!!!!!!!  I ERRORY I JEDNOSTKĘ USD
        const requestUser = dataUser["email"];
        window.localStorage.setItem("email", requestUser);
      }
    },

    created() {
        this.setUserInfo();
    }
}
</script>


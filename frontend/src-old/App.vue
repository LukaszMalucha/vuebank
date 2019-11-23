<template>

      <div id="app">
        <NavbarComponent />
        <NavbarMobileComponent />
        <FooterComponent />
        <router-view/>
      </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
import NavbarComponent from "@/components/Navbar.vue";
import NavbarMobileComponent from "@/components/NavbarMobile.vue";
import FooterComponent from "@/components/Footer.vue";
export default {
    name: "App",
    components: {
        NavbarComponent,
        NavbarMobileComponent,
        FooterComponent
    },
    methods: {
      async setUserInfo() {
        const dataUser = await apiService("/portfolio/user/");
        const requestUser = dataUser["email"];
        window.localStorage.setItem("email", requestUser);
      }
    },
    created() {
        this.setUserInfo();

    }
}
</script>


<template>

      <div id="app">
        <NavbarComponent />
        <NavbarMobileComponent />
        <FooterComponent />
        <router-view/>
      </div>
</template>

<script>
import NavbarComponent from "@/components/Navbar.vue";
import NavbarMobileComponent from "@/components/NavbarMobile.vue";
import FooterComponent from "@/components/Footer.vue";
export default {
    name: "App",
    components: {
        NavbarComponent,
        NavbarMobileComponent,
        FooterComponent
    }
}
</script>


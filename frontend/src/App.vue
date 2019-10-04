<template>

      <div id="app">
        <NavbarComponent />
        <NavbarMobileComponent />
        <FooterComponent />
        <router-view/>
      </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue";
import NavbarMobileComponent from "./components/NavbarMobile.vue";
import FooterComponent from "./components/Footer.vue";
export default {
    name: "App",
    components: {
        NavbarComponent,
        NavbarMobileComponent,
        FooterComponent
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

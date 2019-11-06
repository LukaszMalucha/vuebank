import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Instruments from "./views/Instruments.vue";
import Instrument from "./views/Instrument.vue";

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/instruments/",
      name: "instruments",
      component: Instruments
    },
    {
      path: "/instrument/:slug",
      name: "instrument",
      component: Instrument,
      props: true
    },

  ]
})

import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import Instruments from "./views/Instruments.vue";
import BuyInstrument from "./views/BuyInstrument.vue";
import SellInstrument from "./views/SellInstrument.vue"
import AssetManager from "./views/AssetManager.vue";
import CashTransfer from "./views/CashTransfer.vue";

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
      path: "/instruments",
      name: "instruments",
      component: Instruments
    },
    {
      path: "/instrument/:slug/buy",
      name: "buy-instrument",
      component: BuyInstrument,
      props: true
    },
    {
      path: "/instrument/:slug/sell",
      name: "sell-instrument",
      component: SellInstrument,
      props: true
    },
    {
      path: "/asset-manager",
      name: "asset-manager",
      component: AssetManager,
    },
    {
      path: "/cash-transfer",
      name: "cash-transfer",
      component: CashTransfer,
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})

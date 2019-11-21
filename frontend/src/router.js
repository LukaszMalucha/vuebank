import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Instruments from "./views/Instruments.vue";
import BuyInstrument from "./views/BuyInstrument.vue";
import SellInstrument from "./views/SellInstrument.vue"
import InstrumentEditor from "./views/InstrumentEditor.vue";
import AssetManager from "./views/AssetManager.vue";
import CashBalance from "./views/CashBalance.vue";
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
      path: "/add-instrument",
      name: "instrument-editor",
      component: InstrumentEditor,
    },
    {
      path: "/asset-manager",
      name: "asset-manager",
      component: AssetManager,
    },
    {
      path: "/cash-balance",
      name: "cash-balance",
      component: CashBalance,
    },
    {
      path: "/cash-transfer",
      name: "cash-transfer",
      component: CashTransfer,
    },
  ]
})

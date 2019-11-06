import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Instruments from './views/Instruments.vue';

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
        path: '/instruments/',
        name: 'instruments',
        component: Instruments
    }
  ]
})

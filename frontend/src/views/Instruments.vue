<template>
<div id="page-index">
  <RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
    <h4>Available Instruments</h4>
    </div>
    <div class="col-md-4 no-padding">
    </div>
  </div>
  <div class="dashboard-cards">
    <div class="container text-center container-welcome">
        <div class="search-wrapper">
           <input type="text" v-model="search" placeholder="Search title.."/>
          <label>Search title:</label>
        </div>
      <table>
        <thead>
        <tr>
          <th>Instrument</th>
          <th>Symbol</th>
          <th>Category</th>
          <th>Price</th>
          <th>Buy</th>
          <th>Sell</th>
        </tr>
        </thead>
        <tbody>
          <tr v-for="instrument in filteredList" :key="instrument.pk">
            <td>{{ instrument.name }}</td>
            <td>{{ instrument.symbol }}</td>
            <td>{{ instrument.category }}</td>
            <td>{{ instrument.price }}</td>
            <td>Buy</td>
            <td>Sell</td>
          </tr>
       </tbody>
      </table>
    </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js"
import RowHeaderComponent from "@/components/RowHeader.vue";


export default {
  name: 'Instruments',
  components: {
    RowHeaderComponent,
  },
  data() {
    return {
        search: '',
        instruments: [],
    }
  },
  methods: {
    getInstruments() {
    let endpoint = "/portfolio/instruments/";
    apiService(endpoint)
      .then( data => {
          this.instruments.push(...data.results)
     })
    }
  },
  computed: {
    filteredList() {
      return this.instruments.filter(instrument => {
        return instrument.name.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  },
  created() {
    this.getInstruments();
    document.title = "Instruments";
  }
}
</script>
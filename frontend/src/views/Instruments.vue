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
           <label>Search:</label>
           <input type="text" v-model="search"/>
        </div>
      <table id="instrumentTable">
        <thead>
        <tr>
          <th onclick="sortTable(0)">Instrument</th>
          <th onclick="sortTable(1)" class="text-center">Symbol</th>
          <th onclick="sortTable(2)" class="text-center">Category</th>
          <th class="text-center">Price</th>
          <th class="text-center">Buy</th>
          <th class="text-center">Sell</th>
        </tr>
        </thead>
        <tbody>
          <tr v-for="instrument in filteredList" :key="instrument.pk">
            <td>{{ instrument.name }}</td>
            <td  class="text-center">{{ instrument.symbol }}</td>
            <td class="text-center">{{ instrument.category }}</td>
            <td class="text-center">{{ instrument.price }}</td>
            <td class="text-center">Buy</td>
            <td class="text-center">Sell</td>
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
    },
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
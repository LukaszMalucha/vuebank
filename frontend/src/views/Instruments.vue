<template>
  <div class="wrapper">
      <div id="page-index">
        <div class="dashboard-cards">
            <div class="container text-center container-welcome">
                    <div class="row">
                        <h3>Available Instruments</h3>
                    </div>
                    <br>
                    <div class="row">

                    </div>
            </div>
        </div>
      </div>
  </div>
</template>


<script>
import { apiService } from "../common/api.service.js"

export default {
    name: 'instruments',
    data() {
        return {
            instruments: []
        }
    },
    methods: {
        getInstruments() {
        let endpoint = "portfolio/instruments/";
        apiService(endpoint)
            .then( data => {
                this.instruments.push(...data.results)
           })
        }
    },
    created() {
        this.getInstruments()
        console.log(this.instruments)
    }
}
</script>
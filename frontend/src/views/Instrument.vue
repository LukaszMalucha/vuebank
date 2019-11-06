<template>
  <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="container text-center container-welcome">
          <div class="row">
            <h3>{{ instrument.name }}</h3>
          </div>
          <br>
          <div class="row">
                <p>{{ instrument.symbol }}</p>
                <p>{{ instrument.category }}</p>
                <p>{{ instrument.price }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { apiService } from "../common/api.service.js"

export default {
  name: 'Instrument',
  props: {
    slug: {
      type: String,
      required: true
    }
  }
}

</script>
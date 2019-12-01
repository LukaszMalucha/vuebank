<template>
<div id="page-index">
  <RowHeaderComponent/>
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>{{ message }}</h4>
    </div>
    <div class="col-md-4 no-padding">
    <visualisation></visualisation>
    </div>
  </div>
</div>
</template>


<script>
import RowHeaderComponent from "@/components/RowHeader.vue";
import Visualisation from '@/components/Visualisation.vue';

export default {
  name: "NotFound",
  components: {
    RowHeaderComponent,
    Visualisation,
  },
  data() {
    return {
      message: "404 - Page Not Found"
    }
  }
}
</script>
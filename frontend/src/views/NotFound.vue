<template>
  <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="row">
          <div class="col-md-4 plain-element"></div>
          <div class="col-md-4 plain-element">
            <div class="card card-instrument">
              <div class="card-content">
                  <h4>  {{ message }} </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>
export default {
  name: "NotFound",
  data() {
    return {
      message: "404 - Page Not Found"
    }
  }
}
</script>
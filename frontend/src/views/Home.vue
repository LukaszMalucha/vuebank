<template>
  <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="container text-center container-welcome">
          <div class="row">
            <h3>Welcome to the RESTBank</h3>
          </div>
          <br>
          <div class="row">
            <div class="col-md-3 text-center">
                <button onclick="window.location='/user/login'" class="btn route"><b>Login</b></button>
            </div>
            <div class="col-md-3 text-center">
                <button onclick="window.location='/user/register'" class="btn route"><b>Register</b>
                </button>
            </div>
            <div class="col-md-3 text-center">
                <button class="btn route"><b>User Profile</b>
                </button>
            </div>
            <div class="col-md-3 text-center">
                <button class="btn route"><b>Instruments</b></button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
  name: 'home',
  created() {
    document.title = "VueBank";
  }
};

</script>

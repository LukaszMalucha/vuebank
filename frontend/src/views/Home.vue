<template>
  <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="container text-center container-welcome">
          <div class="row">
            <h4>RESTBank Asset Manager</h4>
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
            <router-link
            :to="{name: 'asset-manager'}">
                <button class="btn route"><b>My Assets</b>
                </button>
            </router-link>
            </div>
            <div class="col-md-3 text-center">
                <button onclick="window.location='/instruments'" class="btn route"><b>Instruments</b></button>
            </div>
          </div>
          <div class="row">
            <div class="col-md-3 text-center">
            <router-link
            :to="{name: 'cash-balance'}">
                <button class="btn route"><b>Cash Balance</b>
                </button>
            </router-link>
            </div>
            <div class="col-md-3 text-center">
            <router-link
            :to="{name: 'buy'}">
                <button class="btn route"><b>Buy</b>
                </button>
            </router-link>
            </div>
            <div class="col-md-3 text-center">
            <router-link
            :to="{name: 'asset-manager'}">
                <button class="btn route"><b>Sell</b>
                </button>
            </router-link>
            </div>
            <div class="col-md-3 text-center">
                <button onclick="window.location='/instruments'" class="btn route"><b>User Profile</b></button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'home',
  created() {
    document.title = "VueBank";
  }
};

</script>

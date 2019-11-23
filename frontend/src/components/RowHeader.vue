<template>
  <div class="row header">
      <div class="row top-menu">
          <router-link
            :to="{name: 'home'}"
            class="navbar-brand waves-effect waves-dark">
            <img alt="RestBank" src="../assets/restbank.png" class="img responsive restbank" alt="RESTBank logo" />
          </router-link>
          <ul>
              <li><a href="">My Assets</a></li>
              <li><a href="">Trade Assets</a></li>
              <li><a target="_blank" href="">My Profile</a></li>
              <li><a target="_blank" href="http://www.minerstartup.com/">Blockchain Platform</a></li>
              <li><a target="_blank" href="http://www.quantproperties.com/">Property Value Estimator</a></li>
              <li><a href="">Contact</a></li>
          </ul>
      </div>
  </div>
</template>

<script>
export default {
    name: "RowHeaderComponent"
}

</script>
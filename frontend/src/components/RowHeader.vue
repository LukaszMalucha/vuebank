<template>
  <div class="row header">
      <div class="row top-menu">
          <router-link :to="{name: 'home'}">
            <img src="../assets/restbank.png" class="img responsive restbank" alt="RESTBank logo" />
          </router-link>
          <ul>
              <li><router-link :to="{ name: 'asset-manager'}">My Asset Manager</router-link></li>
              <li><router-link :to="{ name: 'instruments'}">Trade Assets</router-link></li>
              <li><router-link :to="{ name: 'cash-balance'}">Cash Transfer</router-link></li>
              <li class="link-advert"><a target="_blank" href="http://www.minerstartup.com/">Blockchain Platform</a></li>
              <li class="link-advert"><a target="_blank" href="http://www.quantproperties.com/">Property Value Estimator</a></li>
              <li class="link-advert"><a target="_blank" href="http://www.thompsonsampling.com/">Ad Campaign</a></li>
              <li><a target="_blank" href="https://github.com/LukaszMalucha">Contact</a></li>
          </ul>
      </div>
  </div>
</template>

<script>
export default {
    name: "RowHeaderComponent"
}

</script>
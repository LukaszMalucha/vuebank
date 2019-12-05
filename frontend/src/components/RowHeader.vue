<template>
  <div class="row header">
      <div class="row top-menu">
        <div class="col-sm-2 col-md-2 plain-element col-logo">
            <router-link :to="{name: 'home'}">
              <img src="../assets/restbank.png" class="img responsive restbank" alt="RESTBank logo" />
            </router-link>
        </div>
        <div class="col-sm-12 col-md-10 plain-element">
            <ul>
                <li><router-link :to="{ name: 'asset-manager'}">My Asset Manager</router-link></li>
                <li><router-link :to="{ name: 'instruments'}">Trade Assets</router-link></li>
                <li><router-link :to="{ name: 'cash-balance'}">Cash Transfer</router-link></li>
                <li><router-link :to="{ name: 'transaction-history'}">Transaction History</router-link></li>
                <li class="link-advert"><a target="_blank" href="http://www.quantproperties.com/">Property Value Estimator</a></li>
                <li class="link-advert"><a target="_blank" href="http://www.thompsonsampling.com/">Ad Campaign</a></li>
                <li class="link-advert"><a target="_blank" href="https://github.com/LukaszMalucha">Contact</a></li>
            </ul>
        </div>
      </div>
  </div>
</template>

<script>
export default {
    name: "RowHeaderComponent"
}

</script>
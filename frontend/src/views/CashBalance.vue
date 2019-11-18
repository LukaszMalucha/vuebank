<template>
  <div class="wrapper">
    <div id="page-index">
      <div class="dashboard-cards">
        <div class="row">
          <div class="col-md-4 plain-element"></div>
          <div class="col-md-4 plain-element">
            <div class="card card-instrument">
              <div class="card-header">
                <div class="row plain-element">
                  <div class="col-md-4 plain-element">
                    <div class="card-image">
                      <img alt="Currency" src="../assets/currency.png" class="img responsive"/>
                    </div>
                  </div>
                <div class="col-md-8 plain-element">
                  <div class="card-title text-left">
                    <h5>Cash Balance</h5>
                      <table class="table table-company">
                        <tbody>
                          <tr>
                            <td>Category:</td>
                            <td><b>{{ cash.category }}</b></td>
                          </tr>
                          <tr>
                            <td>Ticker:</td>
                            <td><b>{{ cash.symbol }}</b></td>
                          </tr>
                          <tr>
                            <td>Current Amount:</td>
                            <td><b>{{ cash.quantity }}</b></td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            <div class="card-content">
              <b class="instrument-website">

                    Top Up

              </b>
            </div>
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
  name: 'CashBalance',
  data() {
    return {
      cash: {}
    }
  },
  methods: {
    getCashData() {
      let endpoint = '/portfolio/cash-balance/';
      apiService(endpoint)
        .then(data => {
          this.cash = data['results'][0];

        })
    }

  },
  created() {
    this.getCashData();
    document.title = "Cash Balance";
  }
}

</script>

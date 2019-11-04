<template>
  <div class="wrapper">
<div class="container text-center container-welcome">
        <div class="row">
            <h3>Welcome to the RESTBank API</h3>
        </div>
        <br>
        <div class="row">
            <div class="col-md-3 text-center">
                <button class="btn route"><b>Register</b></button>
            </div>
            <div class="col-md-3 text-center">
                <button class="btn route"><b>Authenticate</b>
                </button>
            </div>
            <div class="col-md-3 text-center">
                <button class="btn route"><b>User Details</b>
                </button>
            </div>
            <div class="col-md-3 text-center">
                <button class="btn route"><b>My
                    Portfolio</b></button>
            </div>
        </div>
        <br>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service"

export default {
  name: 'home',
  data() {
    return {
        questions: []
    }

  },
  methods: {
    getQuestions() {
        let endpoint = "api/questions/";
        apiService(endpoint)
        .then(data => {
            this.questions.push(...data.results);
        })
    }
  }
}
</script>

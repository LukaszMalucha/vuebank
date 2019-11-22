<template>
  <div class="dashboard-cards">
    <div class="row row-cards">
        <div class="col-md-4 no-padding">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="../assets/portfolio.jpg" class="img responsive" alt="portfolio">
                </div>
                <div class="card-content">
                    <span class="card-title">Manage Portfolio</span>
                    <p>Manage Investment Protfolio with REST API</p>
                </div>
                <button onclick="#" class="btn btn-enter"><span>Continue <i class="far fa-arrow-alt-circle-right"></i></span></button>
            </div>
        </div>
        <div class="col-md-4 no-padding">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="../assets/advert.jpg" class="img responsive" alt="thompson campaign">
                </div>
                <div class="card-content">
                    <span class="card-title">Advertising with AI</span>
                    <p>Build an Advert with Thompson Sampling</p>
                </div>
                <button onclick="#" type="submit" class="btn btn-enter"><span>Continue <i class="far fa-arrow-alt-circle-right"></i></span></button>
            </div>
        </div>
        <div class="col-md-4 no-padding">
            <div class="card menu-card">
                <div class="card-image">
                    <img src="../assets/blockchain.jpg" class="img responsive" alt="blockchain">
                </div>
                <div class="card-content">
                    <span class="card-title">Blockchain Platform</span>
                    <p>Basic Blockchain concepts explained</p>
                </div>
                <button onclick="#" type="submit" class="btn btn-enter"><span>Continue <i class="far fa-arrow-alt-circle-right"></i></span></button>
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

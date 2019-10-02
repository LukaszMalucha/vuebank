<template>
<nav class="navbar navbar-default top-navbar" role="navigation">
    <div class="navbar-header">
        <a class="navbar-brand waves-effect waves-dark" href=""><strong> Welcome to
            <b>RESTBank</b></strong></a>
    </div>
    <ul class="nav navbar-top-links navbar-right">
        <li><a class="nav-link" href=""><i class="fas fa-terminal"></i><b> Code Blog</b></a>
        </li>
        <li><a class="nav-link" target="_blank" href="https://github.com/LukaszMalucha/"><i
                class="fab fa-github"></i> <b> GitHub</b></a></li>
        <li><a class='dropdown-trigger nav-link' href='#' data-target='dropdown1' id="user_dropdown"><i
                class="fas fa-caret-down"></i><b>User </b></a></li>
        <li><a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons" id="trigger">menu</i></a>
        </li>
    </ul>
</nav>
</template>


<script>
export default {
    name: "NavbarComponent"

}
</script>

<style>


</style>
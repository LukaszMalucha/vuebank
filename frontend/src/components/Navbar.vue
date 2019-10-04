<template>
<nav class="navbar navbar-default top-navbar" role="navigation">
    <div class="navbar-header">
        <router-link
            :to="{name: 'home'}"
            class="navbar-brand waves-effect waves-dark"
        ><strong> Welcome to <b>RESTBank</b></strong>
        </router-link>
    </div>
    <ul class="nav navbar-top-links navbar-right">
        <li><a class='dropdown-trigger nav-link' href='#' data-target='dropdown-user' id="user_dropdown"><i
                class="fas fa-caret-down"></i><b>
            Login/Register
        </b></a></li>
        <li><a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons"
                                                                             id="trigger">menu</i></a>
        </li>
    </ul>

    <ul id="dropdown-user" class="dropdown-content">
        <li><a href="/user/logout"><i class="fas fa-sign-out-alt"></i> Log Out</a></li>
        <li><a href="/user/login"><i class="fa fa-user fa-fw"></i> Log In</a></li>
        <li><a href="/user/register"><i class="fas fa-tasks"></i> Register</a></li>
    </ul>

</nav>

</template>


<script>
export default {
    name: "NavbarComponent"
}

</script>



<template>
  <div id="page-index">
  <div class="home">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
}
</script>

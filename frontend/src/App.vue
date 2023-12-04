<template>
  <div class="wrapper">
    <Navbar />

    <div class="container">
      <router-view></router-view>
    </div>
    <div class="push"></div>

  </div>
  <div class="page-footer">
    <Footer />
  </div>
</template>

<script>

import Navbar from './components/NavbarComponent.vue'
import Footer from './components/FooterComponent.vue'
export default {
  name: 'App',
  components: {
    Navbar,
    Footer
  }
}
</script>

<style>
.wrapper {
  min-height: 100vh;
  margin-bottom: -100px;
}

</style>
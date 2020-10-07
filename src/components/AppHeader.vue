<template>
  <header id="header" class="container">
    <div class="logo">
      <router-link to="/">
        <img src="@/static/img/SVG/logo.svg" alt="ez-logo">
      </router-link>
    </div>
    <nav>
      <router-link to="/" class="active">Home</router-link>
      <span>|</span>
      <router-link to="/">Slang</router-link>
      <span>|</span>
      <router-link to="/">About</router-link>
    </nav>
    <div class="search">
      <input type="text" placeholder="Search">
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
}
</script>
<template>
  <div id="default">
    <AppHeader />
    <main class="container">
      <slot />
    </main>
  </div>
</template>

<script>
import AppHeader from '@/components/AppHeader'

export default {
  name: 'default',
  components: { AppHeader }
}
</script>

<style>
</style>
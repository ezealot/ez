<template>
  <div id="app">
    <Default>
      <router-view></router-view>
    </Default>
  </div>
</template>

<script>
import Default from '@/layouts/Default'

export default {
  name: 'App',
  components: {
    Default
  }
}
</script>

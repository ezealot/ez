<template>
  <div id="home">
    <div id="home-main-content">
      <div>
        <h2>Popular Games</h2>
        <div id="games">
          <div class="template"></div>
          <div class="template"></div>
          <div class="template"></div>
        </div>
      </div>
      <div id="slang">
        <div class="template"></div>
        <div class="template"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home' 
}
</script>

<style>
  #games {
    height: 200px;
    display: flex;
    gap: 20px;
    margin-top: 20px;
  }
  #slang {
    height: 280px;
    display: flex;
    gap: 20px;
  }
  .template {
    border-radius: 8px;
    height: 100%;
    flex: 1;
    background-color: rgb(216, 216, 216);
    box-shadow: 0px 1px 5px 0 rgba(0, 0, 0, 0.1);
  }
</style>
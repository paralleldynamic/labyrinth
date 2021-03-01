<template>
  <div class="card">
    <div class="card-image">
      <slot name="card-image" />
    </div>
    <div class="card-title">
      <slot name="card-title" />
    </div>
    <div class="card-description">
      <slot name="card-description" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContentCard',
};
</script>

<style>
.card {
  box-shadow: 0 5px 10px #191919;
  border-radius: 3px;
  box-sizing: border-box;
  max-width: 25vw;
  padding: 0.25em;
  margin: 0.5em;
  background-color: #FBFBFF;
}

.card-title > * {
  text-align: center;
  font-size: medium;
}

.card-image > * {
  border-radius: 3px;
  width: 85%;
  display: block;
  padding: 3px;
  margin: 0.5em;
  margin-left: auto;
  margin-right: auto;
}

.card-description > * {
  text-align: justify;
  font-size: smaller;
  margin: 0.5em;
}
</style>

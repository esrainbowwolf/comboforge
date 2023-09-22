<template>
  <div class="Account">
    <h1> {{login}}</h1>
    <button></button>
  </div>
</template>
<script setup>
import {ref} from 'vue'

const login=ref('Welcome to the log in page')


</script>

<style lang="scss" scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #8702a1;
}
.Account {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  width:fit-content;
  margin:auto
}
</style>
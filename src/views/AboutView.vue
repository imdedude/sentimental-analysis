<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h2>{{ message }}</h2>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import * as shop from '../../shop.ts';

export default {
  setup() {
    const message = ref('');

    const fetchMessage = () => {
      shop
        .getSth()
        .then((resp) => {
          message.value = resp
        })
    };

    onMounted(() => {
      fetchMessage()
    })

    return { message };
  }
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

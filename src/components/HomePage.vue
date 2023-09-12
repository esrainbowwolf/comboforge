<template>
  <div class="hello">
    <h1>Welcome to Comboforge!</h1>

    <h1>{{ msg }}</h1>
    <p>
      This is a website for the card game keyforge to accumulate combos and get
      ratings from the community to find the strongest combos!
    </p>
    <h3>Other Sites</h3>
    <ul>
      <li>
        <a href="https://decksofkeyforge.com/" target="_blank" rel="noopener"
          >Decks of Keyforge</a
        >
      </li>
      <li>
        <a
          href="https://archonarcana.com/Main_Page"
          target="_blank"
          rel="noopener"
          >Archon Arcana</a
        >
      </li>
      <li>
        <a href="https://thecrucible.online/" target="_blank" rel="noopener"
          >The Crucible</a
        >
      </li>
      <li>
        <a href="https://keyforging.com/" target="_blank" rel="noopener"
          >Keyforge Website</a
        >
      </li>
      <li>
        <a
          href="https://twitter.com/GhostGalaxyGam1"
          target="_blank"
          rel="noopener"
          >Ghost Galaxy Twitter</a
        >
      </li>
    </ul>
    <h3>My info</h3>
    <ul>
      <li>
        <a
          href="https://github.com/esrainbowwolf?tab=repositories"
          target="_blank"
          rel="noopener"
          >Github</a
        >
      </li>
      <!-- <li>
        <a href="https://vuex.vuejs.org" target="_blank" rel="noopener">Twitter (X)</a>
      </li> -->
      <li>
        <a>My Discord: ESRainbowWolf</a>
      </li>
    </ul>
  </div>
</template>
  
  <script>
export default {
  name: "WelcomePage",
  props: {
    msg: String,
  },
};
</script>


  <!-- Add "scoped" attribute to limit CSS to this component only -->
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
</style>
  
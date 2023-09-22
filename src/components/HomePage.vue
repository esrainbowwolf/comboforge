<template>
  <div class="hello" text-align:center>
    <h1>Welcome to Comboforge!</h1>
      <img src="../assets/ComboCropped.png">
    <p>
      This is a website for the card game keyforge to accumulate combos and get
      ratings from the community to find the strongest combos! This website is quite rough but it will be updated slowly but surely!
    </p>
    <p>
      Please refrain from messaging me personally unless it is something urgent!
      The plan is to add the capability to find combos in decks as well as some form of rating system but I'm not sure.
      I want to also create forums but I'm not quite sure yet.  
    </p>
    <h2>
      How this works!!
    </h2>
    <p>
      <ul>
      <li>You can search cards on this website in the card list tab on the left.</li>
      <li>If you are logged in you can create a combo under a card if it does not already exist.</li>
      <li>If it does exist you can not create the same combo BUT you can add your own rating to said combo and the public score will be an average of all scores given to the combo.</li>
        <li>If you hover over a combo it will show the original rating created by the combo's creator.</li>
    </ul>  
    </p>
      <p>  
        <ul>
      <li>The Rankings tab ranks all combos that exist into an easy to read list.</li>
        <li>You can search by whatever ratings you need.</li>
      </ul>
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
          href="https://drawbetter.cards/about"
          target="_blank"
          rel="noopener"
          >Z Scoring System</a
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
p {
}
.hello {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: fit-content;
  margin: auto;
  gap: 20px
}
</style>
  
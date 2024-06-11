<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card class="mx-auto" color="grey-lighten-3" max-width="400">
          <v-card-text>
            <v-text-field
              :loading="loading"
              class="search-bar"
              density="compact"
              variant="solo"
              label="Search Cards"
              single-line
              hide-details
              append-inner-icon="mdi-magnify"
              @click:append-inner="onClickSearch"
            >
            </v-text-field>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <div class="image-gallery">
      <v-row>
        <v-col>
          <v-dialog v-model="showModal" max-width="600">
            <v-card>
              <v-img :src="selectedImage.src" :alt="selectedImage.alt"></v-img>
            </v-card>
          </v-dialog>

          <v-dialog v-model="showModal" max-width="600">
            <v-card>
              <v-img :src="selectedImage.src" :alt="selectedImage.alt"></v-img>
            </v-card>
          </v-dialog>
          <div
            v-for="(cardName, index) in card_Names"
            :key="index"
            @click="openModal(index)"
          >
            <img
              :src="getImageUrl(cardName.house, cardName.name, 'png')"
              :alt="cardName.name"
            />
          </div>
          <v-dialog v-model="showModal" max-width="600">
            <v-card>
              <v-img :src="selectedImage.src" :alt="selectedImage.alt"></v-img>
            </v-card>
          </v-dialog>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>
  
  <script>
export default {
  data() {
    return {
      card_Names: [
        { house: "Brobnar", name: "12-punch" },
        { house: "Dis", name: "arise" },
        { house: "Ekwidon", name: "trader" },
        // Add more card names as needed
      ],
      house_Names: [
        "Brobnar",
        "Dis",
        "Geistoid",
        "Skyborn",
        "Ekwidon",
        "Logos",
        "Mars",
        "Sanctum",
        "Saurian",
        "Shadows",
        "Star Alliance",
        "Unfathomable",
        "Untamed",
        "Special",
      ],
      showModal: false,
      selectedImage: {},
    };
  },
  methods: {
    openModal(index) {
      const imageUrl = this.getImageUrl(
        this.card_Names[index].house,
        this.card_Names[index].name,
        "png"
      );
      console.log("Image URL:", imageUrl);

      this.selectedImage = {
        src: imageUrl,
        alt: this.card_Names[index],
      };
      this.showModal = true;
    },
    getImageUrl(house, name, ext) {
      const imageUrl = require(`@/assets/Cards/${house}/${name}.${ext}`);
      return imageUrl;
    },
  },
};
</script>
  
  <style scoped>
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
.search-bar {
}
</style>
  
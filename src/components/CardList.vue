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
    <div class="block galleryBlock">
      <v-row>
        <v-col
          v-for="image in images"
          :key="image"
          class="d-flex child-flex"
          cols="2"
          md="4"
          lg="2"
          sm="7"
        >
          <v-img
            :src="image"
            style="cursor: pointer"
            @click="onClickImage"
            margin="auto"
            aspect-ratio="auto"
            cover
            class="bg-grey-lighten-2"
            on
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey-lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import images from "./images.js";

export default {
  data() {
    
    return {
      loaded: false,
      loading: false,
      images: images,
    };
  },
  methods: {
    onClickImage() {
      this.$router.push("/loginPage");
    },
    onClickSearch () {
        this.loading = true

        setTimeout(() => {
          this.loading = false
          this.loaded = true
        }, 2000)
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
  
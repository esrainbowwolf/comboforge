const context = require.context("@/assets/Cards/Brobnar/", false, /\.png$/);
const brobnarImages = context.keys().map(context);

export default brobnarImages;
const context = require.context("@/assets/Cards/Brobnar", false, /\.png$/);
const images = context.keys().map(context);

export default images;
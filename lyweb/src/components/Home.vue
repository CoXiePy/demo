<template>
  <div className="index">
    <Header></Header>
    <Statement></Statement>
    <Footer></Footer>

  </div>

</template>

<script>
import Header from "./common/Header";
import Footer from "./common/Footer";
import Statement from "./common/Statement";
export default {
  name: "Home",
  components: {
    Header,
    Footer,
    Statement,
  },
}
</script>


<style scoped>

</style>

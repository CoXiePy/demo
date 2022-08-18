<template>
  <div>
    <Header></Header>
    <Alipay></Alipay>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "./common/Header";
import Footer from "./common/Footer";
import Alipay from "./techlist/Alipay";
export default {
  name: "Tech",
  components: {
    Header,
    Alipay,
    Footer,

  },
}
</script>
<style scoped>

</style>

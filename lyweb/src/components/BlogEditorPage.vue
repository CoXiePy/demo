<template>
<!--  博客编辑页面-->
  <div className="index">
    <Header></Header>

    <Footer></Footer>
  </div>
</template>

<script>
import Header from "./common/Header";
import Footer from "./common/Footer";

export default {
  name: "BlogEditorPage",
  components: {
    Header,
    Footer,
  },
}
</script>

<style scoped>

</style>

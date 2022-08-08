<template>
  <div className="index">
  <Header></Header>
  <BlogArticles></BlogArticles>
  <Footer></Footer>
  </div>
</template>

<script>
import Header from "./common/Header";
import Footer from "./common/Footer";
import BlogArticles from "./blog/BlogArticles";
export default {
  name: "Blog",
  components: {
    Header,
    BlogArticles,
    Footer,

  },
}
</script>

<style scoped>

</style>

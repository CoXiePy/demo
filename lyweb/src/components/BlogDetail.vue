<template>
  <div className="index">
  <Header></Header>
  <BlogArticleDetail></BlogArticleDetail>
  <Footer></Footer>
  </div>
</template>

<script>
import Header from "./common/Header";
import Footer from "./common/Footer";
import BlogArticleDetail from "./blog/BlogArticleDetail";
export default {
  name: "BlogDetail",
  components: {
    Header,
    BlogArticleDetail,
    Footer,

  },
}
</script>

<style scoped>

</style>

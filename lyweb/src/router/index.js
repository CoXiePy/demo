import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
// import ElementUI from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css';
// import Login from "../components/Login";
import BlogArticles from "../components/blog/BlogArticles";
import Blog from "../components/Blog";
import BlogDetail from "../components/BlogDetail";



Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },


    // {
    //   path: '/register',
    //   name: 'RegisterNew',
    //   component: RegisterNew
    // },
    {
      path: '/blog',
      component: Blog,
      children: [
        {path: '', redirect: '/blog/articles'}, // 这里出问题了
        {path: '/blog/articles', component: BlogArticles},  // 主页的路由,不要轻易动
      ]
    },
    {
      path: "/blog/detail/:id/",
      name: BlogDetail,
      component: BlogDetail,
    },
  ]
})

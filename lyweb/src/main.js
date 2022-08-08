// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import settings from './settings'
import '../static/css/retset.css'
import axios from 'axios'; // 从node_modules目录中导入包
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// ------- markdown 配置
import marked from "marked";
import "../static/css/github-markdown.css"
import "../static/css/materialdesignicons.min.css"
const markedMixin = {
  methods: {
    md(){
      return marked(input);
    }
  }
};
Vue.prototype.md = markedMixin.methods.md;
// ------- markdown 配置
// font-awesome配置
import "font-awesome/css/font-awesome.min.css"


// font-awesome配置结束


Vue.use(ElementUI);
// 客户端配置是否允许ajax发送请求时附带cookie，false表示不允许
axios.defaults.withCredentials = false;
Vue.prototype.$settings = settings;
Vue.prototype.$axios = axios; // 把对象挂载vue中
Vue.config.productionTip = false


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})

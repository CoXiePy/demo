<template>
  <!--    博客声明>-->
  <div class="state">
    <h1>博客声明</h1>
    <ul class="state-ul">
      <li>该博客仅用于个人技术知识分享,专门分享python语言的相关技术</li>
      <li>该博客不对外提供文章撰写功能,若要分享,仅可通过投稿形式筛选后才可展示</li>
      <li>该博客的一切最终解释权归本人所有,也望大家监督</li>
      <li>该博客采用开源形式,源码可通过github来获取(博客上线后会公开源码)</li>
      <li>该博客在未得到相关的备案,不提供相关的功能,包括但不限于以下几点:<br></li>

      <li class="state-ul-li-s">登录、注册、视频观看等一切需登录后才可使用的功能</li>
      <li class="state-ul-li-l">如有需要联系,可添加微信:coxie_py,进行问题反馈</li>
    </ul>
  </div>


</template>

<script>

export default {
  name: "Statement",
  data() {
    return {}
  },

}
</script>

<style scoped>
.state {
  color: #4E5D59FF;
  height: 500px;
  margin: auto 0;
}

.state-ul li {
  margin-top: 30px;
}

.state-span {
  font-weight: 50;
}

.state-ul-li-s {
  color: red;
  font-weight: bolder;

}

.state-ul-li-l {
  color: red;
  font-weight: bolder;
}
</style>

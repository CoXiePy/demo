<template>
  <!--  博客的显示页面-->

  <el-row>
    <h1 class="">显示页面</h1>
    <el-card class="box-card-left">  <!-- 循环写这里 -->
      <template #header>
        <div class="card-header text-a-no">
          <slot name="article-title"> <!--插槽一，插入文章标题部分-->
            <h1 style="text-align: center">{{ acticle.title }}</h1>
          </slot>
        </div>
      </template>
      <slot name="article-content"> <!--插槽二，插入文章内容 -->
        <div v-html="markdown" class="markdown-body markdown-stule"></div>
        <div class="item-ft mar-left">
          <div class="text item"> <!--默认值-->
            <!--          <VueMarkdown :source="acticle.content"></VueMarkdown>-->

          </div>
          <div class="fa fa-eye">
            <span>{{ acticle.re_blog_comment.praise }}</span>
          </div>
          <div class="fa fa-thumbs-o-up mar-left">
            <span>{{ acticle.re_blog_comment.reading }}</span>
          </div>
          <div class="fa fa-commenting-o mar-left">
            <span>{{ acticle.re_blog_comment.comments }}</span>
          </div>
          <!--          放右侧两个字体图标-->
          <div class="mar-right">
            <div class="fa fa-calendar-times-o">
              <span>{{ acticle.updated_time }}</span>
            </div>
            <div class="fa fa fa-user-o mar-three">
              <span>{{ acticle.author_name }} </span>
            </div>
          </div>

        </div>
      </slot>
    </el-card>
  </el-row>
</template>

<script>
import marked from 'marked'
import 'highlight.js/styles/foundation.css'
import MarkdownIt from "markdown-it";
export default {
  name: "BlogArticles",
  components: {},
  data() {
    return {
      content: "# s测试3内容哦个\r\n```python\r\nfor i in range(5):\r\n\tprint(i)\r\n```\r\n\r\n\r\n> 可以看到结果 0,1,2,3,4",
      acticle: {
        "id": 4,
        "title": "测3",
        "abstract": "测3摘要",
        "content": "# s测试3内容哦个\r\n```python\r\nfor i in range(5):\r\n\tprint(i)\r\n```\r\n\r\n\r\n> 可以看到结果 0,1,2,3,4",
        "updated_time": "2022-08-02 01:15:30",
        "tags_data": [
          {
            "name": "Django-Rest-Framework"
          }
        ],
        "author": 1,
        "author_name": "该用户很懒没有设置昵称",
        "re_blog_comment": {
          "praise": 3,
          "reading": 4,
          "comments": 5
        }
      },
    }
  },

  methods: {
    // 发生请求数据:获取id=? 的博客文章数据
    get_acticels_data() {

    },
  },

  created() {
    console.log("文章详情页进来了");
    this.get_acticels_data();

  },
  computed: {
    markdown() {
    const  md = new MarkdownIt();
    return md.render(this.content)
    }
  },
}


</script>

<style scoped>
.text {
  font-size: 15px;
}
.markdown-stule {
  text-align: left;
}
.item {
  margin-bottom: 18px;
  text-align: left;
}

.box-card-left {
  width: 60%;
  min-width: 460px;
  margin: 10px auto;
}

.text-a-no {
  text-align: left;
}

.item-ft {
  font-size: 15px;
  text-align: left;
  color: #999abd;
}


.mar-left {
  margin-left: 8px;
}

.mar-right {
  float: right;
}

.mar-right div {
  margin-right: 8px;
}

span {
  margin-left: 8px;
}

.mar span {
  margin-left: 8px;
}

.article {
  width: 1200px;
  margin: 30px auto;
  overflow: hidden;
}

/* markdown 行号的样式 */
#content li {
  list-style: decimal;
}

.article-con div pre {
  position: relative;
  padding: 0 29px;
  overflow: hidden;
  font-size: 90%;
  line-height: 1.9;
  background: #282c34;
}

.article-con div pre code {
  padding: 0.4em;
}

.article-con div .pre-numbering {
  position: absolute;
  top: 0;
  left: 0;
  width: 29px;
  padding: 9px 7px 12px 0;
  border-right: 1px solid #C3CCD0;
  background: #282c34;
  text-align: right;
  font-size: 16px;
  line-height: 1.45;
}

.pre-numbering li {
  list-style: none;
  font-family: Menlo, monospace;
  color: #abb2bf;
}

.mar-three {
  width: 80px;
  overflow: hidden;

  text-overflow: ellipsis;

  white-space: nowrap;
}
</style>

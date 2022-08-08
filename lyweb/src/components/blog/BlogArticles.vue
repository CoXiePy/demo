<template>
  <!--  博客的显示页面-->
  <el-row>
    <el-card class="box-card-left" v-for="(value,index) in this.acticles_list" :key="value.id">  <!-- 循环写这里 -->
      <template #header>
        <router-link :to='"/blog/detail/" + value.id + "/"'>
          <div class="card-header">
            <slot name="article-title"> <!--插槽一，插入文章标题部分-->
              {{ value.title }} ,{{ value.id }} <!--默认值-->
            </slot>
          </div>
        </router-link>
      </template>

      <slot name="article-content"> <!--插槽二，插入文章摘要部分-->
        <router-link :to=" '/detail/' + value.id + '/' ">
          <div class="text item"> <!--默认值-->
            {{ value.abstract }}
          </div>
        </router-link>
        <div class="item-ft mar-left">
          <div class="fa fa-eye">
            <span>{{ value.blog_comment.praise }}</span>
          </div>
          <div class="fa fa-thumbs-o-up mar-left">
            <span>{{ value.blog_comment.reading }}</span>
          </div>
          <div class="fa fa-commenting-o mar-left">
            <span>{{ value.blog_comment.comments }}</span>
          </div>
          <!--          放右侧两个字体图标-->
          <div class="mar-right">
            <div class="fa fa-calendar-times-o">
              <span>{{ value.updated_time }}</span>
            </div>
            <div class="fa fa fa-user-o mar-three">
              <span>{{ value.author_name }} </span>
            </div>
          </div>


        </div>
      </slot>

    </el-card>

  </el-row>

</template>

<script>
export default {
  name: "BlogArticles",
  data() {
    return {
      acticles_list: [
        {
          "id": 4,
          "title": "博客测试1",
          "abstract": "博客测试1 的摘要",
          "updated_time": "2022-07-29 15:45:18",
          "tags_data": [
            {
              "name": "Django"
            }
          ],
          "author": 1,
          "author_name": "该用户很懒没有设置昵称",
          "blog_comment": {
            "praise": 1,
            "reading": 1,
            "comments": 1
          }
        },
        {
          "id": 4,
          "title": "博客测试2",
          "abstract": "博客测试2的摘要",
          "updated_time": "2022-07-29 15:45:44",
          "tags_data": [
            {
              "name": "Django-Rest-Framework"
            }
          ],
          "author": 1,
          "author_name": "该用户很懒没有设置昵称",
          "blog_comment": {
            "praise": 2,
            "reading": 2,
            "comments": 2
          }
        },
        {
          "id": 4,
          "title": "测3",
          "abstract": "测3摘要",
          "updated_time": "2022-08-02 01:15:30",
          "tags_data": [
            {
              "name": "Django-Rest-Framework"
            }
          ],
          "author": 1,
          "author_name": "该用户很懒没有设置昵称",
          "blog_comment": {
            "praise": 3,
            "reading": 4,
            "comments": 5
          }
        }
      ],
    }
  },
  methods: {
    // 发生请求数据:获取博客列表数据
    get_acticels_data() {
      console.log("get", this)
      this.$axios.get(`${this.$settings.host}/blog/`)
        .then((res) => {
          this.acticles_list = res.data;
        }).catch((error) => {
        console.log(message.error("请求失败"))
      })
    },
  },
  created() {
    this.get_acticels_data();
    // console.log("created", this)
  },
}


</script>

<style scoped>
.text {
  font-size: 15px;
}

.item {
  margin-bottom: 18px;
  text-align: left;
}

.box-card-left {
  margin: auto;
  width: 60%;
  min-width: 460px;
  margin-top: 10px;
  margin-bottom: 10px;
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

.mar-three {
  width: 50px;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
</style>

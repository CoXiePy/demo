<template>
  <el-row>
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <slot name="article-title"> <!--插槽一，插入文章标题部分-->
            博客标题  <!--默认值-->
          </slot>
        </div>
      </template>
      <slot name="article-content"> <!--插槽二，插入文章内容部分-->
        <div v-for="o in 4" :key="o" class="text item"> <!--默认值-->
          {{ '博客内容 ' + o }}
        </div>
      </slot>
    </el-card>
  </el-row>
</template>

<script>
export default {
  name: "BlogCard"
}
</script>

<style scoped>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}

.box-card {
  margin-left: auto;
  width: 70%;
  min-width: 1200px;
}
</style>

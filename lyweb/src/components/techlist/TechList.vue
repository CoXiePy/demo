<template>

    <Alipay></Alipay>


</template>

<script>
import Alipay from "./Alipay";
import Order from "./Order";
import SMS from "./SMS";

export default {
  name: "TechList",
  components: {
    Alipay,
    Order,
    SMS,
  }

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


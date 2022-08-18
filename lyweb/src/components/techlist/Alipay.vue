<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>购物车模拟(积分|优惠券|支付)</span>
      <!--    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
    </div>
    <div class="discount">
      <div id="accordion">
        <div class="coupon-box">
          <div class="icon-box">
            <span class="select-coupon">使用优惠劵：</span>
            <a class="select-icon unselect" :class="use_coupon?'is_selected':''" @click="use_coupon=!use_coupon">
              <img class="sign is_show_select" src="../../../static/image/12.png" alt="">
            </a>
            <span class="coupon-num">有{{ coupon_list.length }}张可用</span>
          </div>
          <p class="sum-price-wrap">商品总金额：<span class="sum-price">{{ t_price.toFixed(2) }}元</span></p>
        </div>
        <!--           给过期的优惠券添加不能点击事件或者优惠券不显示的问题-->
        <div id="collapseOne" v-if="use_coupon">
          <ul class="coupon-list" v-if="coupon_list.length>0">
            <li class="coupon-item " @click="change_coupon_status(coupon_value.id,coupon_index)"
                :class="coupon_status(coupon_value.id,coupon_index)"
                v-for="(coupon_value,coupon_index) in coupon_list">
              <p class="coupon-name">{{ coupon_value.coupon.name }}</p>
              <p class="coupon-condition">{{ coupon_value.coupon.conditions }}</p>
              <p class="coupon-time start_time">开始时间：{{ coupon_value.start_time }}</p>
              <p class="coupon-time end_time">过期时间：{{ coupon_value.end_time.replace('T', '') }}</p>
            </li>
          </ul>
          <div class="no-coupon" v-if="coupon_list.length<1">
            <span class="no-coupon-tips">暂无可用优惠券</span>
          </div>
        </div>
        <div class="credit-box">
          <!--          <label class="my_el_check_box">-->
          <!--            <el-checkbox class="my_el_checkbox" v-model="use_credit"></el-checkbox>-->
          <!--          </label>-->
          <!--          <p class="discount-num1" v-if="!use_credit"></p>-->
          <p class="discount-num2" @click="get_credit()"><span>总积分：{{ credit }},本次将花费
            <el-input-number v-model="credit_num" @change="handleChange" :min="0" :max="max_credit()"
                             label="描述文字">

            </el-input-number>
            积分,已抵扣 ￥{{ (credit_num / credit_to_money).toFixed(2) }}，</span></p>
        </div>
        <p class="sun-coupon-num">优惠券抵扣：<span>{{ this.coupon_price.toFixed(2) }}元</span></p>
      </div>
    </div>
    <div class="calc">
        <el-row class="pay-row">
          <el-col :span="4" class="pay-col"><span class="pay-text">支付方式：</span></el-col>
          <el-col :span="8">
            <span class="alipay" v-if="pay_type===0"><img src="../../../static/image/alipay2.png" alt=""></span>
            <span class="alipay" v-else style="cursor: pointer" @click="pay_type=0"><img
              src="../../../static/image/alipay.png" alt=""></span>
            <span class="alipay wechat" v-if="pay_type===1"><img src="../../../static/image/wechat2.png" alt=""></span>
            <span class="alipay wechat" v-else style="cursor: pointer" @click="pay_type=1"><img
              src="../../../static/image/wechat.png" alt=""></span>
          </el-col>
          <el-col :span="8" class="count">实付款： <span>¥ {{
              (t_price - this.credit_num / this.credit_to_money).toFixed(2)
            }}</span></el-col>
          <el-col style="cursor: pointer" :span="4" class="cart-pay"><span @click="payhander"> 去支付</span></el-col>
        </el-row>
      </div>

  </el-card>

</template>

<script>

export default {
  name: "alipay",
  components: {},

  data() {
    return {
      coupon_list: [
        {
          "id": 2,
          "start_time": "2022-08-15 22:53:00",
          "end_time": "2022-08-22T22:53:00",
          "coupon": {
            "name": "618:-10",
            "condition": 20,
            "sale": "-10",
            "coupon_type": 1
          }
        },
        {
          "id": 3,
          "start_time": "2022-08-15 22:55:00",
          "end_time": "2022-09-14T22:55:00",
          "coupon": {
            "name": "开学季:8折",
            "condition": 100,
            "sale": "*0.8",
            "coupon_type": 0
          }
        }
      ],
      settle_data: [],
      total_price: 5000.11,
      t_price: 5000.11, // 使用优惠券后的价格
      pay_type: 0,
      use_coupon: 0,
      use_credit: 0,
      credit: 0,
      credit_to_money: 0,
      coupon_price: 0,  // 优惠券抵扣的金额
      credit_num: 0,
    }
  },
  methods: {
    // 计算优惠券抵扣的价钱


    // 获取当前金额可用最大积分
    max_credit() {
      let mc = this.t_price * this.credit_to_money;
      if (mc > this.credit) {
        return parseInt(this.credit)
      } else {
        return parseInt(mc)
      }

    },

    // 获取保存在session中的积分
    handleChange(val) {
      if (val === undefined) {
        this.credit_num = 0;
        return false
      } else {
        this.credit_num = val;

      }
      // 获取去除积分后的价格


    },


    get_credit() {
      this.credit = localStorage.credit || sessionStorage.credit;
      this.credit_to_money = localStorage.credit_to_money || sessionStorage.credit_to_money;
    },

    // 点击使用优惠券修改总金额

    change_coupon_status(coupon_id, coupon_index) {
      console.log(coupon_index)
      let data = this.coupon_list[coupon_index]
      let sale = data.coupon.sale; //
      // console.log(data);

      let condition = data.coupon.condition;
      let now = (new Date()) / 1000;

      let s_time = (new Date(data.start_time)) / 1000;
      let e_time = (new Date(data.end_time)) / 1000;
      if (now < s_time || now > e_time) {
        return false
      }
      if (this.total_price < condition) {
        return false
      }
      // 开始计算优惠券使用后的价格
      this.t_price = this.total_price;
      this.select_coupon_id = coupon_id;

      let a = sale[0];
      let n = parseFloat(sale.substr(1));
      this.coupon_price = n;
      if (a === '-') {
        this.t_price -= n;
      } else {
        this.t_price *= n;
      }
      this.coupon_price = this.total_price - this.t_price;


    },
    // 筛选所有的优惠券中可用的优惠券
    coupon_status(coupon_id, coupon_index) {
      let data = this.coupon_list[coupon_index]
      // console.log(data);
      let condition = data.coupon.condition;
      // 获取当前时间戳， 秒级单位
      let now = (new Date()) / 1000;
      // 获取优惠券开始时间戳和结束时间戳
      let s_time = (new Date(data.start_time)) / 1000;
      let e_time = (new Date(data.end_time)) / 1000;
      if (now < s_time || now > e_time) {
        return 'disable'
      }
      if (this.total_price < condition) {
        return 'disable'
      }

      if (this.select_coupon_id === coupon_id) {
        return 'active';
      }

      return ''

    },
    payhander() {
      let token = sessionStorage.token || localStorage.token;
      console.log(this.pay_type)
      this.$axios.post(`${this.$settings.host}/order/list/`, {
        pay_type: this.pay_type,
        credit: this.credit_num,  // 使用的积分
        coupon: this.select_coupon_id,  // 选择的优惠券id
      }, {
        headers: {
          'authorization': `jwt ${token}`,
        }
      }).then((res) => {
        let order_number = res.data.order_number;

        this.$message.success("订单生产成功，即将跳往支付页面")
        this.$axios.get(`${this.$settings.host}/payment/list/?order_number=${order_number}`,
          {
            headers: {
              'authorization': `jwt ${token}`,
            }
          }
        ).then((res) => {
          console.log(res.data.url);
          // this.$router.go(res.data.url)
          location.href = res.data.url;
        }).catch((error) => {
          this.$message.error("跳转失败")
        })


      }).catch((error) => {
        this.$message.error('失败')
      })
    },
    // 获取优惠券数据
    get_coupon_data() {
      let token = sessionStorage.token || localStorage.token;
      this.$axios.get(
        `${this.$settings.host}/coupon/list`,
        {
          headers: {
            'authorization': `jwt ${token}`,
          }
        }
      ).then((res) => {
        console.log(res.data);
        this.coupon_list = res.data
      }).catch((error) => {
        this.$message.error("优惠券获取失败")
      })
    },
    // 获取购物车数据
    /*get_settle_data() {*/
    /*  let token = localStorage.token || sessionStorage.token;*/
    /*  this.$axios.get(`${this.$settings.host}/cart/settle/`,*/
    /*    {*/
    /*      headers: {*/
    /*        "authorization": `jwt ${token}`*/
    /*      }*/
    /*    })*/
    /*    .then((res) => {*/

    //       // res.data => {'cart_data': [], 'total': }
    //       this.settle_data = res.data.cart_data
    //       this.total_price = res.data.total
    //       this.t_price = res.data.total
    //
    //     })
    //     .catch((error) => {
    //       this.$message.error("出错了")
    //     })
    // }
  },
  created() {
    // this.get_settle_data();
    this.get_coupon_data();
    this.get_credit();

    console.log(11111)

  },

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
  width: 70%;
  min-width: 550px;
  margin: 20px auto 20px;
}

.coupon-box {
  text-align: left;
  padding-bottom: 22px;
  padding-left: 30px;
  border-bottom: 1px solid #e8e8e8;
}

.coupon-box::after {
  content: "";
  display: block;
  clear: both;
}

.icon-box {
  float: left;
}

.icon-box .select-coupon {
  float: left;
  color: #666;
  font-size: 16px;
}

.icon-box::after {
  content: "";
  clear: both;
  display: block;
}

.select-icon {
  width: 20px;
  height: 20px;
  float: left;
}

.select-icon img {
  max-height: 100%;
  max-width: 100%;
  margin-top: 2px;
  transform: rotate(-90deg);
  transition: transform .5s;
}

.is_show_select {
  transform: rotate(0deg) !important;
}

.coupon-num {
  height: 22px;
  line-height: 22px;
  padding: 0 5px;
  text-align: center;
  font-size: 12px;
  float: left;
  color: #fff;
  letter-spacing: .27px;
  background: #fa6240;
  border-radius: 2px;
  margin-left: 20px;
}

.sum-price-wrap {
  float: right;
  font-size: 16px;
  color: #4a4a4a;
  margin-right: 45px;
}

.sum-price-wrap .sum-price {
  font-size: 18px;
  color: #fa6240;
}

.no-coupon {
  text-align: center;
  width: 100%;
  padding: 50px 0px;
  align-items: center;
  justify-content: center; /* 文本两端对其 */
  border-bottom: 1px solid rgb(232, 232, 232);
}

.no-coupon-tips {
  font-size: 16px;
  color: #9b9b9b;
}

.credit-box {
  height: 30px;
  margin-top: 40px;
  display: flex;
  align-items: center;
  justify-content: flex-end
}

.my_el_check_box {
  position: relative;
}

.my_el_checkbox {
  margin-right: 10px;
  width: 16px;
  height: 16px;
}

.discount {
  overflow: hidden;
}

.discount-num1 {
  color: #9b9b9b;
  font-size: 16px;
  margin-right: 45px;
}

.discount-num2 {
  margin-right: 45px;
  font-size: 16px;
  color: #4a4a4a;
}

.sun-coupon-num {
  margin-right: 45px;
  margin-bottom: 43px;
  margin-top: 40px;
  font-size: 16px;
  color: #4a4a4a;
  display: inline-block;
  float: right;
}

.sun-coupon-num span {
  font-size: 18px;
  color: #fa6240;
}

.coupon-list {
  margin: 20px 0;
}

.coupon-list::after {
  display: block;
  content: "";
  clear: both;
}

.coupon-item {
  float: left;
  margin: 15px 8px;
  width: 180px;
  height: 100px;
  padding: 5px;
  background-color: #fa3030;
  cursor: pointer;
}

.coupon-list .active {
  background-color: #fa9000;
}

.coupon-list .disable {
  cursor: not-allowed;
  background-color: #fa6060;
}

.coupon-condition {
  font-size: 12px;
  text-align: center;
  color: #fff;
}

.coupon-name {
  color: #fff;
  font-size: 24px;
  text-align: center;
}

.coupon-time {
  text-align: left;
  color: #fff;
  font-size: 12px;
}

.unselect {
  margin-left: 0px;
  transform: rotate(-90deg);
}

.is_selected {
  transform: rotate(-1turn) !important;
}

.cart {
  margin-top: 80px;
}

.cart-info {
  overflow: hidden;
  width: 1200px;
  margin: auto;
}

.cart-top {
  font-size: 18px;
  color: #666;
  margin: 25px 0;
  font-weight: normal;
}

.cart-top span {
  font-size: 12px;
  color: #d0d0d0;
  display: inline-block;
}

.cart-title {
  background: #F7F7F7;
  height: 70px;
}

.calc {
  margin-top: 25px;
  margin-bottom: 40px;
}

.calc .count {
  text-align: right;
  margin-right: 10px;
  vertical-align: middle;
}

.calc .count span {
  font-size: 36px;
  color: #333;
}

.calc .cart-pay {
  margin-top: 5px;
  width: 110px;
  height: 38px;
  outline: none;
  border: none;
  color: #fff;
  line-height: 38px;
  background: #ffc210;
  border-radius: 4px;
  font-size: 16px;
  text-align: center;
  cursor: pointer;
}

.cart-item {
  height: 120px;
  line-height: 120px;
  margin-bottom: 30px;
}

.course-info img {
  width: 175px;
  height: 115px;
  margin-right: 35px;
  vertical-align: middle;
}

.alipay {
  display: inline-block;
  height: 48px;
}

.alipay img {
  height: 100%;
  width: auto;
}

.pay-text {
  display: block;
  text-align: right;
  height: 100%;
  line-height: 100%;
  vertical-align: middle;
  margin-top: 20px;
}
</style>

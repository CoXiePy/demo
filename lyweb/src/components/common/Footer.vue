<template>
    <div class="footer">
      <div class="footer-item">
        <div class="foot-left">
        <div class="foot-content">
          <p>
            <span>关于我们</span>
<!--            &nbsp;&nbsp;|&nbsp;&nbsp;-->
<!--            <span>贝里小卖铺</span>-->
          </p>
          <p>
            地址:广东省广州市天河区珠江新车乔鑫国际(测试)  邮箱：lzcom321@gmail.com
          </p>
          <p>
             © 2022-2024 广东广州测试科技有限公司版权所有
            <a class="copyright" href="http://beian.miit.gov.cn" target="_blank" >京ICP备66666666号-1</a>
          </p>
          <p>
            <a class="report-link" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102002019&amp;token=1ee3034d-ba3a-4cc3-89d4-89875e2dd0b1">
              <img class="report-img" src="//img.alicdn.com/tfs/TB1..50QpXXXXX7XpXXXXXXXXXX-40-40.png" >
              京公网安备 12345671002022号
            </a>
          </p>
        </div>

      </div>


<!--        <img src="@/assets/code.png" alt="" class="code">-->
      </div>
    </div>
</template>

<script>
    export default {
        name: "Foot"
    }
</script>

<style scoped>

  .footer{
    display: flex;
    align-items: center;
    width: 100%;
    height: 200px;
    flex-direction: column;
    overflow: hidden;
    background: #191c25;
  }
  .footer .foot-left{
    display: flex;
    align-items: center;
  }
  .footer .foot-left .foot-content p{
    margin-bottom: 10px;
    font-size: 13px;
    font-family: 黑体;
    font-weight: 400;
    color: #d0d0d0;
  }
  .footer-item{
    width: 960px;
    height: 100%;
    justify-content: space-between;
  }
  .foot-left{
    display: flex;
    align-items: center;
    float: left;
  }
  .foot-content a{
    color: #d0d0d0;
  }
  .footer .foot-left .foot-content p:first-child span{
    font-size: 16px;
    font-weight: 400;
    display: inline-block;
    font-family: 宋体;
    cursor: pointer;
  }
  .foot-content .report-img{
    display: inline-block;
    height: 20px;
    margin-right: 12px;
  }
  .footer-item .code{
    width: 74px;
    height: auto;
    margin-right: 100px;
    float: right;
    padding-top: 30px;
  }

</style>

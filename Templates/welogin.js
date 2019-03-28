/*
Time    : 2019/2/25 16:48
Author  : wangguoqiang@kedacom.com
*/
"use strict";
// 解决兼容问题 

let loginStore = {
    conenteId:'storesearch',
    loginurl: '/login/',
    homeurl: '/home/',
    disklist: {
        data: [],
        type: 0,
    },
    actions: {
        checkpath:function(path){
            if(path == "" || path == null)
            {
                return false;
            }else{
                return true;
            }

        },
        login: function(account, password, vertifyCode){
            $.ajax({
                url: loginStore.loginurl,
                type: 'POST',
                data: {
                    account: account,
                    password: password,
                    vertifyCode:vertifyCode,
                },
                dataType: 'json',
                success: function (data) {
                    console.log("login test");
                    console.log(data.webmsg);
                    var result = parseInt(data.webmsg.success);
                    if(result == 0){
                        alert("errcode:"+ data.webmsg.errcode + "\ndetails:" + data.webmsg.details);
                    }
                    else{
                        window.location.href = loginStore.homeurl;

                    }
                }
            })
        },
        centerDiv:function(elementID){
            window.onload=function(){
                console.log(elementID);
                var element = document.getElementById(elementID);//获取div块对象
                var Height=document.documentElement.clientHeight;//取得浏览器页面可视区域的高度
                var Width=document.documentElement.clientWidth;  //取得浏览器页面可视区域的宽度
                var divH = element.offsetHeight;//获取div块的高度值
                var divW = element.offsetWidth;//获取div块的宽度值
                var CenterHeight= (Height - divH)/2+"px";
                var CenterWidth= (Width - divW)/2+"px";
                element.style.top=CenterHeight;
                element.style.left=CenterWidth;
            }


        },
    }
}
loginStore.actions.centerDiv('loginID');

let loginapp = {
    template:`
    <div class="container">
    <div class="col-sm-6 testonly" id="loginID">
        <div class="form form-group">
            <div class="col-sm-3 testonly">
                <label style="float:left;">账  号：</label>
            </div>
            <div class="col-sm-8">
                <input type="text" class="form-control" id="inputAccount" 
                 placeholder="请输入账号">
            </div>
            <div class="col-sm-12 myseperator"></div>   
            <div class="col-sm-3 testonly">
                <label style="float:left;">密  码：</label>
            </div>
            <div class="col-sm-8">
                <input type="text" class="form-control" id="inputPassword" 
                 placeholder="请输入密码（仅限数字字母下划线）">
            </div>
            <div class="col-sm-12 myseperator"></div>
            <div class="col-sm-3 testonly">
                <label style="float:left;">验证码：</label>
            </div>
            <div class="col-sm-4">
                <input type="text" class="form-control" id="inputCode"  
                 placeholder="请输入验证码">
            </div>
            <div class="col-sm-4">
                <input type="text" class="form-control" id="imgCode"
                 placeholder="请输入验证码">
            </div>
            <div class="col-sm-3">
                <button class="btn btn-primary myinnerbtn" @click="login">登录</button>
            </div>
            <div class="col-sm-12 mytempdiv"></div>
        </div>
    </div>
    </div>
    `,
    methods:{
        login(){
            var account = $("#inputAccount").val();
            var password = $("#inputPassword").val();
            var vercode = $("#inputCode").val();
            loginStore.actions.login(account, password, vercode);

        },
    },
}

let root = new Vue({
    el:'#loginapp',
    template:`<loginapp></loginapp>`,
    components:{
        'loginapp':loginapp
    },
})
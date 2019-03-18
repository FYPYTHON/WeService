/*
created:2019/3/14
Author :ljf2010_2010@126.com
*/
"use strict";
// 解决兼容问题 
// Block-scoped declarations (let, const, function, class) not yet supported outside strict mode
// 文件列表
let homeStore = {
    conenteId:'profile',
    filelist: {
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
        getFileList: function(path, ftype){
            $.ajax({
                url: '/api/',
                async : false,
                type: 'GET',
                headers:{
                    type: atype,
                    home: hometype
                },
                data: {
                    path: path,
                    type: ftype
                },
                dataType: 'json',
                success: function (data) {

                    var all_file_directory = data.filelist.directory.concat(data.filelist.file)
                    homeStore.filelist.data = all_file_directory
                }
            })
        },
        getFileListSync: function(path, ftype, atype, hometype){
            $.getJSON({
                url: '/api/',
                type: 'GET',
                headers:{
                    type: atype,
                    home: hometype,
                    'file-size':520,
                },
                data: {
                    path: path,
                    type: ftype
                },
                dataType: 'json',
                success: function (data) {
                    var result = parseInt(data.repmsg.success);
                    if(result == 0){
                        alert("errorcode:"+ data.repmsg.errorcode + "\nderccription:" + data.repmsg.description);
                    }
                    else{
                        var all_file_directory = data.filelist.directory.concat(data.filelist.file);
                        homeStore.filelist.data = all_file_directory;
                        $("#searchResultSync").html("");
                        for (var i = 0; i < all_file_directory.length; i++) {
                            var item = '<li>' + all_file_directory[i] + '</li>';
                            $("#searchResultSync").append(item);  
                        }
                    }
                }
            })
        },

    }
}
let navBar = {
    template:`
    <nav class="navbar navbar-default">
        <div class="container-fluid">
              <ul class="nav navbar-nav">
                <li><button v-bind:class="{active:status=='profile'}" class="btn  mynavbtn" id="profile" @click="nav_profile">{{profile}}</button></li>
                <li><button v-bind:class="{active:status=='chart'}" class="btn  mynavbtn" id="chart" @click="nav_chart">{{chart}}</button></li>
                <li><button v-bind:class="{active:status=='device'}" class="btn  mynavbtn" id="device" @click="nav_device">{{device}}</button></li>
                <li><button v-bind:class="{active:status=='map'}" class="btn  mynavbtn" id="map" @click="nav_map">{{map}}</button></li>
                <li><button v-bind:class="{active:status=='user'}" class="btn  mynavbtn" id="user" @click="nav_user">{{user}}</button></li>
                <li><button v-bind:class="{active:status=='setting'}" class="btn mynavbtn" id="setting" @click="nav_setting">{{setting}}</button></li>            
              </ul>
        </div>
    </nav>
    `,
    script:`
    <script type="text/javascript">
        console.log("navbar script.");
    </script>
    `,
    data:function(){
        return {
            profile:'Profile',
            chart:'Chart',
            device:'Device',
            map:'Map',
            user:'User',
            setting:'Setting',
            status:'profile',
        }
    },
    methods:{
        nav_profile(){
            this.compID = 'profile';
            this.status = 'profile';
        },
        nav_chart(){
            this.compID = 'chart';
            this.status = 'chart';
        },
        nav_device(){
            this.compID = 'device';
            this.status = 'device';
        },
        nav_map(){
            this.compID = 'map';
            this.status = 'map';
        },
        nav_user(){
            this.compID = 'user';
            this.status = 'user';
        },
        nav_setting(){
            this.compID = 'setting';
            this.status = 'setting';
        },

    },
}

let headContent = {
    template:`
    <div class="myhead"></div>
    `,
}
let headapp = {
    template:`
    <div class="myhead"></div>
    `
}
let profileContent = {}
let bodyContent = {}
let homeApp = {
    template:`
    <div>
    <headContent id="myhead"></headContent>
    <div class="container">
        <div class="row">
            <nav-bar></nav-bar>
        </div>
    </div>
    </div>
    `
    ,
    components:{
        'headContent':headContent,
        'nav-bar':navBar,
        // 'bodyContent':bodyContent,
    }
}
// let head = new Vue({
//     el:'#headapp',
//     template:`<headapp></headapp>`,
//     components:{
//         'headapp':headapp,
//     }
// })
let root = new Vue({
    el:'#homeapp',
    template:`<homeapp></homeapp>`,
    components:{
        'homeapp':homeApp,
    },
})
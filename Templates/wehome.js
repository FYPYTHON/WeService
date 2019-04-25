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
    uri:'/weservice/v1/',
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
    <div class="wemenu">
        <div class="container-fluid">
              <ul class="nav navbar-nav">
                <li><a v-bind:class="{current:status=='profile'}" id="profile" @click="nav_profile">{{profile}}</a></li>
                <li><a v-bind:class="{current:status=='chart'}" id="chart" @click="nav_chart">{{chart}}</a></li>
                <li><a v-bind:class="{current:status=='device'}" id="device" @click="nav_device">{{device}}</a></li>
                <li><a v-bind:class="{current:status=='map'}" id="map" @click="nav_map">{{map}}</a></li>
                <li><a v-bind:class="{current:status=='user'}" id="user" @click="nav_user">{{user}}</a></li>
                <li><a v-bind:class="{current:status=='setting'}" id="setting" @click="nav_setting">{{setting}}</a></li>            
              </ul>
        </div>
    </div>
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
let homeApp = {
    template:`
    <div>
    <headContent id="myhead"></headContent>
    <div class="container">
        <div class="row">
            <nav-bar></nav-bar>
        </div>
        <div class="col-sm-3 center-content">
            <left-content @getrightContentId="rightContentIdChanged"></left-content>
        </div>
        <div class="col-sm-8 center-content">
            <right-contents v-bind:is="rightContentId"></right-contents>
        </div> 
    </div>
    </div>
    `
    ,
    data:function(){
        return{
            rightContentId:globalVar.rightContentId,
        }
    },
    components:{
        'headContent':headContent,
        'nav-bar':navBar,
        'left-content':leftContent,
        'right-content':rightContent,
        'right-form':rightForm,
    },
    methods:{
        rightContentIdChanged(data){  // get id from left content
            console.log("right content id changed.",data);
            this.rightContentId = data;
        },
    }
}
let root = new Vue({
    el:'#homeapp',
    template:`<homeapp></homeapp>`,
    components:{
        'homeapp':homeApp,
    },
})
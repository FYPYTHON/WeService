// <li class="active"><a href="{{ home }}">Home</a></li>
// <li><a href="{{ about }}">About</a></li>
"use strict";
// 解决兼容问题 
// Block-scoped declarations (let, const, function, class) not yet supported outside strict mode
// 文件列表
let homeStore = {
    conenteId:'search',
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
                    store.filelist.data = all_file_directory
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
                        store.filelist.data = all_file_directory;
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
                <li class="active">{{home}}</li>
                <li>{{about}}</li>               
              </ul>
        </div>
    </nav>
    `,
    data:function(){
        return {
            home:'Home',
            about:'About'
        }
    }
}

let mainContent = {
    template:`
    <h1 class="fs-title testonly">{{ content }}</h1>
    `,
    data:function(){
        return {
            content:'文件服务器demo'
        }
    }
}

// let rightContent = {
//     // <searchContent></searchContent>
//     template:`
//     <div class="col-sm-8 mycontent testonly" id="switchContent">
//         <div class="mytempdiv testonly" style="background:#33CCFF">内容</div>

//         <component v-bind:is="which_to_show"></component>
//     </div>
//     `, // 逗号不能少
//     data(){
//         return {
//             which_to_show:store.conenteId,
//         }
//     },

//     components:{
//         // 'searchContent':searchContent,
//         'searchContent': searchContent,
//         'deleteContent': deleteContent,
//     },
//     methods:{
//         // this.which_to_show = store.conenteId;
//     }
// }
let searchContent = {}
let deleteContent = {}
let bodyContent = {
    template:`
    <div class="col-sm-12">
        <div class="col-sm-4 mymenu myborder">
            <div class="mytempdiv testonly" style="background:#33CCFF">操作</div>
            <ul class="list-unstyled" style="float:left">
                <li><button class="btn btn-info mybtn" id="search_con" @click="showsearch">查询</button></li>
                <li><button class="btn btn-info mybtn" id="new_con" @click="shownew">新建</button></li>
                <li><button class="btn btn-info mybtn" id="modify_con">修改</button></li>
                <li><button class="btn btn-info mybtn" id="copy_con" @click="showcopy">复制</button></li>
                <li><button class="btn btn-info mybtn" id="upload_con" @click="showupload">上传 </button></li>
                <li><button class="btn btn-info mybtn" id="delete_con" @click="showdownload">下载</button></li>
                <li><button class="btn btn-info mybtn" id="delete_con" @click="showdelete">删除</button></li>
            </ul>
        </div>
        <div class="col-sm-8 mycontent testonly" id="compID">
            <div class="mytempdiv testonly" style="background:#33CCFF">内容</div>
            <componentb v-bind:is="compID"></componentb>
        </div>
    </div>
    `,
    data(){
        return {
            compID: store.conenteId,
        }
    },
    components:{
        'search': searchContent,
        'delete': deleteContent,
        // 'new': newContent,
        // 'upload': uploadContent,
        // 'download': downloadContent,
        // 'copy': copyContent,
    },
    methods:{
        showsearch(){
            this.compID = 'search';
        },
        shownew(){
            this.compID = 'new';
        },
        showdelete(){
            this.compID = 'delete';
        },
        showupload(){
            this.compID = 'upload';
        },
        showdownload(){
            this.compID = 'download';
        },
        showcopy(){
            this.compID = 'copy';
        },
        showmodify(){
            this.compID = 'modify';
        }

    }
}
let homeapp = {
    template:`
    <div class="container">
        <div class="row">
            <nav-bar></nav-bar>
        </div>
        <div class="row" style="background:#33FFCC;">
            <main-content></main-content>
        </div>
        <div class="container-fluid">
            <bodyContent></bodyContent>
        </div>
    </div>
    `,
    components:{
        'nav-bar':navBar,
        'main-content':mainContent,
        'bodyContent':bodyContent,
    }
}

let root = new Vue({
    el:'#homeapp',
    template:`<homeapp></homeapp>`,
    components:{
        'homeapp':homeapp
    },
})
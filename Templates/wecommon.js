/*
created:2019/3/25
Author :ljf2010_2010@126.com
*/
"use strict";
let alertModal = {
    template:`
    <div>
    <div class="modal fade" v-show="showMask" id="myModal" tabindex="-1"
        role="dialog" aria-labelledby="myModalLabel" aria-hidden="false" data-backdrop="static">
        <div class="modal-dialog modal-sm myalert">
            <div class="modal-header">
                <button class="close" type="button" @click="closeMask" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="dialog-title">{{title}}</h4>
            </div>
            <div class="modal-body" v-html="content"></div>
            <div class="modal-footer">
                <div class="btn btn-info" @click="closeBtn" data-dismiss="modal" aria-hidden="true">
                    {{cancelText}}
                </div>
                <div class="btn btn-danger" @click="dangerBtn" data-dismiss="modal" aria-hidden="true">
                    {{dangerText}}
                </div>
                <div class="btn btn-primary" @click="confirmBtn" data-dismiss="modal" aria-hidden="true">
                    {{confirmText}}
                </div>
            </div>
        </div>
    </div>
    </div>
    `,
    props: {
        value: {},
        // 类型包括 defalut 默认， danger 危险， confirm 确认，
        type:{
            type: String,
            default: 'default'
        },
        content: {
            type: String,
            default: 'Message'
        },
        title: {
            type: String,
            default: '确认是否删除！'
        },
        cancelText: {
            type: String,
            default: '取消'
        },
        dangerText: {
            type: String,
            default: '删除'
        },

        confirmText: {
            type: String,
            default: '确认'
        },

    },
    data(){
        return{
            showMask: false,
        }
    },
    methods:{
        closeMask(){
            this.showMask = false;
        },
        closeBtn(){
            this.closeMask();
        },
        dangerBtn(){
            this.closeMask();
        },
        confirmBtn(){
            this.closeMask();
        },
        showModal(){
            console.log("modal show");
            $('#myModal').modal('show');
            // $('#myModal').modal();
            // data-backdrop="static"
        }
    },
}
let alertcommon = new Vue({
    el:'#modalapp',
    template:`<modalapp></modalapp>`,
    components:{
        'modalapp':alertModal,
    },
})
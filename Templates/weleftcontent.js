/*
created:2019/3/29
Author :ljf2010_2010@126.com
*/
"use strict";
var plus_img = 'css/img/plus.gif';
var minus_img = 'css/img/minus.gif';
let searchContent = {
	template:`
	<div class="sidebar_search">
	<form>
		<input type="text" id="weCommonSearchID" class="search_input" value="search keyword" />
		<input type="image" class="search_submit" src="img/search.png" @click="weCommonSearch" />
	</form>
	</div>
	`,
}
// span 图片， ：style绑定display属性。
let leftContent = {
	template:`
	<div class="wesidebarmenu">
		<a class="wemenuitem submenuheader" herf="" @click="showSubmenu">
				{{subname1}}
			<span class="accordsuffix">
				<img :src="plus_minus_img" class="statusicon">
			</span>
		</a>
		<div class="wesubmenu" v-bind:style="{display:submenuDisplay}">
			<ul>
				<li><a href="">submenu1</a></li>
				<li><a href="">submenu2</a></li>
			</ul>
		</div>
		<a class="wemenuitem submenuheader" herf="" @click="showSubmenu2">
			{{subname2}}
			<span class="accordsuffix">
				<img :src="plus_minus_img2" class="statusicon">
			</span>
		</a>
		<div class="wesubmenu" v-bind:style="{display:submenuDisplay2}">
			<ul>
				<li><a href="">submenu</a></li>
			</ul>
		</div>
	</div>
	`,
	data:function(){
		return{
			subname1:"系统设置",
			subname2:"配置管理",
			plus_minus_img:plus_img,
			plus_minus_img2:plus_img,
			submenuDisplay:'none',
			submenuDisplay2:'none',

		}
	},
	methods:{
		weCommonSearch(){
			var searchInput = $("#weCommonSearchID").val();
			console.log("search:", searchInput);
		},
		showSubmenu(){
			this.$emit('getrightContentId',"right-content");
			if(this.plus_minus_img == plus_img){
				this.submenuDisplay = "";
				this.plus_minus_img = minus_img;
			}else{
				this.submenuDisplay = "none";
				this.plus_minus_img = plus_img;
			}
		},
		showSubmenu2(){
			this.$emit('getrightContentId',"right-form"); // sent id to home>>right ontent
			console.log(this.subname2, "clicked");
			globalVar.rightContentId = 'right-form';
			if(this.plus_minus_img2 == plus_img){
				this.submenuDisplay2 = "";
				this.plus_minus_img2 = minus_img;
			}else{
				this.submenuDisplay2 = "none";
				this.plus_minus_img2 = plus_img;
			}
		},
	}

}
/*
Time    : 2019/4/9 15:33
Author  : wangguoqiang@kedacom.com
*/
"use strict";

var xdata = [0,1,2,3,4,5,6,7,8,9];
var ydata1 = [0,2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6];
var ydata2 = [0,23.2, 2.6, 7.7, 13.6, 62.2, 32.6, 2.0, 16.4, 122.3];
var used = [20,90,30,70,10,80,60,50];
var exist = [1,1,2,1,0,1,1,0];


let diskIOApp = {
	template:`
	<div id="diskIOCount" class="weechart">
	</div>
	`,
	created(){
		require.config({
	        paths: {
	            echarts: './js',    
	        }
   		});
   		require(
	        [    // 依赖项列表
	            'echarts',
	            'echarts/chart/bar',
	            'echarts/chart/line',
	            'echarts/chart/map'
	        ],
	        function (ec) {
            //--- 折柱 ---
	            var cpuUsed = ec.init(document.getElementById('diskIOCount'));
	            cpuUsed.setOption({
	                title : {
	                    text: '磁盘读写次数',
	                    subtext: '测试数据'
	                },
	                tooltip : {
	                    trigger: 'axis'
	                },
	                legend: {
	                    data:['读次数','写次数']
	                },
	                toolbox: {
	                    show : true,
	                    feature : {
	                        // mark : {show: true},
	                        // dataView : {show: true, readOnly: false},
	                        magicType : {show: true, type: ['line', 'bar']},
	                        // restore : {show: true},
	                        saveAsImage : {show: true}
	                    }
	                },
	                calculable : true,
	                xAxis : [
	                    {
	                        type : 'category',
	                        data : xdata,
	                        axisLabel: {
			                    interval: 0,
			                    rotate: 45,
			                    //倾斜度 -90 至 90 默认为0  
			                    margin: 2,
			                    textStyle: {
			                        fontWeight: "bolder",
			                        color: "#000000",
			                        fontSize:'7px',
			                    }
	                    	},
	                    }
	                ],
	                yAxis : [
	                    {
	                        type : 'value',
	                        splitArea : {show : true}
	                    }
	                ],
	                series : [
	                    {
	                        name:'读次数',
	                        type:'bar',
	                        data: ydata1
	                    },
	                    {
	                        name:'写次数',
	                        type:'bar',
	                        data: ydata2
	                    },
	                ]
	            });
        	}  // function
	    );  // require
	},
}
let cpuUsedApp = {
	template:`
	<div id="cpuUsedCount" class="weechart">
	</div>
	`,
	created(){
		require.config({
	        paths: {
	            echarts: './js',    
	        }
   		});
   		require(
	        [    // 依赖项列表
	            'echarts',
	            'echarts/chart/bar',
	            'echarts/chart/line',
	            'echarts/chart/map'
	        ],
	        function (ec) {
            //--- 折柱 ---
	            var cpuUsed = ec.init(document.getElementById('cpuUsedCount'));
	            cpuUsed.setOption({
	                title : {
	                    text: 'cpu使用率',
	                    subtext: '测试数据'
	                },
	                tooltip : {
	                    trigger: 'axis'
	                },
	                // legend: {
	                //     data:['cpu使用率']
	                // },
	                toolbox: {
	                    show : true,
	                    feature : {
	                        // mark : {show: true},
	                        // dataView : {show: true, readOnly: false},
	                        magicType : {show: true, type: ['line', 'bar']},
	                        // restore : {show: true},
	                        saveAsImage : {show: true}
	                    }
	                },
	                calculable : true,
	                xAxis : [
	                    {
	                        type : 'category',
	                        data : xdata,
	                        axisLabel: {
			                    interval: 0,
			                    rotate: 45,
			                    //倾斜度 -90 至 90 默认为0  
			                    margin: 2,
			                    textStyle: {
			                        fontWeight: "bolder",
			                        color: "#000000"
			                    }
	                    	},
	                    }
	                ],
	                yAxis : [
	                    {
	                        type : 'value',
	                        splitArea : {show : true}
	                    }
	                ],
	                series : [
	                    {
	                        name:'cpu使用率',
	                        type:'bar',
	                        data: ydata1
	                    },
	                ]
	            });
        	}  // function
	    );  // require
	},
}
let memoryUsedApp = {
	template:`
	<div id="memoryUsedCount" class="weechart">
	</div>
	`,
	created(){
		require.config({
	        paths: {
	            echarts: './js',    
	        }
   		});
   		require(
	        [    // 依赖项列表
	            'echarts',
	            'echarts/chart/bar',
	            'echarts/chart/line',
	            'echarts/chart/map'
	        ],
	        function (ec) {
            //--- 折柱 ---
	            var memoryUsed = ec.init(document.getElementById('memoryUsedCount'));
	            memoryUsed.setOption({
	                title : {
	                    text: '内存使用率',
	                    subtext: '测试数据'
	                },
	                tooltip : {
	                    trigger: 'axis'
	                },
	                toolbox: {
	                    show : true,
	                    feature : {
	                        // mark : {show: true},
	                        // dataView : {show: true, readOnly: false},
	                        magicType : {show: true, type: ['line', 'bar']},
	                        // restore : {show: true},
	                        saveAsImage : {show: true}
	                    }
	                },
	                calculable : true,
	                xAxis : [
	                    {
	                        type : 'category',
	                        data : xdata,
	                        axisLabel: {
			                    interval: 0,
			                    rotate: 45,
			                    //倾斜度 -90 至 90 默认为0  
			                    margin: 2,
			                    textStyle: {
			                        fontWeight: "bolder",
			                        color: "#000000"
			                    }
	                    	},
	                    }
	                ],
	                yAxis : [
	                    {
	                        type : 'value',
	                        splitArea : {show : true}
	                    }
	                ],
	                series : [
	                    {
	                        name:'内存使用率',
	                        type:'bar',
	                        data: ydata1,
	                    },
	                ]
	            });
        	}  // function
	    );  // require
	},
}
let netIOCountApp = {
	template:`
	<div id="netioCount" class="weechart">
	</div>
	`,
	created(){
		require.config({
	        paths: {
	            echarts: './js',    
	        }
   		});
   		require(
	        [    // 依赖项列表
	            'echarts',
	            'echarts/chart/bar',
	            'echarts/chart/line',
	            'echarts/chart/map'
	        ],
	        function (ec) {
            //--- 折柱 ---
	            var netIO = ec.init(document.getElementById('netioCount'));
	            netIO.setOption({
	                title : {
	                    text: '网口吞吐量',
	                    subtext: '测试数据'
	                },
	                tooltip : {
	                    trigger: 'axis'
	                },
	                legend: {
	                    data:['进口','出口']
	                },
	                toolbox: {
	                    show : true,
	                    feature : {
	                        magicType : {show: true, type: ['line', 'bar']},
	                        saveAsImage : {show: true}
	                    }
	                },
	                calculable : true,
	                xAxis : [
	                    {
	                        type : 'category',
	                        data : xdata,
	                        axisLabel: {
			                    interval: 0,
			                    rotate: 45,
			                    //倾斜度 -90 至 90 默认为0  
			                    margin: 2,
			                    textStyle: {
			                        fontWeight: "bolder",
			                        color: "#000000"
			                    }
	                    	},
	                    }
	                ],
	                yAxis : [
	                    {
	                        type : 'value',
	                        splitArea : {show : true}
	                    }
	                ],
	                series : [
	                    {
	                        name:'进口',
	                        type:'bar',
	                        data: ydata1,
	                    },
	                    {
	                        name:'出口',
	                        type:'bar',
	                        data: ydata2
	                    },
	                ]
	            });
        	}  // function
	    );  // require
	},
}
// v-bind:class="{样式:判断条件}"
// v-bind:class="{btn:index==0}"
// :class="clicked? 'blue-class':'red-class'"
let profileapp = {
	template:`
	<div class="container-fluid">
        <div class="row-fluid">
        	<div class="col-sm-12">
        		<h4>磁盘使用情况</h4>
        	</div>
        	<div class="col-sm-12">
	        	<div class="col-sm-3" v-for="(us,index) in diskinfo">
	        		<div class="wediskinfo">
	        			<div class="col-sm-12"><h6>盘位{{index+1}}</h6></div>
	        			<div class="col-sm-12" v-bind:class="flag[index]<1?'wegraybg':(flag[index]==1?'webluebg':'weredbg')">
	        				<h6 style="float:left;">磁盘{{index}}</h6>
	        				<h6 style="float:right;">容量:40T</h6>
	        			</div>
	        			<div class="col-sm-12">
	        				<h6 style="float:left;">已使用:20T</h6>
	        				<h6 style="float:right;">{{us}}%</h6>
	        			</div>
	        		</div>
	        	</div>
	        </div>
        	
        	<div class="col-sm-6">
        		<div id="cpuUsed" class="weechart"></div>
    		</div>
    		<div class="col-sm-6">
    			<diskioapp></diskioapp>
    		</div>
    		<div class="col-sm-6">
    			<cpuusedapp></cpuusedapp>
    		</div>
    		<div class="col-sm-6">
    			<memoryusedapp></memoryusedapp>
    		</div>
    		<div class="col-sm-6">
    			<netiocountapp></netiocountapp>
    		</div>
        </div>
    </div>
	`,
	data:function(){
        return {
            diskinfo:used,
            flag:exist,
        }
    },
	components:{
		'diskioapp':diskIOApp,
		'cpuusedapp':cpuUsedApp,
		'memoryusedapp':memoryUsedApp,
		'netiocountapp':netIOCountApp,
	},
    // url path is :/profile/js/...
    // eg: bar.js url:/profile/js/chart/bar.js
	created(){
	require.config({
        paths: {
            echarts: './js',    
        }
    });
    require(
        [    // 依赖项列表
            'echarts',
            'echarts/chart/bar',
            'echarts/chart/line',
            'echarts/chart/map'
        ],
        function (ec) {
        	// profileFunction.cpuUsed(ec);
            //--- 折柱 ---
            var weChart = ec.init(document.getElementById('cpuUsed'));
            weChart.setOption({
                title : {
                    text: '年降雨量和蒸发量',
                    subtext: '纯属虚构'
                },
                tooltip : {
                    trigger: 'axis'
                },
                legend: {
                    data:['蒸发量','降水量']
                },
                toolbox: {
                    show : true,
                    feature : {
                        // mark : {show: true},
                        // dataView : {show: true, readOnly: false},
                        magicType : {show: true, type: ['line', 'bar']},
                        restore : {show: true},
                        saveAsImage : {show: true}
                    }
                },
                calculable : true,
                xAxis : [
                    {
                        type : 'category',
                        data : ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
                    }
                ],
                yAxis : [
                    {
                        type : 'value',
                        splitArea : {show : true}
                    }
                ],
                series : [
                    {
                        name:'蒸发量',
                        type:'bar',
                        data:[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
                    },
                    {
                        name:'降水量',
                        type:'bar',
                        data:[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
                    }
                ]
            });
            
            // --- 地图 ---
            // var weChart2 = ec.init(document.getElementById('memoryUsed'));
            // weChart2.setOption({
            //     tooltip : {
            //         trigger: 'item',
            //         formatter: '{b}'
            //     },
            //     series : [
            //         {
            //             name: '中国',
            //             type: 'map',
            //             mapType: 'china',
            //             selectedMode : 'multiple',
            //             itemStyle:{
            //                 normal:{label:{show:true}},
            //                 emphasis:{label:{show:true}}
            //             },
            //             data:[
            //                 {name:'广东',selected:true}
            //             ]
            //         }
            //     ]
            // });
        }
    );
    },
}
let root = new Vue({
    el:'#profileapp',
    template:`<profileapp></profileapp>`,
    components:{
        'profileapp':profileapp
    },
})


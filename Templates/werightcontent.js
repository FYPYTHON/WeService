/*
created:2019/3/29
Author :ljf2010_2010@126.com
*/
"use strict";
var user_edit_png = "css/img/user_edit.png";
var trash_png = "css/img/trash.png";

let rightContent = {
	template:`
	<div class="right-content">
		<h2>{{title}}</h2>
		<table id="rounded-corner">
			<thead>
				<tr>
					<th scope="col" class="rounded-company"></th>
					<th scope="col" class="rounded">Product</th>
					<th scope="col" class="rounded">Details</th>
					<th scope="col" class="rounded">Price</th>
					<th scope="col" class="rounded">Date</th>
					<th scope="col" class="rounded">Edit</th>
					<th scope="col" class="rounded-q4">Delete</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td><input type="checkbox" name="" /></td>
					<td>Apple</td>
					<td>apples red 1kg</td>
					<td>$50</td>
					<td>18/04/20</td>
					<td><a href="#"><img :src="user_edit_png" alt="Edit" /></a></td>
					<td><a href="#" class="ask"><img :src="trash_png" /></a></td>
				</tr>
				<tr>
					<td><input type="checkbox" name="" /></td>
					<td>Apple</td>
					<td>apples red 1kg</td>
					<td>$50</td>
					<td>18/04/20</td>
					<td><a href="#"><img :src="user_edit_png" alt="Edit" /></a></td>
					<td><a href="#" class="ask"><img :src="trash_png" /></a></td>
				</tr>
			</tbody>
			<tfoot>
				<tr>
					<td colspan="6" class="rounded-foot-left">
						<em>tfoot something to describe the tabel</em>
					</td>
					<td class="rounded-foot-left">&nbsp;</td>
				</tr>
			</tfoot>
		</table>
		<el-pagination
		    @size-change="handleSizeChange"
	        @current-change="handleCurrentChange"
	        :current-page="currentPage"
	        :page-sizes="[15, 30, 50, 100]"
	        :page-size="pageSize"
	        layout="total, sizes, prev, pager, next, jumper"
	        :total="currentTotal">
    	</el-pagination>
	</div>
	`,
	data:function(){
		return{
			title:"We Service Table",
			user_edit_png: user_edit_png,
			trash_png: trash_png,
			currentPage:0,
			pageSize:10,
			currentTotal:10,
		}
	},
	components:{
		'el-pagination':el_pagination,
	},
	methods:{
		handleSizeChange(val){    // 每页
			this.pageSize = val;
		},
		handleCurrentChange(val){ // 当前页
			this.currentPage = val;
		},
	}
}
let rightForm = {
	template:`
	<div>
	<h2>right Form</h2>
	</div>
	`,
}
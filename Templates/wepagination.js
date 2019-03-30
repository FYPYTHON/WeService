/*
created:2019/3/30
Author :ljf2010_2010@126.com
*/
let paper = {
    template:`
    <ul @click="onPagerClick($event)" class="el-pager">
      <li :class="{ active: currentPage === 1 }" v-if="pageCount > 0" class="number">1</li>
      <li class="ellipsis btn-quickprev" v-if="showPrevMore"></li>
      <li v-for="pager in pagers" :class="{ active: $parent.currentPage === pager }" class="number">{{ pager }}</li>
      <li class="ellipsis btn-quicknext" v-if="showNextMore"></li>
      <li :class="{ active: currentPage === pageCount }" class="number" v-if="pageCount > 1">{{ pageCount }}</li>
    </ul>
    `,
    name:'ELPager',
    props:{
      currentPage: {
        type: Number
      },

      pageCount: {
        type: Number
      }
    },  // props

    methods:{
      onPagerClick(event) {
        const target = event.target;
        if (target.tagName === 'UL') {
          return;
        }
        let newPage = Number(event.target.textContent);
        const pageCount = this.pageCount;
        const currentPage = this.currentPage;
        if (target.className.indexOf('ellipsis') !== -1) {
          if (target.className.indexOf('quickprev') !== -1) {
            newPage = currentPage - 5;
          } else if (target.className.indexOf('quicknext') !== -1) {
            newPage = currentPage + 5;
          }
        }
        if (!isNaN(newPage)) {
          if (newPage < 1) {
            newPage = 1;
          }
          if (newPage > pageCount) {
            newPage = pageCount;
          }
        }
        this.currentPage = newPage;
        if (newPage !== currentPage) {
          this.$parent.$emit('current-change', newPage);
        }
      }
    }, // paper methods
    // paper compute
    computed: {
      pagers() {
        const pagerCount = 7;
        const currentPage = Number(this.currentPage);
        const pageCount = Number(this.pageCount);
        let showPrevMore = false;
        let showNextMore = false;
        if (pageCount > pagerCount) {

          if (currentPage > pagerCount - 2) {

            showPrevMore = true;

          }
          if (currentPage < pageCount - 2) {

            showNextMore = true;

          }

        }
        const array = [];
        if (showPrevMore && !showNextMore) {
          for (let i = pageCount - pagerCount; i < pageCount; i++) {
            array.push(i);
          }
        } else if (!showPrevMore && showNextMore) {
          for (let i = 2; i < pagerCount; i++) {
            array.push(i);
          }
        } else if (showPrevMore && showNextMore) {
          const offset = Math.floor(pagerCount / 2) - 1;
          for (let i = currentPage - offset ; i <= currentPage + offset; i++) {
            array.push(i);
          }
        } else {
          for (let i = 2; i < pageCount; i++) {
            array.push(i);
          }

        }
        this.showPrevMore = showPrevMore;
        this.showNextMore = showNextMore;
        return array;
      }
    },
    // paper computed
    data() {
        return {
          current: null,
          showPrevMore: false,
          showNextMore: false
        }
    },
  } // Paper

var TEMPLATE_MAP = {
    prev: '<span is="prev"></span>',
    jumper: '<span is="jumper"></span>',
    pager: '<span is="pager" :current-page.sync="currentPage" :page-count.sync="pageCount"></span>',
    next: '<span is="next"></span>',
    sizes: '<span is="sizes"></span>',
    slot: '<slot></slot>',
    total: '<span is="total"></span>'
};
let el_pagination = {
    template:`
    <div class="el-pagination">
    </div>
    `,
    props:{
      pageSize:{
        type:Number,
        default:10,
      },
      total:{
        type:Number,
        default:0,
      },
      currentPage:{
        type:Number,
        default:1
      },
      layout:{
        default:'prev,pager,next,jumper,slot,->,total'
      },
      pageSizes:{
        type:Array,
        default(){
          return [10,20,30,40,50,100];
        }
      }
    },
    components:{
      Prev: {
        template: '<button class="btn-prev" :class="{ disabled: $parent.currentPage <= 1 }" @click="$parent.prev()"></button>'
      },
      Next: {
        template: '<button class="btn-next" @click="$parent.next()" :class="{ disabled: $parent.currentPage === $parent.pageCount }"></button>'
      },
      Sizes: {
        template: '<select v-model="$parent.pageSize"><option v-for="item in $parent.pageSizes" value="item">{{item}}</option></select>'
      },
      Jumper: {
        data() {
          return {
            oldValue: null
          };
        },
        methods: {
          handleFocus(event) {
            this.oldValue = event.target.value;
          },
          handleChange(event) {
            const target = event.target;
            if (target.value !== this.oldValue && Number(target.value) === this.$parent.currentPage) {
              this.$parent.$emit('current-change', this.$parent.currentPage);
            }
            this.oldValue = null;
          }
        },
        template: `<span>前往<input class="el-pagination-editor"
                  v-model="$parent.currentPage"
                  @change="handleChange($event)"
                  @focus="handleFocus($event)" style="width: 30px;" number lazy />
                  页</span>`,
      },
      Total: {
        template: '<span class="el-pagination-total">共 {{$parent.total}} 条</span>'
      },
      Pager:paper,
    },
    // methods
    methods: {
      prev() {
        const oldPage = this.currentPage;
        const newVal = this.currentPage - 1;
        this.currentPage = this.getValidCurrentPage(newVal);
        if (this.currentPage !== oldPage) {
          this.$emit('current-change', this.currentPage);
        }
      },
      next() {
        const oldPage = this.currentPage;
        const newVal = this.currentPage + 1;
        this.currentPage = this.getValidCurrentPage(newVal);
        if (this.currentPage !== oldPage) {
          this.$emit('current-change', this.currentPage);
        }
      },
      first() {
        const oldPage = this.currentPage;
        const newVal = 1;
        this.currentPage = this.getValidCurrentPage(newVal);
        if (this.currentPage !== oldPage) {
          this.$emit('current-change', this.currentPage);
        }
      },
      last() {
        const oldPage = this.currentPage;
        const newVal = this.pageCount;
        this.currentPage = this.getValidCurrentPage(newVal);
        if (this.currentPage !== oldPage) {
          this.$emit('current-change', this.currentPage);
        }
      },
      getValidCurrentPage(value) {
        value = parseInt(value, 10);
        var resetValue;
        if (value < 1) {
          resetValue = this.pageCount > 0 ? 1 : 0;
        } else if (value > this.pageCount) {
          resetValue = this.pageCount;
        }
        if (resetValue === undefined && isNaN(value)) {
          value = this.pageCount > 0 ? 1 : 0;
        }
        return resetValue === undefined ? value : resetValue;
      }
    },
    // created ...
    created() {
      this.$options._linkerCachable = false;
      let template = '<div class="el-pagination">';
      const layout = this.$options.layout || this.layout || '';
      const components = layout.split(',').map((item) => item.trim());
      let haveRightWrapper = false;
      components.forEach((component) => {
        if (component === '->') {
          haveRightWrapper = true;
          template += '<div class="el-pagination-rightwrapper">';
        } else {
          if (!TEMPLATE_MAP[component]) {
            console.warn('layout component not resolved:' + component);
          }
          template += TEMPLATE_MAP[component] || '';
        }
      });
      if (haveRightWrapper) {
        template += '</div>';
      }
      template += '</div>';
      this.$options.template = template;
    },
    // computed ...
    computed: {
      pageCount() {
        return Math.ceil(this.total / this.pageSize);
      },
      startRecordIndex() {
        const result = (this.currentPage - 1) * this.pageSize + 1;
        return result > 0 ? result : 0;
      },
      endRecordIndex() {
        const result = this.currentPage * this.pageSize;
        return result > this.total ? this.total : result;
      }
    },
    // watch
    watch: {
      pageCount(newVal) {
        if (newVal > 0 && this.currentPage === 0) {
          this.currentPage = 1;
        } else if (this.currentPage > newVal) {
          this.currentPage = newVal;
        }
      },
      currentPage(newVal, oldVal) {
        newVal = parseInt(newVal, 10);
        if (isNaN(newVal)) {
          newVal = oldVal || 1;
        } else {
          newVal = this.getValidCurrentPage(newVal);
        }
        if (newVal !== undefined) {
          Vue.nextTick(() => {
            this.currentPage = newVal;
          });
        }
      },
      ready() {
        this.currentPage = this.getValidCurrentPage(this.currentPage);
      }
    },
    // ready
}
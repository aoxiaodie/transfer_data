<template>
  <body>
    <div id="app">
      <el-container>
        <el-header>数据反推工具</el-header>
        <el-container>
          <!-- 顶部 -->
          <el-aside width="200px" style="text-align: left;">
            <el-menu default-active="2" router class="el-menu-vertical-demo">
              <el-menu-item index="/index">
              	<i class="el-icon-menu"></i>
              	<span slot="title">主页</span>
              </el-menu-item>
              <el-menu-item index="/dbInfo">
                <i class="el-icon-menu"></i>
                <span slot="title">数据库管理</span>
              </el-menu-item>
              <el-menu-item index="/tableInfo">
                <i class="el-icon-menu"></i>
                <span slot="title">创建库操作</span>
              </el-menu-item>
            </el-menu>
          </el-aside>
          <el-container>
            <!-- 主体 -->
            <el-main>
              <!-- 查询 -->
              <el-form :inline="true" style="margin-top: 10px;">
                <el-row :gutter="20">
                  <el-col :span="15">
                    <el-form-item label="请输入表名：">
                      <el-input v-model="table_name" placeholder="请输入表名"></el-input>
                    </el-form-item>
                    <el-button @click="getTableInfo()">查询</el-button>
                  </el-col>
                  <el-col :span="14">
                  </el-col>
                </el-row>
              </el-form>

              <!-- 表格 -->
              <el-table :data='pageTable' @selection-change="handleSelectionChange" style="width: 100%">
                <el-table-column type="selection">
                </el-table-column>
                <el-table-column type="index">
                </el-table-column>
                <el-table-column prop="table_name" label="表名">
                </el-table-column>
                <el-table-column prop="column_name" label="字段名">
                </el-table-column>
                <el-table-column prop="column_type" label="字段类型">
                </el-table-column>
                <el-table-column prop="column_key" label="属性">
                </el-table-column>
              </el-table>
              <!-- 分页 -->
              <el-row style="margin-top: 10px;">
                <el-col :span="8" style="text-align: left;">
                  <el-button type="primary" @click="insertTable()" size="mini">添加表到源数据库</el-button>
                  <el-button type="primary" @click="dialogFormVisible=true" size="mini">添加数据到源数据库</el-button>
                </el-col>
                <el-col :span="16" style="text-align: right;">
                  <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentpage"
                    :page-sizes="[5, 10, 50, 100]" :page-size="pagesize" layout="total, sizes, prev, pager, next, jumper"
                    :total="total">
                  </el-pagination>
                </el-col>
              </el-row>

              <!-- 脱敏表单 -->
              <el-dialog title="是否需要脱敏" :visible.sync="dialogFormVisible" width="40%">
                <el-button type="primary" @click="insertData(1)">是</el-button>
                <el-button type="infor" @click="insertData(0)" style="margin-left: 30px;">否</el-button>
              </el-dialog>
            </el-main>
            <!-- <el-footer>2020-05-23</el-footer> -->
          </el-container>
        </el-container>
      </el-container>
    </div>
  </body>
</template>

<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        show: true,
        resp: 'error',
        tableInfo: [],
        insertTables: [], // 需要插入的数据
        pageTable: [],
        table_name: '',
        total: 0,
        currentpage: 1,
        pagesize: 10,
        dialogFormVisible: false, // 隐藏弹框
        tag: 0, // 是否需要脱敏，0否，1是
      }
    },


    methods: {
      // 获取表结构
      getTableInfo() {
        // const that = this;
        axios.post("http://127.0.0.1:8000/tableInfo", {
            table_name: this.table_name
          })
          .then((response) => {
            console.log(response)
            if (response.data.error_no === 0) {
              this.tableInfo = response.data.data;
              this.total = response.data.data.length;
              this.getPageTable();
            } else {

            }
          })
          .catch((error) => {
            console.log(error)
          })
      },

      // 实现分页
      getPageTable() {
        this.pageTable = [];
        for (let i = (this.currentpage - 1) * this.pagesize; i < this.total; i++) {
          this.pageTable.push(this.tableInfo[i]);
          if (this.pageTable.length === this.pagesize) break;
        }
      },

      handleSizeChange(size) {
        this.pagesize = size;
        this.getPageTable();
      },

      handleCurrentChange(pageNum) {
        this.currentpage = pageNum;
        this.getPageTable();
      },

      // 实现多选
      handleSelectionChange(data) {
        this.insertTables = data;
        console.log(data);
      },

      // 插入表结构
      insertTable() {
        // this.dialogFormVisible = true;
        // const that = this;
        axios.post("http://127.0.0.1:8000/insertTable", {
            insertTables: this.insertTables
          })
          .then((response) => {
            console.log(response)
            if (response.data.error_no === 0) {
              this.$message({
                message: '创建表结构成功！',
                type: 'success'
              });
            } else {
              this.$message.error('创建表结构失败！');
            }
          })
          .catch((error) => {
            console.log(error)
            this.$message.error(error);
          })
      },

      // 插入表数据
      insertData(tags){
        // const that = this;
        axios.post("http://127.0.0.1:8000/insertData",
        {
          insertTables: this.insertTables,
          tag: tags
        }
        )
          .then((response) => {
            console.log(response)
            if (response.data.error_no === 0) {
              this.dialogFormVisible = false;
              this.$message({
                message: '插入表数据成功！',
                type: 'success'
              });
            } else {
              this.$message.error('插入表数据失败！');
            }
          })
          .catch((error) => {
            console.log(error)
            this.$message.error(error);
          })
      }
    },

    closeForm(formName) {
      this.dialogFormVisible = false;
    },

    mounted() {
      // this.getTableInfo();
    }
  }
</script>

<style>
  body,
  #app,
  .el-container {
    margin: 0px;
    padding: 0px;
    height: 100%;
  }

  .el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: left;
    line-height: 60px;
    font-size: 16px;
  }

  .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;

  }

  body>.el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>

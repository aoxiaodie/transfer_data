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
              <!-- Form -->
              <el-row :gutter="0">
                <el-col :span="15" style="text-align: left;">
                  <el-button @click="dialogFormVisible = true">添加数据库</el-button>
                </el-col>
              </el-row>
              <!-- 表单 -->
              <el-dialog title="添加数据库" :visible.sync="dialogFormVisible" width="40%">
                <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px">
                  <el-form-item label="是否为源库">
                    <el-select v-model="ruleForm.tag" placeholder="请选择">
                      <el-option label="是" value="0"></el-option>
                      <el-option label="否" value="1"></el-option>
                    </el-select>
                  </el-form-item>
                  <el-form-item label="IP地址" prop="ip">
                    <el-input v-model="ruleForm.ip"></el-input>
                  </el-form-item>
                  <el-form-item label="端口" prop="post">
                    <el-input v-model="ruleForm.post"></el-input>
                  </el-form-item>
                  <el-form-item label="用户名" prop="user">
                    <el-input v-model="ruleForm.user"></el-input>
                  </el-form-item>
                  <el-form-item label="密码" prop="password">
                    <el-input v-model="ruleForm.password"></el-input>
                  </el-form-item>
                  <el-form-item label="数据库名" prop="data">
                    <el-input v-model="ruleForm.data"></el-input>
                  </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button type="infor" @click="closeForm('ruleForm')">取 消</el-button>
                  <el-button type="primary" @click="submitForm('ruleForm')">确 定</el-button>
                </div>
              </el-dialog>

              <!-- 表格 -->
              <el-table :data='db' style="width: 100%; margin-top: 20px;">
                <el-table-column prop="tag" label="是否为源库">
                </el-table-column>
                <el-table-column prop="ip" label="IP地址">
                </el-table-column>
                <el-table-column prop="post" label="端口">
                </el-table-column>
                <el-table-column prop="user" label="用户名">
                </el-table-column>
                <el-table-column prop="password" label="密码">
                </el-table-column>
                <el-table-column prop="data" label="数据库名">
                </el-table-column>
              </el-table>
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
        db: [],

        dialogFormVisible: false, // 隐藏弹框
        ruleForm: { // 表单的默认展示
          ip: '',
          post: '',
          user: '',
          password: '',
          data: ''
        },
        rules: {
          ip: [{
            required: true,
            message: '请输入IP地址',
            trigger: 'blur'
          }],
          post: [{
            required: true,
            message: '请输入端口',
            trigger: 'blur'
          }],
          user: [{
            required: true,
            message: '请输入用户',
            trigger: 'blur'
          }],
          password: [{
            required: true,
            message: '请输入密码',
            trigger: 'blur'
          }],
          data: [{
            required: true,
            message: '请输入数据库名',
            trigger: 'blur'
          }]
        }
      }
    },

    methods: {
      getDbInfo() {
        // const that = this;
        axios.get('http://127.0.0.1:8000/dbInfo')
          .then((response) =>  {
            if (response.data.error_no === 0) {
              this.db = response.data.data;
              console.log(response);
            }
            // that.obj.push(response.data[0].fields);
          })
          .catch((error) => {
            console.log(error)
          })
      },

      // 添加信息
      addDbInfo() {
        // let that = this;
        axios.post('http://127.0.0.1:8000/addInfo', this.ruleForm)
          .then((response) => {
            debugger;
            if (response.data.error_no === 0) {
              this.getDbInfo();
              this.closeForm('ruleForm');
            }
          })
          .catch((error) => {
            console.log(error)
          })
      },

      // 表单提交
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.addDbInfo();
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      // 关闭
      closeForm(formName) {
        this.$refs[formName].resetFields();
        this.ruleForm.ip = '';
        this.ruleForm.post = '';
        this.ruleForm.user = '';
        this.ruleForm.password = '';
        this.ruleForm.data = '';
        this.dialogFormVisible = false;
      }
    },

    mounted() {
      this.getDbInfo();
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

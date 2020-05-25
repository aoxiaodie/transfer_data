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

              <div>
                <span>
                  <p align="left"><strong>数据反推工具transfer_data_202005.01.000</strong></p>
                </span>
                <el-divider></el-divider>
                <span>
                  <p align="left">
                    <strong>功能支持：</strong>
                    </br>
                    1、支持添加数据库信息；
                    </br>
                    2、支持通过表名模糊搜索源数据库里的表信息，包括表名、列名和属性；
                    </br>
                    3、支持批量选择查询到的列并在目标库建表；
                    </br>
                    4、支持将对应列的所有数据插入目标库的新表中，并可配置是否脱敏；
                    </br>
                    <strong>存在问题：</strong>
                    </br>
                    1、只能新增两个数据库信息，一个源库一个目标库；
                    </br>
                    2、数据库信息未做修改、删除和测试连接功能；
                    </br>
                    3、批量选择数据导入表结构后未做控制不能多选；
                    </br>
                    4、前台仍有一些校验待优化。
                  </p>
                </span>
              </div>

            </el-main>
            <!-- <el-footer>2020-05-23</el-footer> -->
          </el-container>
        </el-container>
      </el-container>
    </div>
  </body>
</template>

<script>
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

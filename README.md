项目名称：staff_n1

应用名称：staff

### 9.9记录

1. 创建应用

2. 网页结构设计：

   > **用户组：**
   > - HC管理员(hc_admin)
   > - 部门HC管理员(hc_g1\hc_g2\hc_art\hc_plat)

   > **页面包含:**
   > - **首页**（上导航）
   > - **员工信息查看**查看自己有权限的人员整体信息 *（使用带排序搜索表格）*
   > - **统计-投入游戏占比查看** *(使用引用更多信息的表格)*
   > - **录入-入职离职**（可编辑表格）
   > - **录入-HC调整**
   > - **录入-工作投入**l（填写工时）

3. 数据结构设计：

   > **dept**部门表
   > - deptcode 部门编码（主键）
   > - deptname 部门名称
   
   > **jobtype** 岗位名称表
   > - jobcode 岗位编码（主键）
   > - jobname 岗位名称
   > - jobtypename 岗位类型（策划/运营/程序/项管）
   
   > **game** 游戏名称
   > - gamecode 项目编码（主键）
   > - gamename 项目名称（公共/小程序/频道/五指间…）
   
   > **staff:**
   > - scode 编码(主键)
   > - sname 姓名（*待招姓名统一用岗位名称*）
   > - jobname 岗位名称（外健）
   > - stafftype 员工类型（正职/实习生/外包/内包/基地）
   > - staffstatus 员工状态（在职/待招/offer中）
   > - sdept 部门编码（外健）
   > - sproduct 产品线（Z1/N1）
   > - stafflevel 职级
   
   > **projectwork:**工作月份投入表
   > - sname 姓名（外健）
   > - gamename 项目名称（外健）
   > - workpercent 投入占比
   > - month 月份
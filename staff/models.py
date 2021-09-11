from django.db import models

# Create your models here.
class dept(models.Model):
    deptcode = models.CharField(max_length=10, unique=True, primary_key=True)
    deptname = models.CharField(max_length=20, null=True, verbose_name="部门名称")

    def __str__(self):
        return self.deptname


class jobtype(models.Model):
    job_type = models.TextChoices('jobtype', '策划 运营 程序 美术 项管')
    jobcode = models.CharField(max_length=10, unique=True, primary_key=True)
    jobname = models.CharField(max_length=50, unique=True, verbose_name="岗位名称")
    jobtypename = models.CharField(choices=job_type.choices, max_length=10, verbose_name='岗位类型')

    def __str__(self):
        return self.jobname

class game(models.Model):
    gamecode = models.CharField(max_length=10, unique=True, primary_key=True)
    gamename = models.CharField(max_length=50, unique=True, verbose_name="游戏名称")

    def __str__(self):
        return  self.gamename

class staff(models.Model):
    staff_type = models.TextChoices('stafftype', '正职 实习生 外包 内包 基地')
    stuff_status = models.TextChoices('staffstatus', '在职 待招')
    stuff_product = models.TextChoices('staffproduct', 'Z1 N1')
    scode = models.CharField(max_length=10, unique=True, primary_key=True, verbose_name="编码")
    sname = models.CharField(max_length=20, unique=True, verbose_name="姓名")
    jobname = models.ForeignKey(jobtype, on_delete=models.CASCADE, verbose_name="岗位名称")
    stafftype = models.CharField(choices=staff_type.choices, max_length=20, verbose_name='员工类型')
    stuffstatus = models.CharField(choices=stuff_status.choices, max_length=10, verbose_name="员工状态")
    sdept = models.ForeignKey(dept, on_delete=models.CASCADE, verbose_name="所在部门")
    sproduct = models.CharField(choices=stuff_product.choices, max_length=10,  verbose_name="产品线")
    stafflevel = models.CharField(max_length=50, verbose_name="专业职级")

    def __str__(self):
        return self.sname
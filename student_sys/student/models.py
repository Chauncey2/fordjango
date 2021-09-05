from django.db import models


# Create your models here.
class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知')
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝')
    ]
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="电子邮件")
    phone = models.CharField(max_length=128, verbose_name="电话")
    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name="审核状态")
    create_time = models.DateTimeField(max_length=128, verbose_name="创建时间", auto_now=True)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return f"<Student:{self.name}>"

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"

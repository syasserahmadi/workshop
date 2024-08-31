from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User



# Table for newcuts
class cuts(models.Model):
    cut = models.CharField(max_length=200, null=False, verbose_name="برش")
    customcode = models.IntegerField(validators=[MinValueValidator(0)], unique=True, blank=True, null=True, verbose_name="کد دلخواه")
    weight = models.DecimalField(validators=[MinValueValidator(0.1)], max_digits=12, decimal_places=3, null=False, verbose_name="ورن")
    colortype = models.CharField(max_length=8, null=False, verbose_name="نوع رنگ")
    sizetype = models.CharField(max_length=8, null=False, verbose_name="نوع سایز")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    cdate = models.DateTimeField(null=False, auto_now_add=True, verbose_name="تاریخ ایجاد")
    edate = models.DateTimeField(null=True, auto_now=True, verbose_name="تاریخ تصحیح")
    completed = models.BooleanField(default=False, verbose_name="تکمیل شده؟")

    class Meta:
        verbose_name = "برش"
        verbose_name_plural = "برش‌ها"

    def __str__(self):
        return f"{self.cut}: {self.id}"



# Table for sizes
class sizes(models.Model):
    size = models.CharField(max_length=5, null=False, verbose_name="سایز")
    amount = models.IntegerField(validators=[MinValueValidator(0)], null=False, verbose_name="تعداد")
    cut = models.ForeignKey(cuts, on_delete=models.CASCADE, null=False, verbose_name="برش")
    completed = models.BooleanField(default=False, verbose_name="تکمیل شده؟")

    class Meta:
        verbose_name = "سایز"
        verbose_name_plural = "سایزها"

    def __str__(self):
        return f"{self.size}: برش {self.cut.id}"



# Table for colors
class colors(models.Model):
    color = models.CharField(max_length=20, null=False, verbose_name="رنگ")
    amount = models.IntegerField(validators=[MinValueValidator(0)], null=False, verbose_name="تعداد")
    size = models.ForeignKey(sizes, on_delete=models.CASCADE, null=False, verbose_name="سایز")
    cut = models.ForeignKey(cuts, on_delete=models.CASCADE, null=False, verbose_name="برش")
    completed = models.BooleanField(default=False, verbose_name="تکمیل شده؟")


    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ‌ها"

    def __str__(self):
        return f"{self.color}: برش {self.cut.id}"

    
    
# Table for lines
class lines(models.Model):
    line = models.CharField(max_length=32, null=False, verbose_name="خط دوخت")
    price = models.IntegerField(validators=[MinValueValidator(0)], null=True, verbose_name="قیمت")
    color = models.ForeignKey(colors, on_delete=models.CASCADE, null=False, verbose_name="رنگ")
    size = models.ForeignKey(sizes, on_delete=models.CASCADE, null=False, verbose_name="سایز")
    cut = models.ForeignKey(cuts, on_delete=models.CASCADE, null=False, verbose_name="برش")
    completed = models.BooleanField(default=False, verbose_name="تکمیل شده؟")

    class Meta:
        verbose_name = "خط"
        verbose_name_plural = "خط‌ها"

    def __str__(self):
        return f"{self.line}: برش {self.cut.id}"
    


# Table for amounts
class amounts(models.Model):
    cut = models.OneToOneField(cuts, on_delete=models.CASCADE, null=False, verbose_name="برش")
    totalcolors = models.IntegerField(validators=[MinValueValidator(0)], null=True, verbose_name="تعداد رنگ")
    totalsizes = models.IntegerField(validators=[MinValueValidator(0)], null=True, verbose_name="تعداد سایز")
    totallines = models.IntegerField(validators=[MinValueValidator(0)], null=True, verbose_name="تعداد خط")

    class Meta:
        verbose_name = "تعداد"
        verbose_name_plural = "تعدادها"

    def __str__(self):
        return f"{self.cut}"



class jobs(models.Model):
    cut = models.ForeignKey(cuts, on_delete=models.CASCADE, null=False, verbose_name="برش")
    size = models.ForeignKey(sizes, on_delete=models.CASCADE, null=False, verbose_name="سایز")
    color = models.ForeignKey(colors, on_delete=models.CASCADE, null=False, verbose_name="رنگ")
    line = models.ForeignKey(lines, on_delete=models.CASCADE, null=False, verbose_name="خط دوخت")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name="دوزنده")
    cdate = models.DateTimeField(null=False, auto_now_add=True, verbose_name="تاریخ ایجاد")
    edate = models.DateTimeField(null=True, auto_now=True, verbose_name="تاریخ تصحیح")
    completed = models.BooleanField(default=False, verbose_name="تکمیل شده؟")

    class Meta:
        verbose_name = "کار"
        verbose_name_plural = "کارها"

    def __str__(self):
        return f"{self.cut}"
    
    
from . import signals
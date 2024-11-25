from django.db import models

class DepositProducts(models.Model):
        fin_prdt_cd = models.TextField()
        kor_co_nm = models.TextField()
        fin_prdt_nm = models.TextField()
        mtrt_int = models.TextField()
        spcl_cnd = models.TextField()
        etc_note = models.TextField()

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    intr_rate = models.FloatField(null=True, blank=True)
    intr_rate2 = models.FloatField(null=True, blank=True)
    save_trm = models.IntegerField()

class SavingProducts(models.Model):
        fin_prdt_cd = models.TextField()
        kor_co_nm = models.TextField()
        fin_prdt_nm = models.TextField()
        mtrt_int = models.TextField()
        spcl_cnd = models.TextField()
        etc_note = models.TextField()

class EtfProducts(models.Model):
        itmsNm = models.TextField()
        fltRt = models.FloatField()
        trqu = models.IntegerField()
        bssIdxIdxNm = models.TextField()
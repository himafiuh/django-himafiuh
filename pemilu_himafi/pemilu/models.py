from django.db import models
import random
# Create your models here.

class DataPemilih(models.Model):
    nama = models.CharField(max_length=50)
    nik = models.CharField(max_length=17, unique=True)
    nim = models.CharField(max_length=11, unique=True)
    tanggal_lahir= models.DateField()
    angkatan = models.CharField(max_length=5)
    password = models.CharField(
    max_length=6,
    editable=True)

    def __str__(self):
        return self.nama

class PilihanPemilih(models.Model):
    data_peserta_pilih = models.ForeignKey(DataPemilih, on_delete=models.CASCADE)
    pilihan = models.CharField(max_length=1)

    def __str__(self):
        return data_peserta_pilih.nama

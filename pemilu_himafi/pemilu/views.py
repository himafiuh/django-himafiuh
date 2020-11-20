from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import StreamingHttpResponse
from pemilu import models
import random
# Create your views here.

def form_pendaftaran_pemilu_view(request):
    return render(request, 'pemilu/Pendaftaran_Pemilih.html')

def form_pemilihan(request):
    return render(request, 'pemilu/form_pemilihan.html')

def sukses_mendaftar(request):
    return render(request, 'pemilu/result_daftar.html')

def sukses_memilih(request):
    return render(request, 'pemilu/result_pemilihan.html')

def gagal_input(request):
    return render(request, 'pemilu/failed_input.html')

def input_data_peserta_pemilu(request):
    if request.is_ajax():
        nama = request.POST.get('nama', None)
        nik = request.POST.get('nik', None)
        nim = request.POST.get('nim', None)
        tanggal_lahir = request.POST.get('tanggal_lahir', None)
        angkatan = request.POST.get('angkatan', None)
        pwd = create_random_number()
        try:
            data = models.DataPemilih(
            nama=nama,
            nik=nik,
            nim=nim,
            tanggal_lahir=tanggal_lahir,
            angkatan=angkatan,
            password= pwd)
            data.save()
            response = {
                'pesan' : pwd
            }
            return JsonResponse(response)
        except :
            response = {
                'pesan' : "Data Yang dimasukkan Telah Tersimpan pada DataBase. Silahkan Masukkan Data Yang lain"
            }
            return JsonResponse(response)

def create_random_number():
    return str(random.randint(100000,999999))

from django.urls import path
from pemilu import views

app_name = 'dashboard'

urlpatterns = [
    path('pendaftaran/', views.form_pendaftaran_pemilu_view, name="form pendaftaran"),
    path('pendaftaran/ajax-get-pendaftaran/', views.input_data_peserta_pemilu, name='input_data_peserta_pemilu'),
    path('berhasil-daftar/', views.sukses_mendaftar, name='berhasil mendaftar'),
    path('berhasil-pilih/', views.sukses_memilih, name='berhasil memilih'),
    path('pemilihan/', views.form_pemilihan, name='form pemilihan'),
    path('gagal/', views.gagal_input, name='gagal'),
]

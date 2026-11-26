# Analisis Faktor Adopsi Telemedicine dengan Regresi Linear Berganda

Analisis pengaruh **Digital Health Literacy**, **Self-Efficacy**, dan **Perceived Benefit** terhadap **Adoption Telemedicine** menggunakan regresi linear berganda di **Jamovi**, disusun dalam format artikel jurnal.

Penulis: **Zidnia Ilma Arifa** dan Syahiduz Zaman, M.Kom.
Program Studi Teknik Informatika, UIN Maulana Malik Ibrahim Malang (2026).

> **Catatan:** analisis ini memakai **data simulasi** sebanyak 100 responden sebagai latihan prosedur analisis. Hasilnya tidak mewakili populasi nyata.

## Isi Repositori

| File | Isi |
|---|---|
| `artikel.pdf` | Artikel lengkap: pendahuluan, metode, hasil, pembahasan, dan daftar pustaka |
| `kerangka-pemikiran.png` | Gambar kerangka pemikiran penelitian |

## Pertanyaan Penelitian

Apakah kemampuan literasi kesehatan digital, keyakinan diri, dan manfaat yang dirasakan berhubungan dengan niat seseorang menggunakan telemedicine?

| Hipotesis | Pernyataan |
|---|---|
| H1 | Digital Health Literacy berpengaruh positif terhadap Adoption Telemedicine |
| H2 | Self-Efficacy berpengaruh positif terhadap Adoption Telemedicine |
| H3 | Perceived Benefit berpengaruh positif terhadap Adoption Telemedicine |
| H4 | Ketiga variabel secara simultan berhubungan dengan Adoption Telemedicine |

![Kerangka pemikiran](kerangka-pemikiran.png)

## Metode

| Aspek | Keterangan |
|---|---|
| Pendekatan | Kuantitatif, regresi linear berganda |
| Data | Data simulasi, 100 responden |
| Instrumen | 20 pernyataan skala Likert 1–5 (5 pernyataan per variabel) |
| Variabel | X1 Digital Health Literacy, X2 Self-Efficacy, X3 Perceived Benefit, Y Adoption Telemedicine |
| Alat analisis | Jamovi |
| Model | Y = a + b1X1 + b2X2 + b3X3 + e |

## Hasil

**Ringkasan model**

| Ukuran | Nilai |
|---|---|
| N | 100 |
| R | 0,653 |
| R² | 0,427 |

Model menjelaskan **42,7%** variasi skor Adoption Telemedicine.

**Koefisien regresi**

| Prediktor | Estimate (B) | SE | t | p | Keterangan |
|---|---|---|---|---|---|
| Intercept | 0,274 | 0,3409 | 0,805 | 0,423 | Tidak signifikan |
| Digital Health Literacy (X1) | 0,442 | 0,0822 | 5,375 | < 0,001 | Positif, signifikan |
| Self-Efficacy (X2) | 0,241 | 0,0835 | 2,886 | 0,005 | Positif, signifikan |
| Perceived Benefit (X3) | 0,227 | 0,0825 | 2,751 | 0,007 | Positif, signifikan |

**Persamaan regresi**

```
Y = 0,274 + 0,442 X1 + 0,241 X2 + 0,227 X3
```

## Interpretasi

- **Digital Health Literacy** memiliki koefisien terbesar: setiap kenaikan satu unit skor literasi kesehatan digital berkaitan dengan kenaikan 0,442 unit prediksi skor adopsi, dengan variabel lain dianggap tetap.
- **Self-Efficacy** dan **Perceived Benefit** juga berkoefisien positif dan signifikan (p < 0,05).
- Bagi penyedia layanan telemedicine, hasil ini mengarah ke tiga area evaluasi: edukasi penggunaan, antarmuka yang mudah dipahami, dan penyampaian manfaat layanan.

## Keterbatasan dan Pengembangan

- Data bersifat simulasi, sehingga koefisien dan signifikansi belum mewakili responden nyata.
- Uji F, multikolinearitas (VIF), normalitas residual, linearitas, dan homoskedastisitas belum dilaporkan.
- Validitas dan reliabilitas instrumen belum diuji.
- Penelitian lanjutan perlu memakai data responden sebenarnya beserta teknik sampling yang jelas.

## Teknologi

`Jamovi` · `Regresi Linear Berganda` · `Statistik Inferensial` · `Skala Likert`

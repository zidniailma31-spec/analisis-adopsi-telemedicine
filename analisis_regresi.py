"""
Analisis Faktor Adopsi Telemedicine dengan Regresi Linear Berganda
Zidnia Ilma Arifa - Teknik Informatika UIN Maulana Malik Ibrahim Malang

Skrip ini melengkapi analisis Jamovi dengan uji yang belum dilaporkan di artikel:
  1. Uji validitas item (korelasi item-total terkoreksi)
  2. Uji reliabilitas (Cronbach's alpha)
  3. Regresi linear berganda: koefisien, uji t, R², adjusted R², uji F
  4. Uji asumsi klasik: multikolinearitas (VIF), normalitas residual
     (Shapiro-Wilk), dan homoskedastisitas (Breusch-Pagan)

Input  : file CSV dengan kolom seperti template-data.csv
         (responden, DHL1..DHL5, SE1..SE5, PB1..PB5, AT1..AT5; skor Likert 1-5)
Cara   : python analisis_regresi.py data.csv
"""
import sys

import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor

VARIABEL = {
    "DHL": "Digital Health Literacy (X1)",
    "SE": "Self-Efficacy (X2)",
    "PB": "Perceived Benefit (X3)",
    "AT": "Adoption Telemedicine (Y)",
}
ALPHA = 0.05


def cronbach_alpha(items: pd.DataFrame) -> float:
    k = items.shape[1]
    return k / (k - 1) * (1 - items.var(ddof=1).sum() / items.sum(axis=1).var(ddof=1))


def main(path: str) -> None:
    df = pd.read_csv(path)
    kolom = [f"{p}{i}" for p in VARIABEL for i in range(1, 6)]
    hilang = [c for c in kolom if c not in df.columns]
    if hilang:
        sys.exit(f"Kolom tidak ditemukan: {hilang}")
    df = df.dropna(subset=kolom)
    n = len(df)
    if n < 10:
        sys.exit(f"Data baru {n} responden. Isi data responden terlebih dahulu (minimal 10, disarankan ≥ 100).")
    print(f"Jumlah responden: {n}\n")

    # ---------- 1-2. Validitas dan reliabilitas ----------
    print("=" * 70)
    print("UJI VALIDITAS (korelasi item-total terkoreksi) DAN RELIABILITAS")
    print("=" * 70)
    r_tabel = None
    if n > 2:
        t_kritis = stats.t.ppf(1 - ALPHA / 2, n - 2)
        r_tabel = t_kritis / (t_kritis**2 + n - 2) ** 0.5
        print(f"r tabel (alpha 0,05; df = {n - 2}) = {r_tabel:.3f}\n")
    for p, nama in VARIABEL.items():
        items = df[[f"{p}{i}" for i in range(1, 6)]]
        print(nama)
        for c in items.columns:
            r = items[c].corr(items.drop(columns=c).sum(axis=1))
            ket = "" if r_tabel is None else ("valid" if r > r_tabel else "TIDAK valid")
            print(f"  {c:<5} r = {r:6.3f}  {ket}")
        a = cronbach_alpha(items)
        print(f"  Cronbach's alpha = {a:.3f} ({'reliabel' if a >= 0.70 else 'kurang reliabel'}, batas 0,70)\n")

    # ---------- skor variabel = rata-rata item ----------
    skor = pd.DataFrame({p: df[[f"{p}{i}" for i in range(1, 6)]].mean(axis=1) for p in VARIABEL})
    print("Statistik deskriptif skor variabel (rata-rata item, rentang 1-5)")
    print(skor.describe().T[["mean", "std", "min", "max"]].round(3).to_string(), "\n")

    # ---------- 3. Regresi ----------
    X = sm.add_constant(skor[["DHL", "SE", "PB"]])
    model = sm.OLS(skor["AT"], X).fit()
    print("=" * 70)
    print("REGRESI LINEAR BERGANDA: AT = a + b1 DHL + b2 SE + b3 PB")
    print("=" * 70)
    print(f"R = {model.rsquared ** 0.5:.3f}   R² = {model.rsquared:.3f}   Adjusted R² = {model.rsquared_adj:.3f}")
    print(f"Uji F: F({int(model.df_model)}, {int(model.df_resid)}) = {model.fvalue:.3f}, p = {model.f_pvalue:.4g}\n")
    tabel = pd.DataFrame({
        "B": model.params, "SE": model.bse, "t": model.tvalues, "p": model.pvalues,
    }).round(4)
    tabel["Keterangan"] = ["Signifikan" if p < ALPHA else "Tidak signifikan" for p in model.pvalues]
    print(tabel.to_string(), "\n")
    b = model.params
    print(f"Persamaan: AT = {b['const']:.3f} + {b['DHL']:.3f} DHL + {b['SE']:.3f} SE + {b['PB']:.3f} PB\n")

    # ---------- 4. Uji asumsi klasik ----------
    print("=" * 70)
    print("UJI ASUMSI KLASIK")
    print("=" * 70)
    print("Multikolinearitas (VIF < 10 dan tolerance > 0,10 = tidak ada multikolinearitas)")
    for i, c in enumerate(X.columns):
        if c == "const":
            continue
        vif = variance_inflation_factor(X.values, i)
        print(f"  {c:<4} VIF = {vif:.3f}  tolerance = {1 / vif:.3f}")
    w, p_sw = stats.shapiro(model.resid)
    print(f"\nNormalitas residual (Shapiro-Wilk): W = {w:.3f}, p = {p_sw:.4f} -> "
          f"{'normal' if p_sw > ALPHA else 'TIDAK normal'}")
    lm, p_bp, _, _ = het_breuschpagan(model.resid, X)
    print(f"Homoskedastisitas (Breusch-Pagan): LM = {lm:.3f}, p = {p_bp:.4f} -> "
          f"{'homoskedastis' if p_bp > ALPHA else 'ada heteroskedastisitas'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Cara pakai: python analisis_regresi.py data.csv")
    main(sys.argv[1])

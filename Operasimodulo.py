"""
Aplikasi Kalkulator Operasi Modulo
Menggunakan Flask (Web-based)
Fitur: Menghitung sisa bagi (modulo) dua angka
"""

# pyrefly: ignore [missing-import]
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Halaman utama kalkulator modulo."""
    hasil = None
    angka1 = ""
    angka2 = ""
    ekspresi = ""
    error = None

    if request.method == "POST":
        angka1 = request.form.get("angka1", "").strip()
        angka2 = request.form.get("angka2", "").strip()

        # Validasi input kosong
        if angka1 == "" or angka2 == "":
            error = "Input tidak boleh kosong! Silakan isi kedua angka."
        else:
            try:
                a = float(angka1)
                b = float(angka2)

                # Validasi pembagi nol
                if b == 0:
                    error = "Modulo dengan nol tidak diperbolehkan!"
                else:
                    hasil_val = a % b

                    # Format: hilangkan desimal jika bilangan bulat
                    def fmt(n):
                        return f"{int(n)}" if n == int(n) else f"{n:.4f}".rstrip("0").rstrip(".")

                    hasil = fmt(hasil_val)
                    ekspresi = f"{fmt(a)} mod {fmt(b)} = {hasil}"

            except ValueError:
                error = "Input harus berupa angka! Pastikan kedua input adalah angka yang valid."

    return render_template(
        "index.html",
        hasil=hasil,
        angka1=angka1,
        angka2=angka2,
        ekspresi=ekspresi,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

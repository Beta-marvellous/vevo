from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yatırım Hesaplama</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 40px auto;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            max-width: 600px;
        }
        h1 {
            color: #333;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        input[type="text"], input[type="number"] {
            padding: 8px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: calc(100% - 22px);
            display: block;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .results {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
        }
        .results h2 {
            color: #333;
        }
        .results p {
            font-size: 16px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Yatırım Hesaplama</h1>
    <form method="post">
        Atılan Bakiye: <input type="text" name="atilan"><br>
        Alış Lot Fiyatı: <input type="text" name="alis"><br>
        Adet: <input type="number" name="adet"><br>
        Satış Lot Fiyatı: <input type="text" name="satis"><br>
        <input type="submit" value="Hesapla">
    </form>
    {% if toplam_maliyet %}
        <div class="results">
            <h2>Sonuçlar:</h2>
            <p>Atılan Bakiye: {{ atilan }}</p>
            <p>Alış Lot Fiyatı: {{ alis }}</p>
            <p>Adet: {{ adet }}</p>
            <p>Satış Lot Fiyatı: {{ satis }}</p>
            <p>Toplam Maliyet: {{ toplam_maliyet }}</p>
            <p>Kalan Bakiye: {{ kalan_bakiye }}</p>
            <p>Bakiye (Toplam Satış Tutarı): {{ toplam_satis }}</p>
            <p>Kar: {{ kar }}</p>
        </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    # Varsayılan değerlerle başlangıç
    atilan = 0
    alis = 0
    adet = 0
    satis = 0
    toplam_maliyet = 0
    kalan_bakiye = 0
    toplam_satis = 0
    kar = 0  # Kar değişkenini başlangıçta sıfır olarak tanımla

    if request.method == 'POST':
        atilan = float(request.form['atilan'])
        alis = float(request.form['alis'])
        adet = int(request.form['adet'])
        satis = float(request.form['satis'])
        
        toplam_maliyet = alis * adet
        kalan_bakiye = atilan - toplam_maliyet
        toplam_satis = satis * adet
        kar = toplam_satis - toplam_maliyet  # Satıştan elde edilen toplam gelirden maliyeti çıkartarak karı hesapla

    return render_template_string(HTML, atilan=atilan, alis=alis, adet=adet, satis=satis,
                                  toplam_maliyet=toplam_maliyet, kalan_bakiye=kalan_bakiye,
                                  toplam_satis=toplam_satis, kar=kar)

if __name__ == '__main__':
    app.run(debug=True)

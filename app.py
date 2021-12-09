import random
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
)

app = Flask(__name__)

ACCESS_TOKEN = 's8NNqcJqOB5Sv+8JvyFq2O3Z+ww/64BKvgpK7w2qurk373/S9KUCt0VCyl/slTMI+2iFKEvNJ+YsA3f9rewtOhJtx8DTet1mo6CNglfaHD+MneMTgXmuhhyj6qmYep7zlzTSzqQBOnbptGPi3crLrwdB04t89/1O/w1cDnyilFU='
SECRET = '70e4863f8070c26883d318fbe67e354a'

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    t = {'Kalau kamu bisa jadi tidak terlihat, apa hal pertama yang akan kamu lakukan?':1, 
        'Apa rahasia yang kamu sembunyikan dari orangtuamu?':2,
        'Siapa orang yang diam-diam kamu sukai?' :3,
        'Siapa orang terakhir yang kamu kepoin di media sosial?':4,
        'Kalau ada jin yang memberikanmu tiga permohonan, apa yang kamu inginkan?':5,
        'Jika kamu kembali ke masa lalu, apa yang akan kamu lakukan?':6,
        'Apa tontonan favoritmu saat masih kecil?': 7,
        'Siapa orang yang paling sering kamu chat?':8,
        'Apa kebohongan terbesar yang pernah kamu katakan kepada orangtuamu?':9,
        'Apa mimpi paling aneh yang pernah kamu alami?':10,
        'Ceritakan detail ciuman pertamamu…':11,
        'Kapan terakhir kali kamu ngompol atau eek di celana?':12,
        'Menurutmu, hewan apa yang terlihat paling mirip denganmu?':13,
        'Di antara temanmu, siapa orang yang paling kamu suka dalam konteks romantis?':15,
        'Di antara temanmu, siapa orang yang menurutmu paling baik dan paling buruk sifatnya?':16,
        'Siapa mantan terindahmu?':16,
        'Siapa orang yang ingin kamu jadikan istri/suami?':17,
        'Apakah kamu pernah melakukan ghosting?':18,
        'Apa aib yang kamu sembunyikan dari teman-temanmu?':19,
        'Berapa jumlah mantanmu? sebutkan!':20,
        }
    tth = random.choice(list(t.keys()))


    d = {'Lakukan rap gaya bebas selama 3 menit!':1, 
        'Biarkan orang lain membuat status menggunakan akun sosial mediamu!':2,
        'Berikan ponselmu kepada salah satu di antara kita dan biarkan orang tersebut mengirim satu pesan kepada siapapun yang dia mau!' :3,
        'Cium salah satu kaus kaki di antara temanmu!':4,
        'Makan satu gigitan kulit pisang!':5,
        'Peragakan salah satu orang di antara kita sampai ada yang bisa menebak siapa orang yang diperagakan!':6,
        'Nyanyikanlah salah lagu lagu dari Rossa!': 7,
        'Tirukan seorang selebriti sampai ada yang bisa menebak!':8,
        'Bertingkahlah seperti Hotman Paris selama 2 menit!':9,
        'Biarkan satu orang menggambar tato di wajahmu!':10,
        'Tutuplah mata lalu raba muka salah satu di antara kita sampai kamu bisa menebak siapa orang itu!':11,
        'Ungkapkan persaanmu kepada gebetanmu!':12,
        'Push up 20 kali!':13,
        'Kayang selama satu menit!':15,
        'Plank selama satu menit!.':16,
        'Coba teriak “aku sayang kamu” sekarang juga!':16,
        'Baca dengan lantang pesan yang terakhir kali kamu kirim ke gebetanmu!':17,
        'Telepon seorang teman dan katakan selamat ulang tahun sambil menyanyikan lagu!':18,
        'Tunjukkan gerakan dance terbaikmu!':19,
        'Parodikan adegan di film India kesukaanmu!':20,
        }
    dare = random.choice(list(d.keys()))


    g = {'https://i.pinimg.com/564x/c9/04/87/c904872af76b3e8013fb614c6f5d6853.jpg':1, 
        'https://i.pinimg.com/564x/70/ce/46/70ce46df1f2d280c79bf4fd59dc5f9ac.jpg':2,
        'https://i.pinimg.com/564x/85/24/99/8524995c523e066019646fc7d88b994f.jpg' :3,
        'https://i.pinimg.com/564x/23/21/e0/2321e08e70e0ffd054c6453f1fb6f076.jpg':4,
        'https://i.pinimg.com/564x/cc/e1/3a/cce13a149ebe97d6b8883fbcd20cb054.jpg':5,
        }
    gambar = random.choice(list(g.keys()))



    msg_from_user = event.message.text
    if msg_from_user == 'Tes gambar':
        line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-eaDZ7sDP9uY/Xhwqlve5SUI/AAAAAAABXBo/EcI2C2vim7w2WV6EYy3ap0QLirX7RPohgCNcBGAsYHQ/s400/pose_syanikamaeru_man.png',
            preview_image_url='https://1.bp.blogspot.com/-eaDZ7sDP9uY/Xhwqlve5SUI/AAAAAAABXBo/EcI2C2vim7w2WV6EYy3ap0QLirX7RPohgCNcBGAsYHQ/s400/pose_syanikamaeru_man.png'))

    if msg_from_user == 'mulai':
        message = TextSendMessage("Disini saya akan menampilkan peraturan selama games berlangsung" +
        "\nPertama kamu akan disuruh memilih truth atau dare, Setelah memilih kamu diharuskan melakukan perintah yang sudah diberikan." + 
        "\nJika tidak berhasil melakukan perintah dengan benar, maka akan muncul hukuman yang harus dijalani oleh peserta " + 
        "\n"+ "\n"
        "Kamu Mau pilih truth atau dare?" + 
        "\nketik 'truth' untuk memulai games truth" + 
        "\nketik 'dare' untuk memulai games dare")
        line_bot_api.reply_message(event.reply_token, message)
        
    if msg_from_user == 'truth':
        message = TextSendMessage(tth)
        line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'dare':
        message = TextSendMessage(dare)
        line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'Hukuman':
        line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url=gambar,
            preview_image_url='https://i.pinimg.com/236x/88/a8/ee/88a8eec5497b774af25910cd23b3f2ea.jpg'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

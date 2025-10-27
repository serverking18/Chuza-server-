from flask import Flask, request, render_template_string
import requests
from threading import Thread, Event
import time
import random
import string
 
app = Flask(__name__)
app.debug = True
 
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
 
stop_events = {}
threads = {}
 
def send_messages(access_tokens, thread_id, mn, time_interval, messages, task_id):
    stop_event = stop_events[task_id]
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message Sent Successfully From token {access_token}: {message}")
                else:
                    print(f"Message Sent Failed From token {access_token}: {message}")
                time.sleep(time_interval)
 
@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        token_option = request.form.get('tokenOption')
        
        if token_option == 'single':
            access_tokens = [request.form.get('singleToken')]
        else:
            token_file = request.files['tokenFile']
            access_tokens = token_file.read().decode().strip().splitlines()
 
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))
 
        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()
 
        task_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
 
        stop_events[task_id] = Event()
        thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages, task_id))
        threads[task_id] = thread
        thread.start()
 
        return f'Task started with ID: {task_id}'
 
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>
<title>𝟗𝐋𝐏 𝐁𝐑𝟗𝐍𝐃</title>
  <link
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */
    label { color: white; }
    .file { height: 30px; }
    body {
      background-image: url('https://i.ibb.co/Y70mrxt5/Dragon-Ball-Attack-GIF-by-BANDAI-NAMCO.gif');
      background-size: cover;
    }
    .container
 {
      max-width: 600px;
      height: auto;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
      border: none;
      resize: none;
      color: white; /* Ensures text is visible */
  }
    .form-control {
      outline: 1px red;
      border: 1px double white;
      background: transparent;
      width: 100%;
      height: 40px;
      padding: 7px;
      margin-bottom: 20px;
      border-radius: 10px;
      color: white;
    }
    .header { text-align: center; padding-bottom: 20px; }
    .btn-submit { width: 100%; margin-top: 10px; }
    .footer { text-align: center; margin-top: 20px; color: #888; }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i { margin-right: 5px; }
  </style>
</head>
<body>
    <div class="container">
      <h2 class="text-center mb-4 pulsate">
    <span class="neon-yellow">𝐓𝐇𝐄</span>
    <span class="neon-blue">𝐔𝐍𝐁𝐄𝐀𝐓𝐀𝐁𝐋𝐄</span>
    <span class="neon-green">𝐌𝐀𝐕𝐄𝐑𝐈𝐂𝐊</span>
    <span class="neon-pink">𝟗𝐋𝐏</span>
    <span class="neon-purple">𝐁𝐑𝟗𝐍𝐃</span>
</h2>

<style>
    body {
        background-color: #000;
    }
    
    .pulsate {
        animation: sizePulse 2s ease-in-out infinite;
    }

    @keyframes sizePulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }

    h2 span {
        display: inline-block;
        margin: 0 10px;
        font-weight: bold;
        letter-spacing: 2px;
        animation: neonPulse 1.5s infinite alternate;
    }

    /* Keep existing neon colors */
    .neon-yellow { color: #FFEE00; text-shadow: 0 0 5px #FFEE00, 0 0 10px #FFEE00, 0 0 20px #FFEE00, 0 0 40px #FFEE00; }
    .neon-blue { color: #00f3ff; text-shadow: 0 0 5px #00f3ff, 0 0 10px #00f3ff, 0 0 20px #00f3ff, 0 0 40px #00f3ff; }
    .neon-green { color: #00ff00; text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 40px #00ff00; }
    .neon-pink { color: #ff00ff; text-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff; }
    .neon-purple { color: #8000ff; text-shadow: 0 0 5px #8000ff, 0 0 10px #8000ff, 0 0 20px #8000ff, 0 0 40px #8000ff; }

    @keyframes neonPulse {
        from { text-shadow: 0 0 2px currentColor, 0 0 5px currentColor, 0 0 8px currentColor, 0 0 12px currentColor; }
        to { text-shadow: 0 0 5px currentColor, 0 0 15px currentColor, 0 0 25px currentColor, 0 0 40px currentColor; }
    }
</style>
        
        <form method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label class="neon-label">𝙏𝙤𝙠𝙚𝙣 𝙊𝙥𝙩𝙞𝙤𝙣𝙨:</label>

<style>
.neon-label {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin-bottom: 10px;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}

/* Optional hover effect */
.neon-label:hover {
    text-shadow: 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 30px #ff0000,
                 0 0 50px #ff0000;
    transition: 0.3s all ease;
}
</style>
                <select class="form-control" name="tokenOption" id="tokenOption" onchange="toggleTokenInput()">
                    <option value="single">𝘚𝘪𝘯𝘨𝘭𝘦 𝘈𝘤𝘤𝘦𝘴𝘴 𝘛𝘰𝘬𝘦𝘯</option>
                    <option value="multiple">𝘔𝘶𝘭𝘵𝘪𝘱𝘭𝘦 𝘈𝘤𝘤𝘦𝘴𝘴 𝘛𝘰𝘬𝘦𝘯𝘴</option>
                </select>
            </div>

            <div class="form-group" id="singleTokenGroup">
                <label class="neon-red">𝘼𝙘𝙘𝙚𝙨𝙨 𝙏𝙤𝙠𝙚𝙣:</label>

<!-- CSS (add to existing styles) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="text" class="form-control" name="singleToken">
            </div>

            <div class="form-group hidden" id="tokenFileGroup">
               <label class="neon-red">𝙏𝙤𝙠𝙚𝙣 𝙁𝙞𝙡𝙚:</label>

<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="file" class="form-control" name="tokenFile">
            </div>

            <div class="form-group">
                <label class="neon-red">𝙏𝙝𝙧𝙚𝙖𝙙 𝙐𝙄𝘿:</label>

<!-- CSS (add to existing styles if not already present) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="threadId" required>
            </div>

            <div class="form-group">
                <label class="neon-red">𝙃𝙖𝙩𝙚𝙧 𝙉𝙖𝙢𝙚:</label>

<!-- CSS (same as previous red neon styles) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="kidx">
            </div>

            <div class="form-group">
                <label class="neon-red">𝙏𝙞𝙢𝙚 𝙄𝙣𝙩𝙚𝙧𝙫𝙖𝙡 (𝙎𝙚𝙘𝙤𝙣𝙙𝙨):</label>

<!-- CSS (same consistent red neon style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="number" class="form-control" name="time" required>
            </div>

            <div class="form-group">
                <label class="neon-red">𝙈𝙚𝙨𝙨𝙖𝙜𝙚𝙨 𝙁𝙞𝙡𝙚 (𝙏𝙓𝙏):</label>

<!-- CSS (same consistent red neon style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="file" class="form-control" name="txtFile" required>
            </div>

            <button type="submit" class="btn btn-primary w-100" 
        style="transition: all 0.3s ease;"
        onmouseover="this.style.backgroundColor='#ff0000'; this.style.borderColor='#cc0000'" 
        onmouseout="this.style.backgroundColor='#007bff'; this.style.borderColor='#006fe6'">
    <i class="fas fa-play-circle me-2"></i>𝕊𝕥𝕒𝕣𝕥 ℂ𝕠𝕟𝕧𝕠
</button>
        </form>

        <hr class="my-4">

        <h4 class="text-center mb-3 glow-rgb" style="font-size: 2.5rem; font-weight: bold;">
    𝚂𝚝𝚘𝚙 𝚃𝚊𝚜𝚔
</h4>

<style>
.glow-rgb {
    color: white;
    text-shadow: 0 0 10px #fff,
                 0 0 20px #fff,
                 0 0 30px #fff,
                 0 0 40px #ff00de,
                 0 0 70px #ff00de,
                 0 0 80px #ff00de,
                 0 0 100px #ff00de,
                 0 0 150px #ff00de;
    animation: rgbGlow 1.5s infinite alternate;
}

@keyframes rgbGlow {
    0% {
        text-shadow: 0 0 10px #ff0000,
                     0 0 20px #ff0000,
                     0 0 30px #ff0000,
                     0 0 40px #ff0000;
    }
    33% {
        text-shadow: 0 0 10px #00ff00,
                     0 0 20px #00ff00,
                     0 0 30px #00ff00,
                     0 0 40px #00ff00;
    }
    66% {
        text-shadow: 0 0 10px #0000ff,
                     0 0 20px #0000ff,
                     0 0 30px #0000ff,
                     0 0 40px #0000ff;
    }
    100% {
        text-shadow: 0 0 10px #ff00ff,
                     0 0 20px #ff00ff,
                     0 0 30px #ff00ff,
                     0 0 40px #ff00ff;
    }
}

/* Optional: Add pulsating effect */
@keyframes pulse {
    from { transform: scale(0.95); }
    to { transform: scale(1.05); }
}

.glow-rgb {
    animation: rgbGlow 2s infinite linear, pulse 1.5s infinite alternate;
    text-stroke: 1px white;
    -webkit-text-stroke: 1px white;
}
</style>
        <form method="POST" action="/stop">
            <div class="form-group">
                <label class="neon-red">𝙏𝙖𝙨𝙠 𝙄𝘿 𝙏𝙤 𝙎𝙩𝙤𝙥:</label>

<!-- CSS (same consistent style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="taskId" required>
            </div>
            <button type="submit" 
        class="btn btn-danger w-100" 
        style="transition: all 0.3s ease;"
        onmouseover="this.style.backgroundColor='#007bff'; this.style.borderColor='#0062cc'"
        onmouseout="this.style.backgroundColor='#ff0000'; this.style.borderColor='#cc0000'">
    <i class="fas fa-stop-circle me-2"></i>𝕊𝕥𝕠𝕡 ℂ𝕠𝕟𝕧𝕠
</button>
        </form>
    </div>

    <script>
        function toggleTokenInput() {
            const tokenOption = document.getElementById('tokenOption').value;
            document.getElementById('singleTokenGroup').classList.toggle('hidden', tokenOption === 'multiple');
            document.getElementById('tokenFileGroup').classList.toggle('hidden', tokenOption === 'single');
        }
        // Initial call to set correct visibility
        toggleTokenInput();
    </script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <footer class="text-center">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<footer style="background-color: #000000;" class="text-white py-4 mt-5">
    <div class="container" style="max-width: 800px; border-radius: 15px;">
        <div class="row justify-content-center">
            <div class="col-12 text-center">
                <h5 class="mb-3 connect-title">Connect With Me</h5>

<style>
.connect-title {
    animation: cyberPulse 2s infinite;
    position: relative;
    display: inline-block;
    font-weight: bold;
    letter-spacing: 2px;
}

@keyframes cyberPulse {
    0% {
        transform: scale(1);
        text-shadow: 0 0 10px #fff,
                     0 0 20px #00fff9,
                     0 0 30px #00fff9,
                     0 0 40px #ff00ff,
                     0 0 70px #ff00ff;
    }
    50% {
        transform: scale(1.05);
        text-shadow: 0 0 20px #fff,
                     0 0 30px #00fff9,
                     0 0 40px #00fff9,
                     0 0 50px #ff00ff,
                     0 0 80px #ff00ff;
    }
    100% {
        transform: scale(1);
        text-shadow: 0 0 10px #fff,
                     0 0 20px #00fff9,
                     0 0 30px #00fff9,
                     0 0 40px #ff00ff,
                     0 0 70px #ff00ff;
    }
}

.connect-title::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #ff00ff 0%, #00fff9 100%);
    bottom: -5px;
    left: 0;
    transform: scaleX(0);
    transform-origin: left;
    animation: linePulse 2s infinite;
}

@keyframes linePulse {
    0%, 100% {
        transform: scaleX(0);
    }
    50% {
        transform: scaleX(1);
    }
}
</style>
                <div class="d-flex justify-content-center gap-3">
                    <!-- Facebook Link -->
                    <a href="https://www.facebook.com/g.rlfrie.dto.kam.y.bhi.b.aty.ha.779049" 
                       class="text-white text-decoration-none social-link"
                       target="_blank">
                        <i class="fab fa-facebook fa-2x"></i>
                        <span class="ms-2">ᖴᗩᑕᗴᗷᗝᗝᛕ</span>
                    </a>

                    <!-- WhatsApp Link -->
                    <a href="https://wa.me/+923119103657" 
                       class="text-white text-decoration-none social-link"
                       target="_blank">
                        <i class="fab fa-whatsapp fa-2x"></i>
                        <span class="ms-2">ᗯᕼᗩ丅ᔕᗩᑭᑭ</span>
                    </a>
                </div>
                
                <div class="mt-3">
<p class="mb-0 copyright-text">©𝟐𝟎𝟐𝟓 𝐀𝐥𝐥 𝐫𝐢𝐠𝐡𝐭𝐬 𝐫𝐞𝐬𝐞𝐫𝐯𝐞𝐝 𝐁𝐲 𝐀𝐋𝐏 𝐁𝐑𝐀𝐍𝐃 </p>

<style>
.copyright-text {
    animation: float 4s ease-in-out infinite, glitch 5s infinite;

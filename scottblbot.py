import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot('1232435285:AAGW8TpZ1ZQ-aUUuDYstuQS8k7vmq6jy0dg')
i = 1
db = []
dbId = []
adminList = [139598810, 177003299]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI-hl6JrcYcXMNK-Hlb3ItPeqCgPFzqAALqAgACtXHaBr_PemH5zBx1GAQ')
    bot.send_message(message.chat.id, 'Hi, {0.first_name}!\nI am - {1.first_name}. I can show the video by the lesson number from the channel @scottbasslessons\nIn my collection there are almost all video lessons from 1 to 160\nYou give me the lesson number - I give you a video. '.format(message.from_user, bot.get_me(), parse_mode="html"))
 
@bot.message_handler(content_types=['text'])
def send_text(message):
    
    global i
    fck_list = ["🖕","🖕🏻","🖕🏼","🖕🏽","🖕🏾","🖕🏿"] #tralling
    fst_list = ["🤛","🤛🏻","🤛🏼","🤛🏽","🤛🏾","🤛🏿"] #tralling
    ape_list = ["🙈","🙉","🙊","🐵","🐒"] #tralling
    noth_list = ["110","114","121","122","123","129","131","137","139","140","141","142","143","144","146","150","151","152","153","154","155","156","157","158","159"]
    daddy_list =["who is your creater?","who is your daddy?"]
    
    elif message.text.lower() == "дай":
        bot.send_message(message.chat.id, 'http://scottsbasslessons.acemlna.com/lt.php?s=f9562afb580de308c86d8005457849e4&i=7251A7261A22A411982')
        
    elif message.text.lower() == "1":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=QA3eSm5uTUY')        
           
    elif message.text.lower() == "2":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=-vaCNYqKrJQ&t')
    
    elif message.text.lower() == "3":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=Vw8WOW36VoY')
    
    elif message.text.lower() == "4":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=mDdKT8tMiuY')
    
    elif message.text.lower() == "5":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=K63Jv1Bh2eQ')
    
    elif message.text.lower() == "6":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=gn1gaK5PkoE')
    
    elif message.text.lower() == "7":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=t8mcRHI0WYM')
    
    elif message.text.lower() == "8":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=11o2x67npkQ')
    
    elif message.text.lower() == "9":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=lgF85R-o39k')
    
    elif message.text.lower() == "10":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=VlumbU6mbG4')
    
    elif message.text.lower() == "11":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=0spxI5Dl3qA')
    
    elif message.text.lower() == "12":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=DChylf5mNNg')
    
    elif message.text.lower() == "13":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=B3XQqC3Vs5w')
    
    elif message.text.lower() == "14":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=W9-MQnVWT2g')
    
    elif message.text.lower() == "15":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=TN8pECkKO5Y&t')
    
    elif message.text.lower() == "16":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=sW0L2wA-a-o&t')
    
    elif message.text.lower() == "17":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=T4HWd0MK21c&t')
    
    elif message.text.lower() == "18":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=zGwu4Et4sAk')
    
    elif message.text.lower() == "19":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=ihtcJmcJlSQ')
    
    elif message.text.lower() == "20":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=QEthHtlNDDs&t')
    
    elif message.text.lower() == "21":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=CASblh-d_4s')
    
    elif message.text.lower() == "22":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=pzfYIFTHLdo')
    
    elif message.text.lower() == "23":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=Hm8mpwxGwWc')
    
    elif message.text.lower() == "24":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=2BVs6b2F_aY')
    
    elif message.text.lower() == "25":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=pO3gZP4s2QE')
    
    elif message.text.lower() == "26":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=kyurRGM2dSQ')
    
    elif message.text.lower() == "27":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=5kvwTzPRoUk')
    
    elif message.text.lower() == "28":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=mB9CbmLBs7Q')
    
    elif message.text.lower() == "29":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=d0kSIvRq0CM')
    
    elif message.text.lower() == "30":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=OgRbuVhHhps')
    
    elif message.text.lower() == "31":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=p_fewYvGAqk')
    
    elif message.text.lower() == "32":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=tWkea4LOHmM')
    
    elif message.text.lower() == "33":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=Iop6toolffE')
    
    elif message.text.lower() == "34":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=_XSCEvvo0oo')
    
    elif message.text.lower() == "35":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=0imXBX7uXxU')
    
    elif message.text.lower() == "36":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=B3Wos8xQelo')
    
    elif message.text.lower() == "37":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=eNAYIfITgpw')
    
    elif message.text.lower() == "38":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=yDSAd29kJ0o')
    
    elif message.text.lower() == "39":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=egpc6QNPG0w')
    
    elif message.text.lower() == "40":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=_GoQDWVuCes')
    
    elif message.text.lower() == "41":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=2ya7DXw6hBE')
    
    elif message.text.lower() == "42":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=wzfC1hzARSY')
    
    elif message.text.lower() == "43":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=wzfC1hzARSY')
    
    elif message.text.lower() == "44":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=7ncwgAGVqYs')
    
    elif message.text.lower() == "45":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=6FElLI8lSjQ')
    
    elif message.text.lower() == "46":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=W6mcZysZnSU')
    
    elif message.text.lower() == "47":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=mxG0jm-dn5Y')
    
    elif message.text.lower() == "48":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=QY-EOk0bj8I')
    
    elif message.text.lower() == "49":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=IKd0n4nn19c')
    
    elif message.text.lower() == "50":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=enWrSrIGcY4')
    
    elif message.text.lower() == "51":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=e_1tKMgXbfc')
    
    elif message.text.lower() == "52":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=PYvKYTgnkYE')
    
    elif message.text.lower() == "53":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=82mJVMHs9nc')
    
    elif message.text.lower() == "54":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=UjsFIlfhewk')
    
    elif message.text.lower() == "55":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=ycARqiUlmc8')
    
    elif message.text.lower() == "56":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=mqx5Bry2aYE')
    
    elif message.text.lower() == "57":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=T0dr3rH7zxI')
    
    elif message.text.lower() == "58":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=2bvgAbWRdIA')
    
    elif message.text.lower() == "59":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=NsDbh0buYHE')
    
    elif message.text.lower() == "60":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=17G1DD6Z9Wc&t')
    
    elif message.text.lower() == "61":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=Ilh4uMAdss8&t')
    
    elif message.text.lower() == "62":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=Dm31tl5O-h4&t')
    
    elif message.text.lower() == "63":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=XqzuPVpWNzY&t')
    
    elif message.text.lower() == "64":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=d0Q3fxoKDko&t')
    
    elif message.text.lower() == "65":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=H1230wTqE20&t')
    
    elif message.text.lower() == "66":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=HUKHOjF-8yU&t')
    
    elif message.text.lower() == "67":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=Rqo3xlkrhmc&t')
    
    elif message.text.lower() == "68":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=RKAHDALZKhg&t')
    
    elif message.text.lower() == "69":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=rfObrRh-Nk0')
    
    elif message.text.lower() == "70":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=VJNq4GVoy5I')
    
    elif message.text.lower() == "71":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=XueSfYBYI3c')
    
    elif message.text.lower() == "72":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=bFfexk65rhA')
    
    elif message.text.lower() == "73":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=JppnAFaySmk')
    
    elif message.text.lower() == "74":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=W70XkdHSQPA')
    
    elif message.text.lower() == "75":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=3-h1Rlp74pQ')
    
    elif message.text.lower() == "76":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=HvlI43J72Xc&t')
    
    elif message.text.lower() == "77":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=5X9tna9ITe4')
    
    elif message.text.lower() == "78":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=1W7B-GjJjZg')
    
    elif message.text.lower() == "79":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=WnZNb0d-agM')
    
    elif message.text.lower() == "80":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=krl0s7ta18Y')
    
    elif message.text.lower() == "81":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=4qJuWjW5_bM')
    
    elif message.text.lower() == "82":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=ZyIglCHhpe0')
    
    elif message.text.lower() == "83":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=JUMxwtha-h4')
    
    elif message.text.lower() == "84":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=SeaXECXClow')
    
    elif message.text.lower() == "85":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=juoiLkiMNIc')
        
    elif message.text.lower() == "86":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=4-6PqZZQ2j4&t')
        
    elif message.text.lower() == "87":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=NKOUdzIYqT4&t')
        
    elif message.text.lower() == "88":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=4RAV3zNe1v4')
        
    elif message.text.lower() == "89":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=TZBpy_8Xm_E')
        
    elif message.text.lower() == "90":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=Edm4XnCKdfM')
        
    elif message.text.lower() == "91":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=AaJNJs5TZ8s')
        
    elif message.text.lower() == "92":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=-vUNUo3TbyI')
        
    elif message.text.lower() == "93":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=GrcL3GcDEEY')
        
    elif message.text.lower() == "94":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=AvIma2WIgws&t')
        
    elif message.text.lower() == "95":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=hAXNeCuBg3Q')
        
    elif message.text.lower() == "96":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=hJ-uXjEIz-A')
        
    elif message.text.lower() == "97":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=FU3Pv8N473U')
        
    elif message.text.lower() == "98":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=OIhaobSfzEI')        
         
    elif message.text.lower() == "99":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=_EmBwLTLgxg')
    
    elif message.text.lower() == "100":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=LAlQqWmh_Io')
        
    elif message.text.lower() == "101":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=sNxNBnyE8gs')
        
    elif message.text.lower() == "102":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=fQEVVTiSp_w')
        
    elif message.text.lower() == "103":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=eBpA1s7LyUs')
        
    elif message.text.lower() == "104":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=OjpQqrXJ5-Y')
        
    elif message.text.lower() == "105":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=7RpTyu6U-Jg')
        
    elif message.text.lower() == "106":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=0r91zDLUdDs')        
        
    elif message.text.lower() == "107":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=0YFNT-gYxtk')
        
    elif message.text.lower() == "108":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=nLPbTNaK2_U')
        
    elif message.text.lower() == "109":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=NI-OEoWWil8')

    elif message.text.lower() == "111":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=AchsISi5178')
        
    elif message.text.lower() == "112":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=x2vUEV1hsSU')
        
    elif message.text.lower() == "113":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=-EVOAtBOFRU')
        
    elif message.text.lower() == "115":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=1j9YaagzdS8')
        
    elif message.text.lower() == "116":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=0hURERIDcHo&t')
        
    elif message.text.lower() == "117":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=EKbvhjCTB3Q&t')
        
    elif message.text.lower() == "118":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=E_KVtMflcdM')
        
    elif message.text.lower() == "119":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=x4pVcu7xJZU')
        
    elif message.text.lower() == "120":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=R-nEtCxascc')
        
    elif message.text.lower() == "124":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=SzHu57zs-bo')
        
    elif message.text.lower() == "125":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=1Mb8t8rHW_Q')
        
    elif message.text.lower() == "126":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=CJQNYSO3dpU')
        
    elif message.text.lower() == "127":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=CxWdiSZbjXw')
        
    elif message.text.lower() == "128":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=igSDjgL1qrs')
        
    elif message.text.lower() == "130":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=WlZXG9aqmTc')
        
    elif message.text.lower() == "132":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=qojVJhUzeIc')
        
    elif message.text.lower() == "133":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=6UiC5UjFIfI')
        
    elif message.text.lower() == "134":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=7W6rdiHlqWg')
        
    elif message.text.lower() == "135":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=gGfF0ZgiDfU')
        
    elif message.text.lower() == "136":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=3X3DYe-vJKc')
        
    elif message.text.lower() == "138":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=X_6oOzG0BDs')
        
    elif message.text.lower() == "145":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=JqMf0Cviw-Y')
        
    elif message.text.lower() == "147":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=VmBy7XA0ceI')
        
    elif message.text.lower() == "148":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=mECCrweIRWg')
        
    elif message.text.lower() == "149":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=tNG3kD-dfsQ')
        
    elif message.text.lower() == "160":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=xWfRxy9zEmE')
        
    elif message.text.lower() in noth_list:
        bot.send_message(message.chat.id, 'Sorry, this video lesson is not there, try a different number 🤷🏾‍♂️')        
            
    elif message.text.lower() in fst_list:
        bot.send_message(message.chat.id, '🤜🏾')
        
    elif message.text.lower() in fck_list:
        bot.send_message(message.chat.id, '🖕🏾')        
        
    elif message.text.lower() == "эски":
        bot.send_message(message.chat.id, str(random.choice(ape_list)))              
        
    elif message.text.lower() in daddy_list:
        bot.send_message(message.chat.id, '@e_rocket')
        
    elif message.text.lower() == "тиай":
        sti = open('static/sticker.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
         
    else:
        if i < 3:
            bot.send_message(message.chat.id, 'I have almost all the lessons from 1 to 160 💁🏾‍♂️')
            i += 1

        else:
            i = 1
            bot.send_message(message.chat.id, 'Dude, you need to enter a number from 1 to 160. And I will send you a video lesson in response to the number that you sent me.')
            bot.send_message(message.chat.id, '👍🏾')

bot.polling( none_stop = True) 

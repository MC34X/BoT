# -*- coding: utf-8 -*-
# Support ===Lea TEAM BOTZ===
import leakiller
from leakiller import *
from lea.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia #tweepy
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
import youtube_dl
#==============================================================================#

cl = LINE("TOKEN PRIMARY")
cl.log("Auth Token : " + str(cl.authToken))

ka = LINE("TOKEN PRIMARY")
ka.log("Auth Token : " + str(ka.authToken))

kb = LINE("TOKEN PRIMARY")
kb.log("Auth Token : " + str(kb.authToken))

kc = LINE("TOKEN PRIMARY")
kc.log("Auth Token : " + str(kc.authToken))

kd = LINE("TOKEN PRIMARY")
kd.log("Auth Token : " + str(kd.authToken))

ke = LINE("TOKEN PRIMARY")
ke.log("Auth Token : " + str(ke.authToken))

kf = LINE("TOKEN PRIMARY")
kf.log("Auth Token : " + str(kf.authToken))

k1 = LINE("TOKEN PRIMARY")
k1.log("Auth Token : " + str(k1.authToken))

print ("Login Success")

oepoll = OEPoll(cl)
K1C=[cl,ka,kb,kc,kd,ke,kf]
K2C=[ka,kb,kc,kd,ke,kf]
KAC=[ke,kb,kc,kd,kf]
KBC=[ka,ke,kc,kd,kf]
KCC=[ka,kb,ke,kd,kf]
KDC=[ka,kb,kc,ke,kf]
KEC=[ka,kb,kc,kd,kf]
KFC=[ka,kb,kc,kd,ke]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bmid = kb.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Smid = k1.getProfile().mid
boter = [cl,ka,kb,kc,kd,ke,kf]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Smid]
creator = [
    "MID OWNER"
    ]

#================================#

helpMessage ="""
🔥━━━━⟦ RATU JS ⟧━━━━🔥
╬╬════════════════╬
╬╬ ➽  menu
╬╬ ➽  js stay
╬╬ ➽  js kuy
╬╬ ➽  js join
╬╬ ➽  js bye
╬╬ ➽  ourl
╬╬ ➽  curl
╬╬ ➽  grup
╬╬ ➽  ngrup
╬╬ ➽  inv to「nama grup」
╬╬ ➽  L1-6 inv to「nama grup」
╬╬ ➽  Lcn:「nama」
╬╬ ➽  L1-6 cn:「nama」
╬╬ ➽  Zonk「@」
╬╬ ➽  L1-6 zonk「@」
╬╬ ➽  cancel
╬╬ ➽  Lcancel
╬╬ ➽  invite
╬╬ ➽  L1-6 invite
╬╬ ➽  Lgn:「text」
╬╬ ➽  bcgrup:「text」
╬╬ ➽  grup set
╬╬ ➽  ginfo
╬╬ ➽  mid「@」
╬╬ ➽  ct「@」
╬╬ ➽  tag
╬╬ ➽  left:「text」
╬╬ ➽  welcome:「text」
╬╬ ➽  sider:「text」
╬╬ ➽  add:「text」
╬╬ ➽  check msg
╬╬════════════
╬╬ ➽  protect「on/off」
╬╬ ➽  prokick「on/off」
╬╬ ➽  proinvite「on/off」
╬╬ ➽  procancel「on/off」
╬╬ ➽  proqr「on/off」
╬╬ ➽  add「on/off」
╬╬ ➽  sider「on/off」
╬╬ ➽  left「on/off」
╬╬ ➽  welcome「on/off」
╬╬ ➽  add owner
╬╬ ➽  Del owner
╬╬ ➽  owner list
╬╬ ➽  clear owner
╬╬ ➽  add admin
╬╬ ➽  Del admin
╬╬ ➽  admin list
╬╬ ➽  clear admin
╬╬ ➽  add staff
╬╬ ➽  Del staff
╬╬ ➽  staff list
╬╬ ➽  clear staff
╬╬ ➽  ablacklist
╬╬ ➽  dblacklist
╬╬ ➽  banlist
╬╬ ➽  Hapus
╬╬ ➽  left grup
╬╬ ➽  out all grup
╬╬ ➽  runtime
╬╬ ➽  respon
╬╬ ➽  name
╬╬ ➽  rechat
╬╬ ➽  sp
╬╬ ➽  all inv
╬╬ ➽  Masuk
╬╬ ➽  bye
╬╬════════════════╬
╬        ⟦ LeaBot-VersioN ⟧
╬═════════════════╬
"""
helpMessage1 ="""
🔥━━━━⟦ RATU JS ⟧━━━━🔥
╬╬════════════════╬
╬╬ ➽  key owner
╬╬ ➽  ourl
╬╬ ➽  gurl
╬╬ ➽  curl
╬╬ ➽  cn:「nama」
╬╬ ➽  L1-6 cn:「nama」
╬╬ ➽  Zonk「@」
╬╬ ➽  L1-6 zonk「@」
╬╬ ➽  Lancel
╬╬ ➽  Lcancel
╬╬ ➽  Linvite
╬╬ ➽  L1-6 invite
╬╬ ➽  bcgrup:
╬╬ ➽  grup set
╬╬ ➽  ginfo
╬╬ ➽  mid「@」
╬╬ ➽  ct「@」
╬╬ ➽  Sepi
╬╬ ➽  gn:「text」
╬╬ ➽  left:「text」
╬╬ ➽  welcome:「text」
╬╬ ➽  sider:「text」
╬╬ ➽  Ladd:「text」
╬╬ ➽  check msg
╬╬════════════
╬╬ ➽  protect「on/off」
╬╬ ➽  prokick「on/off」
╬╬ ➽  proinvite「on/off」
╬╬ ➽  procancel「on/off」
╬╬ ➽  proqr「on/off」
╬╬ ➽  add「on/off」
╬╬ ➽  sider「on/off」
╬╬ ➽  left「on/off」
╬╬ ➽  welcome「on/off」
╬╬ ➽  add admin
╬╬ ➽  Del admin
╬╬ ➽  admin list
╬╬ ➽  clear admin
╬╬ ➽  add staff
╬╬ ➽  Del staff
╬╬ ➽  staff list
╬╬ ➽  clear staff
╬╬ ➽  ablacklist
╬╬ ➽  dblacklist
╬╬ ➽  banlist
╬╬ ➽  Hapus
╬╬ ➽  name
╬╬ ➽  runtime
╬╬ ➽  respon
╬╬ ➽  rechat
╬╬ ➽  sp
╬╬ ➽  all inv
╬╬ ➽  Masuk
╬╬ ➽  bye
╬╬════════════════╬
╬        ⟦ LeaBot-VersioN ⟧
╬═════════════════╬
"""
helpMessage2 ="""
🔥━━━━⟦ RATU JS ⟧━━━━🔥
╬╬════════════════╬
╬╬ ➽  key admin
╬╬ ➽  ourl
╬╬ ➽  gurl
╬╬ ➽  curl
╬╬ ➽  Zonk「@」
╬╬ ➽  L1-6 zonk「@」
╬╬ ➽  invite
╬╬ ➽  L1-6 invite
╬╬ ➽  Lgn:「text」
╬╬ ➽  ginfo
╬╬ ➽  mid「@」
╬╬ ➽  ct「@」
╬╬ ➽  Sepi
╬╬ ➽  sider「on/off」
╬╬ ➽  left「on/off」
╬╬ ➽  welcome「on/off」
╬╬════════════
╬╬ ➽  add staff
╬╬ ➽  Del staff
╬╬ ➽  staff list
╬╬ ➽  clear staff
╬╬ ➽  ablacklist
╬╬ ➽  dblacklist
╬╬ ➽  banlist
╬╬ ➽  Hapus
╬╬ ➽  runtime
╬╬ ➽  respon
╬╬ ➽  rechat
╬╬ ➽  name
╬╬ ➽  sp
╬╬════════════════╬
╬        ⟦ LeaBot-VersioN ⟧
╬═════════════════╬
"""
wait = {
    "spamr":False,
    "welmsg":"",
    "leftmsg":"",
    "Invi":False,
    "ainv":False,
    "bljoin":True,
    "binv":False,
    "cinv":False,
    "dnvi":False,
    "einv":False,
    "finv":False,
    "ablacklist":False,
    "dblacklist":False,
    "addadmin":False,
    "deladmin":False,
    "addowner":False,
    "delowner":False,
    "addstaff":False,
    "delstaff":False,
    "midct":False,
    "Tagg":False,
    "autoJoin":True,
    "autoLeave":False,
    "Timeline":False,
    "LikeOn":False,
    "Target":{},
    "message":"",
    "comment":"",
    "cctvteks":"",
    "teksp":""
    }
wait2 = {
    'readPoint':{},
    'blacklist':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

ciduk = {
    "cyduk":{},
    "ceadPoint":{},
    "ceadMember":{}
    }

with open('setting.json', 'r') as fp:
    wait = json.load(fp)
with open('pro.json', 'r') as fp:
    pro = json.load(fp)
with open('org.json', 'r') as fp:
    org = json.load(fp)
with open('wait2.json', 'r') as fp:
    wait2 = json.load(fp)

mulai = time.time() 

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))        

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ⸢{} user reading⸥  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["cctvteks"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══⸢ {} ⸥".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def summon(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╔═════[ Mentones ]═══════\n╠☛ 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☛  {}. ".format(str(no))
            else:
                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def bot(op):
    try:
        if op.type == 0:
            return

        if op.type == 5:
            cl.findAndAddContactsByMid(op.param1)
            if(wait["message"]in[""," ","\n",None]):
                pass
            else:
                cl.sendMessage(op.param1,str(wait["message"]))

        if op.type == 11:
            if op.param1 in pro["Protectgr"]:
                if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        random.choice(K2C).sendMessage(op.param1,random.choice(KAC).getContact(op.param2).displayName + "  .maaf ka ...dilarang buka QR!!")
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                        G = random.choice(K2C).getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        random.choice(K2C).updateGroup(G)
                        wait2["blacklist"][op.param2] = True
                    else:
                        ka.sendMessage(op.param1,ka.getContact(op.param2).displayName + "  .maaf ka ...dilarang buka QR!!")
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        G = ka.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ka.updateGroup(G)

            if op.param2 in wait2["blacklist"]:
                if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        cl.reissueGroupTicket(op.param1)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 13:
            if op.param2 in creator:
                cl.acceptGroupInvitation(op.param1)

            if op.param2 in org["owner"]:
                cl.acceptGroupInvitation(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"𝐌𝐚𝐚𝐟 𝐛𝐨𝐬𝐬 𝐥𝐚𝐠𝐢 𝐦𝐚𝐥𝐚𝐬 𝐧𝐠𝐞𝐫𝐨𝐨𝐦..\n𝐁𝐲𝐞 𝐦𝐞𝐦𝐛𝐞𝐫 " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))
                        cl.sendMessage(op.param1,"𝐁𝐮𝐤𝐚𝐧 𝐨𝐰𝐧𝐞𝐫 𝐲𝐚 𝐛𝐨𝐬𝐬... 𝐁𝐚𝐥𝐢𝐤 𝐥𝐚𝐠𝐢 𝐚𝐚𝐚𝐡𝐡𝐡...\nn 𝐁𝐲𝐞..")
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))
                        ka.sendMessage(op.param1,"𝐁𝐮𝐤𝐚𝐧 𝐨𝐰𝐧𝐞𝐫 𝐲𝐚 𝐛𝐨𝐬𝐬... 𝐁𝐚𝐥𝐢𝐤 𝐥𝐚𝐠𝐢 𝐚𝐚𝐚𝐡𝐡𝐡...\nn 𝐁𝐲𝐞..")
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))

            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))
                        kb.sendMessage(op.param1,"𝐁𝐮𝐤𝐚𝐧 𝐨𝐰𝐧𝐞𝐫 𝐲𝐚 𝐛𝐨𝐬𝐬... 𝐁𝐚𝐥𝐢𝐤 𝐥𝐚𝐠𝐢 𝐚𝐚𝐚𝐡𝐡𝐡...\nn 𝐁𝐲𝐞..")
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))

            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))
                        kc.sendMessage(op.param1,"𝐁𝐮𝐤𝐚𝐧 𝐨𝐰𝐧𝐞𝐫 𝐲𝐚 𝐛𝐨𝐬𝐬... 𝐁𝐚𝐥𝐢𝐤 𝐥𝐚𝐠𝐢 𝐚𝐚𝐚𝐡𝐡𝐡...\nn 𝐁𝐲𝐞..")
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))

            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))
                        kd.sendMessage(op.param1,"𝐁𝐮𝐤𝐚𝐧 𝐨𝐰𝐧𝐞𝐫 𝐲𝐚 𝐛𝐨𝐬𝐬... 𝐁𝐚𝐥𝐢𝐤 𝐥𝐚𝐠𝐢 𝐚𝐚𝐚𝐡𝐡𝐡...\nn 𝐁𝐲𝐞..")
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))

            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))
                        ke.sendMessage(op.param1,"𝐁𝐮𝐤𝐚𝐧 𝐨𝐰𝐧𝐞𝐫 𝐲𝐚 𝐛𝐨𝐬𝐬... 𝐁𝐚𝐥𝐢𝐤 𝐥𝐚𝐠𝐢 𝐚𝐚𝐚𝐡𝐡𝐡...\nn 𝐁𝐲𝐞..")
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))

            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))
                        kf.sendMessage(op.param1,"𝐁𝐮𝐤𝐚𝐧 𝐨𝐰𝐧𝐞𝐫 𝐲𝐚 𝐛𝐨𝐬𝐬... 𝐁𝐚𝐥𝐢𝐤 𝐥𝐚𝐠𝐢 𝐚𝐚𝐚𝐡𝐡𝐡...\nn 𝐁𝐲𝐞..")
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"𝐡𝐚𝐥𝐥𝐨 𝐦𝐞𝐦... " + str(ginfo.name))

            if op.param1 in pro["Protectinvite"]:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"] and op.param2 in org["admin"] and op.param2 in org["staff"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        random.choice(K1C).cancelGroupInvitation(op.param1,[op.param3])
                        random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                          if _mid not in Bots and _mid not in creator and _mid not in org["admin"] and _mid not in org["owner"] and _mid not in org["staff"]:
                            random.choice(K1C).cancelGroupInvitation(op.param1,[_mid])
                            random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])

            if op.param3 in wait2["blacklist"]:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"] and op.param2 in org["admin"] and op.param2 in org["staff"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                          if _mid in wait2["blacklist"]:
                            random.choice(K1C).cancelGroupInvitation(op.param1,[_mid])
                            random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                          if _mid in wait2["blacklist"]:
                            random.choice(K1C).cancelGroupInvitation(op.param1,[_mid])
                            random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 15:
            if op.param1 in pro["bymsg"]:
                if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                    return
                else:
                    cl.sendMessage(op.param1, wait["leftmsg"])
            if op.param2 in Bots:
                try:
                    time.sleep(0.001)
                    random.choice(K1C).inviteIntoGroup(op.param1,[Smid])
                except:
                    time.sleep(0.001)
                    cl.inviteIntoGroup(op.param1,[Smid])

        if op.type == 17:
            if wait["joinbl"] == True:
                group = cl.getGroup(op.param1)
                gMembMids = [contact.mid for contact in group.members]
                for _mid in gMembMids:
                  if _mid in wait2["blacklist"]:
                    try:
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])

            if op.param1 in pro["wellcome"]:
                if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                    ginfo = cl.getGroup(op.param1)
                    ang = cl.getContact(op.param2)
                    cl.sendMessage(op.param1, "haiii..  " + str(ang.displayName) + "\nWellcome to " + str(ginfo.name) +"\n"+ wait["welmsg"])

        if op.type == 19:
            if op.param1 in pro["Autokick"]:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"] and op.param2 in org["admin"] and op.param2 in org["staff"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                        if op.param3 in Bots or op.param3 in creator or op.param3 in org["owner"] or op.param3 in org["admin"] or op.param3 in org["staff"]:
                            try:
                                random.choice(K2C).findAndAddContactsByMid(op.param3)
                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                            except:
                                random.choice(K2C).findAndAddContactsByMid(op.param3)
                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                    except:
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                        if op.param3 in Bots or op.param3 in creator or op.param3 in org["owner"] or op.param3 in org["admin"] or op.param3 in org["staff"]:
                            try:
                                random.choice(K2C).findAndAddContactsByMid(op.param3)
                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                            except:
                                random.choice(K2C).findAndAddContactsByMid(op.param3)
                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        x = cl.getGroup(op.param1)
                        x.preventedJoinByTicket = False
                        cl.updateGroup(x)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        kf.acceptGroupInvitationByTicket(op.param1,Ti)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        k1.leaveGroup(op.param1)
                    except:
                        k1.acceptGroupInvitation(op.param1)
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.leaveGroup(op.param1)

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                                                random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(K1C).acceptGroupInvitation(op.param1)
                                            except:
                                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                                                random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(K1C).acceptGroupInvitation(op.param1)
                return

            if op.param3 in creator:
                if op.param2 in Bots and op.param2 in creator:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.findAndAddContactsByMid(op.param3)
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.findAndAddContactsByMid(op.param3)
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param3)
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.findAndAddContactsByMid(op.param3)
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.findAndAddContactsByMid(op.param3)
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                                                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                                                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                return

            if op.param3 in org["owner"]:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.findAndAddContactsByMid(op.param3)
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.findAndAddContactsByMid(op.param3)
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param3)
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.findAndAddContactsByMid(op.param3)
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.findAndAddContactsByMid(op.param3)
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                                                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                                                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                return
            if op.param3 in org["admin"]:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"] and op.param2 in org["admin"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.findAndAddContactsByMid(op.param3)
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.findAndAddContactsByMid(op.param3)
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param3)
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.findAndAddContactsByMid(op.param3)
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.findAndAddContactsByMid(op.param3)
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                                                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                                                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                return
            if op.param3 in org["staff"]:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"] and op.param2 in org["admin"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.findAndAddContactsByMid(op.param3)
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.findAndAddContactsByMid(op.param3)
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param3)
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.findAndAddContactsByMid(op.param3)
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.findAndAddContactsByMid(op.param3)
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                                                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    random.choice(K1C).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                                                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                return
            if op.param3 in Bots or op.param3 in creator or op.param3 in org["owner"] or op.param3 in org["admin"] or op.param3 in org["staff"]:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"] and op.param2 in org["admin"] and op.param2 in org["staff"]:
                    random.choice(K1C).findAndAddContactsByMid(op.param3)
                    random.choice(K1C).inviteIntoGroup(op.param1,[op.param3])
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])

#========[ PROTECT CANCEL ]=========#
        if op.type == 32:
            if op.param1 in pro["Protectcancl"]:
                if op.param2 in Bots and op.param2 in creator and op.param2 in org["owner"] and op.param2 in org["admin"] and op.param2 in org["staff"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                        if op.param3 in Bots or op.param3 in creator or op.param3 in org["owner"] or op.param3 in org["admin"] or op.param3 in org["staff"]:
                            try:
                                random.choice(K1C).findAndAddContactsByMid(op.param3)
                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                            except:
                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                    except:
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                        if op.param3 in Bots or op.param3 in creator or op.param3 in org["owner"] or op.param3 in org["admin"] or op.param3 in org["staff"]:
                            try:
                                random.choice(K1C).findAndAddContactsByMid(op.param3)
                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                            except:
                                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])

#========[ KOMANDO START ]========#
        if op.type == 26:
            print ("[25] OP MSSG")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 and msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            if msg.contentType == 13:
              if msg._from in creator:
                if wait["addowner"]==True:
                    if msg.contentMetadata["mid"] in org["owner"]:
                        cl.sendText(msg.to, "𝐰𝐚𝐬 𝐨𝐰𝐧𝐞𝐫")
                        wait["addowner"]=False
                    else:
                        org["owner"][msg.contentMetadata["mid"]] = True
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to, "𝐨𝐰𝐧𝐞𝐫 𝐚𝐝𝐝𝐞𝐝")
                        wait["addowner"]=False

            if msg.contentType == 13:
              if msg._from in creator:
                if wait["delowner"]==True:
                    if msg.contentMetadata["mid"] in org["owner"]:
                        del org["owner"][msg.contentMetadata["mid"]]
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        wait["delowner"]=False
                        cl.sendMessage(msg.to,"𝐬 𝐝𝐞𝐥𝐞𝐭𝐞𝐝")
                    else:
                        cl.sendMessage(msg.to,"𝐒 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝")

#===[ Add admin ☆☆☆ ]

            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"]:
                if wait["addadmin"]==True:
                    if msg.contentMetadata["mid"] in org["admin"]:
                        cl.sendMessage(msg.to, "𝐰𝐚𝐬 𝐚𝐝𝐦𝐢𝐧")
                        wait["addadmin"]=False
                    else:
                        org["admin"][msg.contentMetadata["mid"]] = True
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to, "𝐚𝐝𝐦𝐢𝐧 𝐚𝐝𝐝𝐞𝐝")
                        wait["addadmin"]=False
                        
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"]:
                if wait["deladmin"]==True:
                    if msg.contentMetadata["mid"] in org["admin"]:
                        del org["admin"][msg.contentMetadata["mid"]]
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        wait["deladmin"]=False
                        cl.sendMessage(msg.to,"𝐬 𝐝𝐞𝐥𝐞𝐭𝐞𝐝")
                    else:
                        cl.sendMessage(msg.to,"𝐒 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝")

#====[ Add staff ☆☆☆ ]
                        
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["addstaff"]==True:
                    if msg.contentMetadata["mid"] in org["staff"]:
                        cl.sendMessage(msg.to, "𝐰𝐚𝐬 𝐬𝐭𝐚𝐟𝐟")
                        wait["addstaff"]=False
                    else:
                        org["staff"][msg.contentMetadata["mid"]] = True
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to, "𝐬𝐭𝐚𝐟𝐟 𝐚𝐝𝐝𝐞𝐝")
                        wait["addstaff"]=False
                else:
                    pass
                    
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["delstaff"]==True:
                    if msg.contentMetadata["mid"] in org["staff"]:
                        del org["staff"][msg.contentMetadata["mid"]]
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to,"𝐬𝐭𝐚𝐟𝐟 𝐝𝐞𝐥𝐞𝐭𝐞𝐝")
                        wait["delstaff"]=False
                    else:
                        cl.sendMessage(msg.to,"𝐒𝐭𝐚𝐟𝐟 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝")
                        wait["delstaff"]=False
                else:
                    pass
                    
#========[ BLACKLIST ]============#

            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["ablacklist"]==True:
                    if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        cl.sendMessage(to, "☛ 𝐖𝐚𝐬 𝐁𝐋 𝐛𝐨𝐬𝐬")
                        wait["ablacklist"]=False
                    else:
                        wait2["blacklist"][msg.contentMetadata["mid"]] = True
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "☛ 𝐁𝐥𝐚𝐜𝐤𝐥𝐢𝐬𝐭 𝐒𝐚𝐯𝐞𝐝")
                        wait["ablacklist"]=False

            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["dblacklist"]==True:
                    if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        del wait2["blacklist"][msg.contentMetadata["mid"]]
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "☛ 𝐁𝐥𝐚𝐜𝐤𝐥𝐢𝐬𝐭 𝐑𝐞𝐦𝐨𝐯𝐞𝐝")
                        wait["dblacklist"]=False
                    else:
                        cl.sendMessage(to,"☛ 𝐭𝐚𝐫𝐠𝐞𝐭 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝")
                        wait["dblacklist"]=False

            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["Invi"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cl.sendMessage(msg.to,"-> " + _name + " was here")
                            wait["Invi"] = False
                            break         
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(msg.to,[target])
                            cl.sendMessage(msg.to,"𝐃𝐨𝐧𝐞 𝐈𝐧𝐯𝐢𝐭𝐞 : \n➡" + _name)
                            wait["Invi"] = False
                            break
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["ainv"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ka.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ka.sendMessage(msg.to,"-> " + _name + " was here")
                            wait["ainv"] = False
                            break         
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            ka.findAndAddContactsByMid(target)
                            ka.inviteIntoGroup(msg.to,[target])
                            ka.sendMessage(msg.to,"𝐃𝐨𝐧𝐞 𝐈𝐧𝐯𝐢𝐭𝐞 : \n➡" + _name)
                            wait["ainv"] = False
                            break
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["binv"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = kb.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            kb.sendMessage(msg.to,"-> " + _name + " was here")
                            wait["binv"] = False
                            break         
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            kb.findAndAddContactsByMid(target)
                            kb.inviteIntoGroup(msg.to,[target])
                            kb.sendMessage(msg.to,"𝐃𝐨𝐧𝐞 𝐈𝐧𝐯𝐢𝐭𝐞 : \n➡" + _name)
                            wait["binv"] = False
                            break
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["cinv"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = kc.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            kc.sendMessage(msg.to,"-> " + _name + " was here")
                            wait["cinv"] = False
                            break         
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            kc.findAndAddContactsByMid(target)
                            kc.inviteIntoGroup(msg.to,[target])
                            kc.sendMessage(msg.to,"𝐃𝐨𝐧𝐞 𝐈𝐧𝐯𝐢𝐭𝐞 : \n➡" + _name)
                            wait["cinv"] = False
                            break
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["dinv"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = kd.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            kd.sendMessage(msg.to,"-> " + _name + " was here")
                            wait["dinv"] = False
                            break         
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            kd.findAndAddContactsByMid(target)
                            kd.inviteIntoGroup(msg.to,[target])
                            kd.sendMessage(msg.to,"𝐃𝐨𝐧𝐞 𝐈𝐧𝐯𝐢𝐭𝐞 : \n➡" + _name)
                            wait["dinv"] = False
                            break
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["einv"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ke.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ke.sendMessage(msg.to,"-> " + _name + " was here")
                            wait["einv"] = False
                            break         
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            ke.findAndAddContactsByMid(target)
                            ke.inviteIntoGroup(msg.to,[target])
                            ke.sendMessage(msg.to,"𝐃𝐨𝐧𝐞 𝐈𝐧𝐯𝐢𝐭𝐞 : \n➡" + _name)
                            wait["einv"] = False
                            break
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["finv"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = kf.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            kf.sendMessage(msg.to,"-> " + _name + " was here")
                            wait["finv"] = False
                            break         
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            kf.findAndAddContactsByMid(target)
                            kf.inviteIntoGroup(msg.to,[target])
                            kf.sendMessage(msg.to,"𝐃𝐨𝐧𝐞 𝐈𝐧??𝐢𝐭𝐞 : \n➡" + _name)
                            wait["finv"] = False
                            break

#=====================================================#
        if op.type == 26:
            print ("[26] OP MSSG")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 and msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 7:
                pass
            elif text is None:
                return
            elif msg.toType == 2:
                if msg.text in ["menu1"]:
                  if msg._from in creator:
                    cl.sendMessage(msg.to,helpMessage)

                if msg.text in ["menu2"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    cl.sendMessage(msg.to,helpMessage1)

                if msg.text in ["menu3"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    cl.sendMessage(msg.to,helpMessage2)

                elif msg.text in ["ginfo"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        gCreator = ginfo.creator.displayName
                        if gCreator is None:
                            gCreator = "Error"
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventedJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        try:
                            cl.sendMessage(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)
                        except:
                            cl.sendMessage(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ ginfo.pictureStatus)

                elif msg.text in ["gurl"]: 
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if msg.toType == 2:
                        x = cl.getGroup(msg.to)
                        if x.preventedJoinByTicket == True:
                            cl.sendMessage(msg.to,"𝐪𝐫 𝐧𝐲𝐚 𝐝𝐢 𝐚𝐧𝐮 𝐝𝐮𝐥𝐮 𝐨𝐦")
                        elif x.preventedJoinByTicket == False:
                            cl.updateGroup(x)
                            gurl = cl.reissueGroupTicket(msg.to)
                            cl.sendMessage(msg.to,"line://ti/g/" + gurl)
                        else:
                            pass

                elif msg.text in ["ourl"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    X = cl.getGroup(msg.to)
                    if X.preventedJoinByTicket == False:
                        cl.sendMessage(msg.to,"𝐪𝐫 𝐰𝐚𝐬 𝐨𝐩𝐞𝐧")
                    else:
                        X.preventedJoinByTicket = False
                        cl.updateGroup(X)
                        cl.sendMessage(msg.to,"𝐐𝐑 𝐨𝐩𝐞𝐧")

                elif msg.text in ["curl"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    X = cl.getGroup(msg.to)
                    if X.preventedJoinByTicket == True:
                        cl.sendMessage(msg.to,"𝐪𝐫 𝐰𝐚𝐬 𝐨𝐩𝐞𝐧")
                    else:
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        cl.sendMessage(msg.to,"𝐔𝐫𝐥 𝐢𝐧𝐀𝐜𝐭𝐢𝐯𝐞")

                elif "bcgrup: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"]:
                    bc = msg.text.replace("bcgrup: ","")
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                            cl.sendMessage(i,bc+"\n\n✤𝐋𝐞𝐚𝐊𝐢𝐥𝐥𝐞𝐫✤")
                            cl.sendMessage(msg.to,"𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐁𝐂 𝐁𝐨𝐬𝐐")

                elif "gn: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn: ","")
                        cl.updateGroup(X)

                elif "mid @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                cl.sendMessage(msg.to,str(mention['M']))
                            except Exception as e:
                                pass

                elif "ct @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)

                elif msg.text in ["sp"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        start = time.time()
                        cl.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                        elapsed_time = time.time() - start
                        cl.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start2 = time.time()
                        ka.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                        elapsed_time = time.time() - start2
                        ka.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start3 = time.time()
                        kb.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                        elapsed_time = time.time() - start3
                        kb.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start4 = time.time()
                        kc.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                        elapsed_time = time.time() - start4
                        kc.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start5 = time.time()
                        kd.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                        elapsed_time = time.time() - start5
                        kd.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start6 = time.time()
                        ke.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                        elapsed_time = time.time() - start6
                        ke.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start7 = time.time()
                        kf.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                        elapsed_time = time.time() - start7
                        kf.sendMessage(msg.to, "%s second" % (elapsed_time))
#-------------------------------------------------------------------
                elif msg.text in ["reboot"]:
                    if msg._from in creator:
                        print ("[Command]Like executed")
                        try:
                            cl.sendMessage(msg.to,"𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠...")
                            restart_program()
                        except:
                            cl.sendMessage(msg.to,"𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭")
                            restart_program()
                            pass

                elif msg.text in ["name"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    profile = cl.getProfile()
                    text = profile.displayName + ""
                    cl.sendMessage(msg.to, text)
                    time.sleep(0.15)
                    profile = ka.getProfile()
                    text = profile.displayName + ""
                    ka.sendMessage(msg.to, text)
                    time.sleep(0.15)           
                    profile = kb.getProfile()
                    text = profile.displayName + ""
                    kb.sendMessage(msg.to, text)
                    time.sleep(0.15)
                    profile = kc.getProfile()
                    text = profile.displayName + ""
                    kc.sendMessage(msg.to, text)
                    time.sleep(0.15)           
                    profile = kd.getProfile()
                    text = profile.displayName + ""
                    kd.sendMessage(msg.to, text)
                    time.sleep(0.15)
                    profile = ke.getProfile()
                    text = profile.displayName + ""
                    ke.sendMessage(msg.to, text)
                    time.sleep(0.15)
                    profile = kf.getProfile()
                    text = profile.displayName + ""
                    kf.sendMessage(msg.to, text)

                elif msg.text in ["respon"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                      cl.sendMessage(msg.to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                      ka.sendMessage(msg.to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                      kb.sendMessage(msg.to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                      kc.sendMessage(msg.to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                      kd.sendMessage(msg.to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                      ke.sendMessage(msg.to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                      kf.sendMessage(msg.to, "𝐊𝐚𝐦𝐢 𝐬𝐢𝐚𝐩 𝐦𝐞𝐧𝐞𝐫𝐢𝐦𝐚 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")

                elif msg.text in ["bot:restart"]:
                    if msg._from in creator:
                        cl.sendMessage(msg.to, "𝐁𝐨𝐭 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝")
                        restart_program()
                        print ("@Restart" )            

                elif msg.text in ["runtime"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    eltime = time.time() - mulai
                    van = "Bot run "+waktu(eltime)
                    cl.sendMessage(msg.to,van)
                    ka.sendMessage(msg.to,van)
                    kb.sendMessage(msg.to,van)
                    kc.sendMessage(msg.to,van)
                    kd.sendMessage(msg.to,van)
                    ke.sendMessage(msg.to,van)
                    kf.sendMessage(msg.to,van)

                elif msg.text in ["kickall"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        group = ka.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        for x in nama:
                            if x not in Bots:
                                if x not in creator:
                                    if x not in org["owner"]:
                                        if x not in org["admin"]:
                                            if x not in org["staff"]:
                                                try:
                                                    anu=[cl,ka,kb,kc,kd,ke,kf]
                                                    nenen=random.choice(anu)
                                                    nenen.kickoutFromGroup(msg.to,[x])
                                                    time.sleep(0.1)
                                                except:
                                                    pass

                elif "kiss @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                cl.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                pass

                elif "l1kick @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ka.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                pass

                elif "l2kick @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                kb.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                pass

                elif "l3kick @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                kc.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                pass

                elif "l4kick @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                kd.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                pass

                elif "l5kick @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ke.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                pass

                elif "l6kick @" in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                kf.kickoutFromGroup(msg.to, [mention['M']])							
                            except:
                                pass

                elif msg.text in ["cancel"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    group = cl.getGroup(msg.to)
                    if group.invitee is None:
                        cl.sendMessage(op.message.to, "╔══════════════\n╠☛ 𝐧𝐨 𝐨𝐧𝐞 𝐢𝐬 𝐢𝐧𝐯𝐢𝐭𝐢𝐧𝐠\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            cl.cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        cl.sendMessage(to, "done.")

                elif msg.text in ["Lcancel"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    group = ka.getGroup(msg.to)
                    group = kb.getGroup(msg.to)
                    group = kc.getGroup(msg.to)
                    group = kd.getGroup(msg.to)
                    group = ke.getGroup(msg.to)
                    group = kf.getGroup(msg.to)
                    if group.invitee is None:
                        random.choice(K2C).sendMessage(op.message.to, "╔══════════════\n╠☛ 𝐧𝐨 𝐨𝐧𝐞 𝐢𝐬 𝐢𝐧𝐯𝐢𝐭𝐢𝐧𝐠\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            random.choice(K2C).cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        random.choice(K2C).sendMessage(to, "done.")

#-------------------------------------------------------
                elif msg.text in ["protection on"]:
                    if msg._from in creator or msg._from in org["owner"]:
                        pro["Protectgr"][msg.to] = True
                        pro["Protectcancl"][msg.to] = True
                        pro["Protectinvite"][msg.to] = True
                        pro["Autokick"][msg.to] = True
                        with open('pro.json','w') as fp:
                            json.dump(pro, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to,"𝐇𝐢𝐠𝐡 𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐧")
                        ka.sendMessage(msg.to,"𝐇𝐢𝐠𝐡 𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐧")
                        kb.sendMessage(msg.to,"𝐇𝐢𝐠𝐡 𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐧")
                        kc.sendMessage(msg.to,"𝐇𝐢𝐠𝐡 𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐧")
                        kd.sendMessage(msg.to,"𝐇𝐢𝐠𝐡 𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐧")
                        ke.sendMessage(msg.to,"𝐇𝐢𝐠𝐡 𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐧")
                        kf.sendMessage(msg.to,"𝐇𝐢𝐠𝐡 𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐧")

                elif msg.text in ["protection off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    if msg.to in pro["Protectgr"]:
                        try:
                            del pro["Protectgr"][msg.to]
                        except:
                            pass
                    if msg.to in pro["Protectcancl"]:
                        try:
                            del pro["Protectcancl"][msg.to]
                        except:
                            pass
                    if msg.to in pro["Protectinvite"]:
                        try:
                            del pro["Protectinvite"][msg.to]
                        except:
                            pass
                    if msg.to in pro["Autokick"]:
                        try:
                            del pro["Autokick"][msg.to]
                        except:
                            pass
                    with open('pro.json','w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐟𝐟")
                    ka.sendMessage(msg.to,"𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐟𝐟")
                    kb.sendMessage(msg.to,"𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐟𝐟")
                    kc.sendMessage(msg.to,"𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐟𝐟")
                    kd.sendMessage(msg.to,"𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐟𝐟")
                    ke.sendMessage(msg.to,"𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐟𝐟")
                    kf.sendMessage(msg.to,"𝐀𝐥𝐥 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐎𝐟𝐟")
#---------------------------------------------------------
                elif msg.text in ["proinvite on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    pro["Protectinvite"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐈𝐧𝐯𝐢𝐭𝐞 𝐨𝐧 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧")

                elif msg.text in ["proinvite off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    del pro["Protectinvite"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐈𝐧𝐯𝐢𝐭𝐞 𝐮𝐧𝐩𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧")

#--------------------------------------------------------
                elif msg.text in ["proqr on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    pro["Protectgr"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐐𝐫 𝐢𝐧 𝐩𝐫𝐨𝐭𝐞𝐜𝐭")

                elif msg.text in ["proqr off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    del pro["Protectgr"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐐𝐫 𝐮𝐧𝐩𝐫𝐨𝐭𝐞𝐜𝐭")

                elif msg.text in ["procancel on"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    pro["Protectcancl"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to," 𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐂𝐚𝐧𝐜??𝐥 𝐨𝐧")

                elif msg.text in ["procancel off"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    del pro["Protectcancl"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐏𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐨𝐧 𝐂𝐚𝐧𝐜𝐞𝐥 𝐨𝐟𝐟")

                elif msg.text in ["prokick on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    pro["Autokick"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐀𝐮𝐭𝐨 𝐊𝐢𝐜𝐤 𝐢𝐧 𝐀𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝")

                elif msg.text in ["prokick off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    pro["Autokick"][msg.to]=False
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐀𝐮𝐭𝐨 𝐊𝐢𝐜𝐤 𝐧𝐨𝐭 𝐀𝐜𝐭𝐢𝐯𝐞")

                elif msg.text in ["autojoin on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["autoJoin"]=True
                    cl.sendMessage(msg.to,"𝐀𝐮𝐭𝐨 𝐣𝐨𝐢𝐧 𝐢𝐧 𝐀𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝")

                elif msg.text in ["autojoin off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["autoJoin"]=False
                    cl.sendMessage(msg.to,"𝐀𝐮𝐭𝐨 𝐣𝐨𝐢𝐧 𝐧𝐨𝐭 𝐀𝐜𝐭𝐢𝐯𝐞")

                elif msg.text in ["autoleft on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["autoLeave"]=True
                    cl.sendMessage(msg.to,"𝐀𝐮𝐭𝐨 𝐋𝐞𝐚𝐯𝐞 𝐢𝐧 𝐀𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝")

                elif msg.text in ["autoleft off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["autoLeave"]=False
                    cl.sendMessage(msg.to,"𝐀𝐮𝐭𝐨 𝐋𝐞𝐚𝐯𝐞 𝐧𝐨𝐭 𝐀𝐜𝐭𝐢𝐯𝐞")

                elif msg.text in ["left on"]:
                    pro["bymsg"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ 𝐦𝐬𝐠 𝐥𝐞𝐟𝐭 𝐨𝐧\n╚════════════")

                elif msg.text in ["left off"]:
                    del pro["bymsg"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ 𝐦𝐬𝐠 𝐥𝐞𝐟𝐭 𝐨𝐟𝐟\n╚════════════")

                elif msg.text in ["welcome on"]:
                    pro["wellcome"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ 𝐬𝐚𝐦𝐛𝐮𝐭𝐚𝐧 𝐨𝐧\n╚════════════")

                elif msg.text in ["welcome off"]:
                    del pro["wellcome"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ 𝐬𝐚𝐦𝐛𝐮𝐭𝐚𝐧 𝐨𝐟𝐟\n╚════════════")

                elif msg.text in ["rechat"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    try:
                        cl.removeAllMessages(op.param2)
                        cl.sendMessage(to,"𝐩𝐞𝐬𝐚𝐧 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐡𝐚𝐩𝐮𝐬 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                        ka.removeAllMessages(op.param2)
                        ka.sendMessage(to,"𝐩𝐞𝐬𝐚𝐧 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐡𝐚𝐩𝐮𝐬 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                        kb.removeAllMessages(op.param2)
                        kb.sendMessage(to,"𝐩𝐞𝐬𝐚𝐧 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐡𝐚𝐩𝐮𝐬 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                        kc.removeAllMessages(op.param2)
                        kc.sendMessage(to,"𝐩𝐞𝐬𝐚𝐧 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐡𝐚𝐩𝐮𝐬 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                        kd.removeAllMessages(op.param2)
                        kd.sendMessage(to,"𝐩𝐞𝐬𝐚𝐧 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐡𝐚𝐩𝐮𝐬 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                        ke.removeAllMessages(op.param2)
                        ke.sendMessage(to,"𝐩𝐞𝐬𝐚𝐧 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐡𝐚𝐩𝐮𝐬 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                        kf.removeAllMessages(op.param2)
                        kf.sendMessage(to,"𝐩𝐞𝐬𝐚𝐧 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐡𝐚𝐩𝐮𝐬 𝐛𝐨𝐬𝐬𝐪𝐮𝐡...")
                    except:
                        pass

                elif msg.text in ["reset grup"]:
                  if msg._from in creator: 
                    if msg.to in pro["Protectgr"]:
                        try:
                            del pro["Protectgr"][msg.to]
                        except:
                            pass
                    if msg.to in pro["Protectinvite"]:
                        try:
                           del pro["Protectinvite"][msg.to]
                        except:
                            pass
                    if msg.to in pro["Protectcancl"]:
                        try:
                            del pro["Protectcancl"][msg.to]
                        except:
                            pass
                    if msg.to in pro["Autokick"]:
                        try:
                            del pro["Autokick"][msg.to]
                        except:
                            pass
                    if msg.to in pro["bymsg"]:
                        try:
                            del wait["bymsg"][msg.to]
                        except:
                            pass
                    if msg.to in pro["wellcome"]:
                        try:
                            del wait['wellcome'][msg.to]
                        except:
                            pass
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐝𝐨𝐧𝐞")

                elif msg.text in ["grup set"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    md = ""
                    if msg.to in pro["Protectgr"]: md+="╠ ➽ 𝐏𝐫𝐨𝐭𝐞𝐜𝐭 𝐠𝐫𝐮𝐩 : ✔\n"
                    else: md +="╠ ➽ 𝐏𝐫𝐨𝐭𝐞𝐜𝐭 𝐠𝐫𝐮𝐩 : ❌\n"
                    if msg.to in pro["Protectcancl"]: md+="╠ ➽ 𝐏𝐫𝐨𝐭𝐞𝐜𝐭 𝐜𝐚𝐧𝐜𝐞𝐥 : ✔\n"
                    else: md+= "╠ ➽ 𝐏𝐫𝐨𝐭𝐞𝐜𝐭 𝐜𝐚𝐧𝐜𝐞𝐥 : ❌\n"
                    if msg.to in pro["Protectinvite"]: md+="╠ ➽ 𝐏𝐫𝐨𝐭𝐞𝐜𝐭 𝐢𝐧𝐯𝐢𝐭𝐞 : ✔\n"
                    else: md+= "╠ ➽ 𝐏𝐫𝐨𝐭𝐞𝐜𝐭 𝐢𝐧𝐯𝐢𝐭𝐞 : ❌\n"
                    if msg.to in pro["Autokick"]: md+="╠ ➽ 𝐚𝐮𝐭𝐨 𝐤𝐢𝐜𝐤 : ✔\n"
                    else:md+="╠ ➽ 𝐚𝐮𝐭𝐨 𝐤𝐢𝐜𝐤 : ❌\n"
                    if msg.to in pro["wellcome"]: md+="╠ ➽ 𝐰𝐞𝐥𝐥𝐜𝐨𝐦𝐞 𝐭𝐞𝐤𝐬 : ✔\n"
                    else:md+="╠ ➽ 𝐰𝐞𝐥𝐥𝐜𝐨𝐦𝐞 𝐭𝐞𝐤𝐬 : ❌\n"
                    if msg.to in pro["bymsg"]: md+="╠ ➽ 𝐥𝐞𝐟𝐭 𝐭𝐞𝐤𝐬 : ✔\n"
                    else:md+="╠ ➽ 𝐥𝐞𝐟𝐭 𝐭𝐞𝐤𝐬 : ❌\n"
                    cl.sendMessage(msg.to,"╔══════════════\n╠⟦ 𝐆𝐫𝐮𝐩 𝐬𝐞𝐭 𝐮𝐩 ⟧\n╔══════════════\n"+ md +"╚══════════════")

                elif msg.text in ["add off"]:
                  if msg._from in creator:
                    wait["Invi"]=False
                    wait["ainv"]=False
                    wait["binv"]=False
                    wait["cinv"]=False
                    wait["dinv"]=False
                    wait["einv"]=False
                    wait["finv"]=False
                    wait["addowner"]=False
                    wait["delowner"]=False
                    wait["addadmin"]=False
                    wait["deladmin"]=False
                    wait["addstaff"]=False
                    wait["delstaff"]=False
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"all add off")

                elif msg.text in ["status"]:
                  if msg._from in creator:
                    md = ""
                    if wait["midct"] == True: md+="╠ ➽ 𝐦𝐢𝐝𝐜𝐭 : ✔\n"
                    else:md+="╠ ➽ 𝐦𝐢𝐝𝐜𝐭 : ❌\n"
                    if wait["spamr"] == True: md+="╠ ➽ 𝐬𝐩𝐚𝐦 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 : ✔\n"
                    else:md+="╠ ➽ 𝐬𝐩𝐚𝐦 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 : ❌\n"
                    if wait["Invi"] == True: md+="╠ ➽ 𝐢𝐧𝐯𝐢 : ✔\n"
                    else:md+="╠ ➽ 𝐢𝐧𝐯𝐢 : ❌\n"
                    if wait["LikeOn"] == True: md+="╠ ➽ 𝐋𝐢𝐤𝐞 : ✔\n"
                    else:md+="╠ ➽ 𝐋𝐢𝐤𝐞 : ❌\n"
                    if wait["Timeline"] == True: md+="╠ ➽ 𝐆𝐞𝐭 𝐩𝐨𝐬𝐭 : ✔\n"
                    else:md+="╠ ➽ 𝐆𝐞𝐭 𝐩𝐨𝐬𝐭 : ❌\n"
                    cl.sendMessage(msg.to,"╔══════════════\n╠⟦ 𝐒𝐞𝐥𝐟 𝐬𝐭𝐚𝐭𝐮𝐬 ⟧\n╔══════════════\n"+ md +"╚══════════════")

                elif msg.text in ["add owner"]:
                    if msg._from in creator:
                        wait["addowner"]=True
                        cl.sendMessage(msg.to, "𝐬𝐞𝐧𝐝 𝐜𝐨𝐧𝐭𝐚𝐜𝐭")

                elif msg.text in ["del owner"]:
                    if msg._from in creator:
                        wait["delowner"]=True
                        cl.sendMessage(msg.to, "𝐬𝐞𝐧𝐝 𝐜𝐨𝐧𝐭𝐚𝐜𝐭")

                elif msg.text in ["clear owner"]:
                  if msg._from in creator:
                    org["owner"] = {}
                    with open('org.json', 'w') as fp:
                        json.dump(org, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"𝐒𝐮𝐜𝐜𝐞𝐬 𝐜𝐥𝐞𝐚𝐫")

                elif msg.text in ["owner list"]:
                  if msg._from in creator:
                    if org["owner"] == {}:
                        cl.sendMessage(msg.to,"𝐞𝐦𝐩𝐭𝐲 𝐓𝐥𝐢𝐬𝐭")
                    else:
                        mc = []
                        for mi_d in org["owner"]:
                            mc.append(mi_d)
                        pass
                        cban = cl.getContacts(mc)
                        nban = []
                        for x in range(len(cban)):
                            nban.append(cban[x].displayName)
                        pass
                        jo = "\n╠ ➽ ".join(str(i) for i in nban)
                        cl.sendMessage(msg.to,"╔══════════════\n╠⟦ 𝐎𝐰𝐧𝐞𝐫 𝐋𝐢𝐬𝐭 ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")

                elif msg.text in ["add owner "]:
                    if msg._from in creator:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:    
                            if target in org["owner"]:
                                cl.sendMessage(msg.to,"𝐰𝐚𝐬 𝐨𝐰𝐧𝐞𝐫")
                                pass
                            else:
                                try:
                                    org["owner"][target] = True
                                    with open('org.json','w') as fp:
                                        json.dump(org, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(msg.to,"𝐬𝐮𝐜𝐜𝐞𝐬 𝐚𝐝𝐝𝐞𝐝 𝐨𝐰𝐧𝐞𝐫")
                                except Exception as e:
                                    cl.sendMessage(msg.to,"𝐄𝐫𝐨𝐫𝐫.....")

                elif msg.text in ["add admin"]:
                    if msg._from in creator or msg._from in org["owner"]:
                        wait["addadmin"]=True
                        cl.sendMessage(msg.to, "𝐬𝐞𝐧𝐝 𝐜𝐨𝐧𝐭𝐚𝐜𝐭")
                elif msg.text in ["Del admin"]:
                    if msg._from in creator or msg._from in org["owner"]:
                        wait["deladmin"]=True
                        cl.sendMessage(msg.to, "𝐬𝐞𝐧𝐝 𝐜𝐨𝐧𝐭𝐚𝐜𝐭")

                elif msg.text in ["clear admin"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    org["admin"] = {}
                    with open('org.json', 'w') as fp:
                        json.dump(org, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"Succes clear")

                elif msg.text in ["admin list"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    if org["admin"] == {}:
                        cl.sendText(msg.to,"empty Tlist")
                    else:
                        mc = []
                        for mi_d in org["admin"]:
                            mc.append(mi_d)
                        pass
                        cban = cl.getContacts(mc)
                        nban = []
                        for x in range(len(cban)):
                            nban.append(cban[x].displayName)
                        pass
                        jo = "\n╠ ➽ ".join(str(i) for i in nban)
                        cl.sendMessage(msg.to,"╔══════════════\n╠⟦ Admin List ⟧\n╔══════════════\n╠ ➽ %s\n╚══════════════\n╠⟦ Total: %s ⟧\n"%(jo,str(len(cban)))+"╚══════════════")

                elif msg.text in ["add staff"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["addstaff"]=True
                        cl.sendMessage(msg.to, "send contact")
                elif msg.text in ["Del staff"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["delstaff"]=True
                        cl.sendMessage(msg.to, "send contact")

                elif msg.text in ["clear staff"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    org["staff"] = {}
                    with open('org.json', 'w') as fp:
                        json.dump(org, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"Succes clear")

                elif msg.text in ["staff list"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if org["staff"] == {}:
                        cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                    else:
                        mc = "╔══════════════\n╠☛ ❲ Friend List ❳☚\n╠══════════════"
                        for mi_d in org["staff"]:
                            mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══════════════")

#=======[ ADD BLACKLIST ]=======#
                elif msg.text in ["cban"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    wait2['blacklist'] = {}
                    with open('wait2.json', 'w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"°done boss")
                elif msg.text in ["addban"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["ablacklist"]=True
                        cl.sendMessage(to, "please send contact")

                elif msg.text in ["delban"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["dblacklist"]=True
                        cl.sendMessage(to, "please send contact")

                elif msg.text in ["banlist"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if wait2["blacklist"] == {}:
                        cl.sendMessage(to,"☛ empty list")
                    else:
                        mc = "╔══════════════\n╠☛ ❲ BanList ❳☚\n╠══════════════"
                        for mi_d in wait2["blacklist"]:
                            mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══════════════")

                elif msg.text in ["list member"]:   
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    kontak = cl.getGroup(msg.to)
                    group = kontak.members
                    msgs="╔══════════════\n╠☛❲ Member List ❳☚\n╠══════════════"
                    for ids in group:
                        msgs+="\n╠☛ %s" % (ids.displayName)
                    msgs+="\n╠══════════════\n╠☛❲ Total Members : %i ❳☚\n" % len(group)+"╚══════════════"
                    cl.sendMessage(to, msgs)

                elif msg.text in ["gift"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    cl.sendMessage(to, "👇👇.For U°°°°")
                    cl.sendMessage(to, None, contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
#=================================#
                elif "sider: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    wait["cctvteks"] = msg.text.replace("sider: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")  

                elif msg.text in ["check msg"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    cl.sendMessage(to,"msg add: \n══════════════\n" + wait["message"] + "\n══════════════")
                    cl.sendMessage(to,"msg sider: \n══════════════\n" + wait["cctvteks"] + "\n══════════════")
                    cl.sendMessage(to,"msg leave: \n══════════════\n" + wait["leftmsg"] + "\n══════════════")
                    cl.sendMessage(to,"msg welcome: \n══════════════\n" + wait["welmsg"] + "\n══════════════")
#===================#
                elif "left: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    wait["leftmsg"] = msg.text.replace("left: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")   

                elif "welcome: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    wait["welmsg"] = msg.text.replace("welcome: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")   
#=================#
                elif "add: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["message"] = msg.text.replace("add: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")   

                elif msg.text in ["sepi","list"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"] or msg._from in org["staff"]:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 20:
                        summon(msg.to, nama)
                    if jml > 20 and jml < 40:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(20, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 40  and jml < 60:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(20, 40):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(40, 60):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(40, 60):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(60, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 80:
                         print ("Terlalu Banyak Men 500+")

                elif msg.text in ["lurk on"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         wait2['readPoint'][msg.to] = msg_id
                         wait2['readMember'][msg.to] = {}
                         cl.sendMessage(msg.to, "Lurking mode on\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                elif msg.text in ["lurk off"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         del wait2['readPoint'][msg.to]
                         del wait2['readMember'][msg.to]
                         cl.sendMessage(msg.to, "Lurking mode off\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                elif msg.text in ["lurkers"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                       if msg.to in wait2['readPoint']:
                           if wait2['readMember'][msg.to] != {}:
                               aa = []
                               for x in wait2['readMember'][msg.to]:
                                   aa.append(x)
                               try:
                                   arrData = ""
                                   textx = "  [ Result Sider Member ]    \n\n      [ Lurking ]\n1. ".format(str(len(aa)))
                                   arr = []
                                   no = 1
                                   b = 1
                                   for i in aa:
                                       b = b + 1
                                       end = "\n"
                                       mention = "@x\n"
                                       slen = str(len(textx))
                                       elen = str(len(textx) + len(mention) - 1)
                                       arrData = {'S':slen, 'E':elen, 'M':i}
                                       arr.append(arrData)
                                       tz = pytz.timezone("Asia/Jakarta")
                                       timeNow = datetime.now(tz=tz)
                                       textx += mention
                                       if no < len(aa):
                                           no += 1
                                           textx += str(b) + ". "
                                       else:
                                           try:
                                               no = " {} ".format(str(cl.getGroup(msg.to).name))
                                           except:
                                               no = "  "
                                   msg.to = msg.to
                                   msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                   msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                   msg.contentType = 0
                                   cl.sendMessage1(msg)
                               except:
                                   pass
                               try:
                                   del wait2['readPoint'][msg.to]
                                   del wait2['readMember'][msg.to]
                               except:
                                   pass
                               wait2['readPoint'][msg.to] = msg.id
                               wait2['readMember'][msg.to] = {}
                           else:
                               cl.sendMessage(msg.to, "°no sider•••")
                       else:
                           cl.sendMessage(msg.to, "please create lurk on")

                elif msg.text in ["sider on"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                      try:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          cl.sendMessage(msg.to, "╔══════════════\n╠☛ starting cek sider\n╚══════════════\n╔══════════════\n╠☛ date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠☛ hour "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚══════════════")
                          del ciduk['ceadPoint'][msg.to]
                          del ciduk['ceadMember'][msg.to]
                          del ciduk['cyduk'][msg.to]
                      except:
                          pass
                      ciduk['ceadPoint'][msg.to] = msg.id
                      ciduk['ceadMember'][msg.to] = ""
                      ciduk['cyduk'][msg.to]=True

                elif msg.text in ["sider off"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                       if msg.to in ciduk['ceadPoint']:
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           ciduk['cyduk'][msg.to]=False
                           cl.sendMessage(msg.to, "╔══════════════\n╠☛ sider off mode\n╚══════════════")
                       else:
                           cl.sendMessage(msg.to, "done off°")

                elif msg.text in ["grup"]:
                    if msg._from in creator:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = cl.getGroup(i).name
                            h += "╠ ➽ %s\n" % (gn)
                        cl.sendMessage(msg.to,"╔══════════════\n╠⟦ My grup ⟧\n╔══════════════\n"+ h +"╚══════════════")
                elif msg.text in ["L1grup"]:
                    if msg._from in creator:
                        gid = ka.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = ka.getGroup(i).name
                            h += "╠ ➽ %s\n" % (gn)
                        ka.sendMessage(msg.to,"╔══════════════\n╠⟦ My grup ⟧\n╔══════════════\n"+ h +"╚══════════════")

                elif msg.text in ["l2grup"]:
                    if msg._from in creator:
                        gid = kb.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kb.getGroup(i).name
                            h += "╠ ➽ %s\n" % (gn)
                        kb.sendMessage(msg.to,"╔══════════════\n╠⟦ My grup ⟧\n╔══════════════\n"+ h +"╚══════════════")
                elif msg.text in ["l3grup"]:
                    if msg._from in creator:
                        gid = kc.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kc.getGroup(i).name
                            h += "╠ ➽ %s\n" % (gn)
                        kc.sendMessage(msg.to,"╔══════════════\n╠⟦ My grup ⟧\n╔══════════════\n"+ h +"╚══════════════")

                elif msg.text in ["l4grup"]:
                    if msg._from in creator:
                        gid = kd.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kd.getGroup(i).name
                            h += "╠ ➽ %s\n" % (gn)
                        kd.sendMessage(msg.to,"╔══════════════\n╠⟦ My grup ⟧\n╔══════════════\n"+ h +"╚══════════════")
                elif msg.text in ["l5grup"]:
                    if msg._from in creator:
                        gid = ke.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = ke.getGroup(i).name
                            h += "╠ ➽ %s\n" % (gn)
                        ke.sendMessage(msg.to,"╔══════════════\n╠⟦ My grup ⟧\n╔══════════════\n"+ h +"╚══════════════")
                elif msg.text in ["l6grup"]:
                    if msg._from in creator:
                        gid = kf.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kf.getGroup(i).name
                            h += "╠ ➽ %s\n" % (gn)
                        kf.sendMessage(msg.to,"╔══════════════\n╠⟦ My grup ⟧\n╔══════════════\n"+ h +"╚══════════════")

                elif "linv to " in msg.text:
                  if msg._from in creator:
                    ng = msg.text.replace("Zinv to ","")
                    gid = cl.getGroupIdsJoined()
                    x = msg._from
                    for i in gid:
                            h = cl.getGroup(i).name
                            if h == ng:
                                cl.inviteIntoGroup(i,[x])
                                cl.sendMessage(msg.to,"Success join to ["+ h +"] group")
                            else:
                                pass
                                
                elif "l1inv to " in msg.text:
                  if msg._from in creator:
                    ng = msg.text.replace("l1inv to ","")
                    gid = ka.getGroupIdsJoined()
                    x = msg._from
                    for i in gid:
                            h = ka.getGroup(i).name
                            if h == ng:
                                ka.inviteIntoGroup(i,[x])
                                ka.sendMessage(msg.to,"Success join to ["+ h +"] group")
                            else:
                                pass
                elif "l2inv to " in msg.text:
                  if msg._from in creator:
                    ng = msg.text.replace("l2inv to ","")
                    gid = kb.getGroupIdsJoined()
                    x = msg._from
                    for i in gid:
                            h = kb.getGroup(i).name
                            if h == ng:
                                kb.inviteIntoGroup(i,[x])
                                kb.sendMessage(msg.to,"Success join to ["+ h +"] group")
                            else:
                                pass
                elif "l3inv to " in msg.text:
                  if msg._from in creator:
                    ng = msg.text.replace("l3inv to ","")
                    gid = kc.getGroupIdsJoined()
                    x = msg._from
                    for i in gid:
                            h = kc.getGroup(i).name
                            if h == ng:
                                kc.inviteIntoGroup(i,[x])
                                kc.sendMessage(msg.to,"Success join to ["+ h +"] group")
                            else:
                                pass
                elif "l4inv to " in msg.text:
                  if msg._from in creator:
                    ng = msg.text.replace("l4inv to ","")
                    gid = kd.getGroupIdsJoined()
                    x = msg._from
                    for i in gid:
                            h = kd.getGroup(i).name
                            if h == ng:
                                kd.inviteIntoGroup(i,[x])
                                kd.sendMessage(msg.to,"Success join to ["+ h +"] group")
                            else:
                                pass
                elif "l5inv to " in msg.text:
                  if msg._from in creator:
                    ng = msg.text.replace("l5inv to ","")
                    gid = ke.getGroupIdsJoined()
                    x = msg._from
                    for i in gid:
                            h = ke.getGroup(i).name
                            if h == ng:
                                ke.inviteIntoGroup(i,[x])
                                ke.sendMessage(msg.to,"Success join to ["+ h +"] group")
                            else:
                                pass
                elif "l6inv to " in msg.text:
                  if msg._from in creator:
                    ng = msg.text.replace("l5inv to ","")
                    gid = kf.getGroupIdsJoined()
                    x = msg._from
                    for i in gid:
                            h = kf.getGroup(i).name
                            if h == ng:
                                kf.inviteIntoGroup(i,[x])
                                kf.sendMessage(msg.to,"Success join to ["+ h +"] group")
                            else:
                                pass

                elif "lcn: " in msg.text:
                  if msg._from in creator:
                    x = cl.getProfile()
                    x.displayName = msg.text.replace("lcn: ","")
                    cl.updateProfile(x)
                    cl.sendMessage(msg.to, " done")
                elif "l1cn: " in msg.text:
                  if msg._from in creator:
                    x = ka.getProfile()
                    x.displayName = msg.text.replace("l1cn: ","")
                    ka.updateProfile(x)
                    ka.sendMessage(msg.to, " done")
                elif "l2cn: " in msg.text:
                  if msg._from in creator:
                    x = kb.getProfile()
                    x.displayName = msg.text.replace("l2cn: ","")
                    kb.updateProfile(x)
                    kb.sendMessage(msg.to, " done")
                elif "l3cn: " in msg.text:
                  if msg._from in creator:
                    x = kc.getProfile()
                    x.displayName = msg.text.replace("l3cn: ","")
                    kc.updateProfile(x)
                    kc.sendMessage(msg.to, " done")
                elif "l4cn: " in msg.text:
                  if msg._from in creator:
                    x = kd.getProfile()
                    x.displayName = msg.text.replace("l4cn: ","")
                    kd.updateProfile(x)
                    kd.sendMessage(msg.to, " done")
                elif "l5cn: " in msg.text:
                  if msg._from in creator:
                    x = ke.getProfile()
                    x.displayName = msg.text.replace("l5cn: ","")
                    ke.updateProfile(x)
                    ke.sendMessage(msg.to, " done")
                elif "l6cn: " in msg.text:
                  if msg._from in creator:
                    x = kf.getProfile()
                    x.displayName = msg.text.replace("l6cn: ","")
                    kf.updateProfile(x)
                    kf.sendMessage(msg.to, " done")

                elif "leave grup " in msg.text:
                  if msg._from in creator:
                    ng = msg.text.replace("leave grup ","")
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                        h = cl.getGroup(i).name
                        if h == ng:
                            ka.sendMessage(i,"Bot di paksa keluar oleh owner!")
                            cl.leaveGroup(i)
                            ka.leaveGroup(i)
                            kb.leaveGroup(i)
                            kc.leaveGroup(i)
                            kd.leaveGroup(i)
                            ke.leaveGroup(i)
                            kf.leaveGroup(i)
                            cl.sendMessage(msg.to,"Success left ["+ h +"] group")
                        else:
                            pass

                elif msg.text in ["out all grup"]:
                  if msg._from in creator:
                    gid = ki.getGroupIdsJoined()
                    for i in gid:
                        ka.sendMessage(i,"Bot di paksa keluar oleh owner!")
                        cl.leaveGroup(i)
                        ka.leaveGroup(i)
                        kb.leaveGroup(i)
                        kc.leaveGroup(i)
                        kd.leaveGroup(i)
                        ke.leaveGroup(i)
                        kf.leaveGroup(i)
                        cl.sendMessage(msg.to,"Success left all group")

                elif msg.text in ["invite"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["Invi"] = True
                        cl.sendMessage(msg.to,"send contact")

                elif msg.text in ["l1invite"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["ainv"] = True
                        ka.sendMessage(msg.to,"send contact")

                elif msg.text in ["l2invite"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["binv"] = True
                        kb.sendMessage(msg.to,"send contact")

                elif msg.text in ["l3invite"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["cinv"] = True
                        kc.sendMessage(msg.to,"send contact")

                elif msg.text in ["l4invite"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["dinv"] = True
                        kd.sendMessage(msg.to,"send contact")

                elif msg.text in ["l5invite"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["einv"] = True
                        ke.sendMessage(msg.to,"send contact")

                elif msg.text in ["l6invite"]:
                    if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait["finv"] = True
                        ke.sendMessage(msg.to,"send contact")

                elif msg.text in ["L34","masuk"]:
                    if msg._from in creator or msg._from in org["owner"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                elif msg.text in ["all inv"]:
                    if msg._from in creator or msg._from in org["owner"]:
                        cl.inviteIntoGroup(msg.to,[Amid,Bmid,Cmid,Dmid,Emid,Fmid])
                        ka.acceptGroupInvitation(msg.to)
                        kb.acceptGroupInvitation(msg.to)
                        kc.acceptGroupInvitation(msg.to)
                        kd.acceptGroupInvitation(msg.to)
                        ke.acceptGroupInvitation(msg.to)
                        kf.acceptGroupInvitation(msg.to)

                elif msg.text in ["jsjoin"]:
                    if msg._from in creator or msg._from in org["owner"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)

                elif msg.text in ["jsstay"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    try:
                        znf = [Smid]
                        cl.inviteIntoGroup(msg.to, znf)
                    except:
                        pass

                elif msg.text in ["jskuy"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    try:
                        znf = [Smid]
                        random.choice(K2C).inviteIntoGroup(msg.to, znf)
                    except:
                        pass

                elif msg.text in ["jsbye"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    if msg.toType == 2:
                        ginfo = k1.getGroup(msg.to)
                        try:
                            k1.leaveGroup(msg.to)
                        except:
                            pass
                elif msg.text in ["Bye"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                            ka.leaveGroup(msg.to)
                            kb.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kd.leaveGroup(msg.to)
                            ke.leaveGroup(msg.to)
                            kf.leaveGroup(msg.to)
                        except:
                            pass

#=====================#
        if op.type == 55:
            try:
                if op.param1 in wait2["readPoint"]:
                   if op.param2 in wait2["readMember"][op.param1]:
                       pass
                   else:
                       wait2["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if ciduk['cyduk'][op.param1]==True:
                if op.param1 in ciduk['ceadPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in ciduk['ceadMember'][op.param1]:
                        pass
                    else:
                        ciduk['ceadMember'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

        if op.type == 59:
            print (op)

    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e) 

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
π₯βββββ¦ RATU JS β§ββββπ₯
β¬β¬βββββββββββββββββ¬
β¬β¬ β½  menu
β¬β¬ β½  js stay
β¬β¬ β½  js kuy
β¬β¬ β½  js join
β¬β¬ β½  js bye
β¬β¬ β½  ourl
β¬β¬ β½  curl
β¬β¬ β½  grup
β¬β¬ β½  ngrup
β¬β¬ β½  inv toγnama grupγ
β¬β¬ β½  L1-6 inv toγnama grupγ
β¬β¬ β½  Lcn:γnamaγ
β¬β¬ β½  L1-6 cn:γnamaγ
β¬β¬ β½  Zonkγ@γ
β¬β¬ β½  L1-6 zonkγ@γ
β¬β¬ β½  cancel
β¬β¬ β½  Lcancel
β¬β¬ β½  invite
β¬β¬ β½  L1-6 invite
β¬β¬ β½  Lgn:γtextγ
β¬β¬ β½  bcgrup:γtextγ
β¬β¬ β½  grup set
β¬β¬ β½  ginfo
β¬β¬ β½  midγ@γ
β¬β¬ β½  ctγ@γ
β¬β¬ β½  tag
β¬β¬ β½  left:γtextγ
β¬β¬ β½  welcome:γtextγ
β¬β¬ β½  sider:γtextγ
β¬β¬ β½  add:γtextγ
β¬β¬ β½  check msg
β¬β¬ββββββββββββ
β¬β¬ β½  protectγon/offγ
β¬β¬ β½  prokickγon/offγ
β¬β¬ β½  proinviteγon/offγ
β¬β¬ β½  procancelγon/offγ
β¬β¬ β½  proqrγon/offγ
β¬β¬ β½  addγon/offγ
β¬β¬ β½  siderγon/offγ
β¬β¬ β½  leftγon/offγ
β¬β¬ β½  welcomeγon/offγ
β¬β¬ β½  add owner
β¬β¬ β½  Del owner
β¬β¬ β½  owner list
β¬β¬ β½  clear owner
β¬β¬ β½  add admin
β¬β¬ β½  Del admin
β¬β¬ β½  admin list
β¬β¬ β½  clear admin
β¬β¬ β½  add staff
β¬β¬ β½  Del staff
β¬β¬ β½  staff list
β¬β¬ β½  clear staff
β¬β¬ β½  ablacklist
β¬β¬ β½  dblacklist
β¬β¬ β½  banlist
β¬β¬ β½  Hapus
β¬β¬ β½  left grup
β¬β¬ β½  out all grup
β¬β¬ β½  runtime
β¬β¬ β½  respon
β¬β¬ β½  name
β¬β¬ β½  rechat
β¬β¬ β½  sp
β¬β¬ β½  all inv
β¬β¬ β½  Masuk
β¬β¬ β½  bye
β¬β¬βββββββββββββββββ¬
β¬        β¦ LeaBot-VersioN β§
β¬ββββββββββββββββββ¬
"""
helpMessage1 ="""
π₯βββββ¦ RATU JS β§ββββπ₯
β¬β¬βββββββββββββββββ¬
β¬β¬ β½  key owner
β¬β¬ β½  ourl
β¬β¬ β½  gurl
β¬β¬ β½  curl
β¬β¬ β½  cn:γnamaγ
β¬β¬ β½  L1-6 cn:γnamaγ
β¬β¬ β½  Zonkγ@γ
β¬β¬ β½  L1-6 zonkγ@γ
β¬β¬ β½  Lancel
β¬β¬ β½  Lcancel
β¬β¬ β½  Linvite
β¬β¬ β½  L1-6 invite
β¬β¬ β½  bcgrup:
β¬β¬ β½  grup set
β¬β¬ β½  ginfo
β¬β¬ β½  midγ@γ
β¬β¬ β½  ctγ@γ
β¬β¬ β½  Sepi
β¬β¬ β½  gn:γtextγ
β¬β¬ β½  left:γtextγ
β¬β¬ β½  welcome:γtextγ
β¬β¬ β½  sider:γtextγ
β¬β¬ β½  Ladd:γtextγ
β¬β¬ β½  check msg
β¬β¬ββββββββββββ
β¬β¬ β½  protectγon/offγ
β¬β¬ β½  prokickγon/offγ
β¬β¬ β½  proinviteγon/offγ
β¬β¬ β½  procancelγon/offγ
β¬β¬ β½  proqrγon/offγ
β¬β¬ β½  addγon/offγ
β¬β¬ β½  siderγon/offγ
β¬β¬ β½  leftγon/offγ
β¬β¬ β½  welcomeγon/offγ
β¬β¬ β½  add admin
β¬β¬ β½  Del admin
β¬β¬ β½  admin list
β¬β¬ β½  clear admin
β¬β¬ β½  add staff
β¬β¬ β½  Del staff
β¬β¬ β½  staff list
β¬β¬ β½  clear staff
β¬β¬ β½  ablacklist
β¬β¬ β½  dblacklist
β¬β¬ β½  banlist
β¬β¬ β½  Hapus
β¬β¬ β½  name
β¬β¬ β½  runtime
β¬β¬ β½  respon
β¬β¬ β½  rechat
β¬β¬ β½  sp
β¬β¬ β½  all inv
β¬β¬ β½  Masuk
β¬β¬ β½  bye
β¬β¬βββββββββββββββββ¬
β¬        β¦ LeaBot-VersioN β§
β¬ββββββββββββββββββ¬
"""
helpMessage2 ="""
π₯βββββ¦ RATU JS β§ββββπ₯
β¬β¬βββββββββββββββββ¬
β¬β¬ β½  key admin
β¬β¬ β½  ourl
β¬β¬ β½  gurl
β¬β¬ β½  curl
β¬β¬ β½  Zonkγ@γ
β¬β¬ β½  L1-6 zonkγ@γ
β¬β¬ β½  invite
β¬β¬ β½  L1-6 invite
β¬β¬ β½  Lgn:γtextγ
β¬β¬ β½  ginfo
β¬β¬ β½  midγ@γ
β¬β¬ β½  ctγ@γ
β¬β¬ β½  Sepi
β¬β¬ β½  siderγon/offγ
β¬β¬ β½  leftγon/offγ
β¬β¬ β½  welcomeγon/offγ
β¬β¬ββββββββββββ
β¬β¬ β½  add staff
β¬β¬ β½  Del staff
β¬β¬ β½  staff list
β¬β¬ β½  clear staff
β¬β¬ β½  ablacklist
β¬β¬ β½  dblacklist
β¬β¬ β½  banlist
β¬β¬ β½  Hapus
β¬β¬ β½  runtime
β¬β¬ β½  respon
β¬β¬ β½  rechat
β¬β¬ β½  name
β¬β¬ β½  sp
β¬β¬βββββββββββββββββ¬
β¬        β¦ LeaBot-VersioN β§
β¬ββββββββββββββββββ¬
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
        textx = " βΈ’{} user readingβΈ₯  ".format(str(len(mid)))
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
                    no = "\nββββΈ’ {} βΈ₯".format(str(cl.getGroup(to).name))
                except:
                    no = "\nβββ[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def summon(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "ββββββ[ Mentones ]βββββββ\nβ β 1. "
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
                textx += "β β  {}. ".format(str(no))
            else:
                textx += "βββββββββββββββββββ\nβββββββββββββββββββ\n  γ α΄α΄α΄α΄Κ α΄α΄α΄Κα΄Κ : {} γ\nβββββββββββββββββββ".format(str(len(mid)))
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
                        cl.sendMessage(op.param1,"ππππ ππ¨π¬π¬ π₯ππ π’ π¦ππ₯ππ¬ π§π ππ«π¨π¨π¦..\nππ²π π¦ππ¦πππ« " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))
                        cl.sendMessage(op.param1,"ππ?π€ππ§ π¨π°π§ππ« π²π ππ¨π¬π¬... πππ₯π’π€ π₯ππ π’ ππππ‘π‘π‘...\nn ππ²π..")
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))
                        ka.sendMessage(op.param1,"ππ?π€ππ§ π¨π°π§ππ« π²π ππ¨π¬π¬... πππ₯π’π€ π₯ππ π’ ππππ‘π‘π‘...\nn ππ²π..")
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))

            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))
                        kb.sendMessage(op.param1,"ππ?π€ππ§ π¨π°π§ππ« π²π ππ¨π¬π¬... πππ₯π’π€ π₯ππ π’ ππππ‘π‘π‘...\nn ππ²π..")
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))

            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))
                        kc.sendMessage(op.param1,"ππ?π€ππ§ π¨π°π§ππ« π²π ππ¨π¬π¬... πππ₯π’π€ π₯ππ π’ ππππ‘π‘π‘...\nn ππ²π..")
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))

            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))
                        kd.sendMessage(op.param1,"ππ?π€ππ§ π¨π°π§ππ« π²π ππ¨π¬π¬... πππ₯π’π€ π₯ππ π’ ππππ‘π‘π‘...\nn ππ²π..")
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))

            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))
                        ke.sendMessage(op.param1,"ππ?π€ππ§ π¨π°π§ππ« π²π ππ¨π¬π¬... πππ₯π’π€ π₯ππ π’ ππππ‘π‘π‘...\nn ππ²π..")
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))

            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in creator and op.param2 not in org["owner"]:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))
                        kf.sendMessage(op.param1,"ππ?π€ππ§ π¨π°π§ππ« π²π ππ¨π¬π¬... πππ₯π’π€ π₯ππ π’ ππππ‘π‘π‘...\nn ππ²π..")
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"π‘ππ₯π₯π¨ π¦ππ¦... " + str(ginfo.name))

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
                        cl.sendText(msg.to, "π°ππ¬ π¨π°π§ππ«")
                        wait["addowner"]=False
                    else:
                        org["owner"][msg.contentMetadata["mid"]] = True
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to, "π¨π°π§ππ« πππππ")
                        wait["addowner"]=False

            if msg.contentType == 13:
              if msg._from in creator:
                if wait["delowner"]==True:
                    if msg.contentMetadata["mid"] in org["owner"]:
                        del org["owner"][msg.contentMetadata["mid"]]
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        wait["delowner"]=False
                        cl.sendMessage(msg.to,"π¬ πππ₯ππ­ππ")
                    else:
                        cl.sendMessage(msg.to,"π π§π¨π­ ππ¨π?π§π")

#===[ Add admin βββ ]

            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"]:
                if wait["addadmin"]==True:
                    if msg.contentMetadata["mid"] in org["admin"]:
                        cl.sendMessage(msg.to, "π°ππ¬ πππ¦π’π§")
                        wait["addadmin"]=False
                    else:
                        org["admin"][msg.contentMetadata["mid"]] = True
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to, "πππ¦π’π§ πππππ")
                        wait["addadmin"]=False
                        
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"]:
                if wait["deladmin"]==True:
                    if msg.contentMetadata["mid"] in org["admin"]:
                        del org["admin"][msg.contentMetadata["mid"]]
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        wait["deladmin"]=False
                        cl.sendMessage(msg.to,"π¬ πππ₯ππ­ππ")
                    else:
                        cl.sendMessage(msg.to,"π π§π¨π­ ππ¨π?π§π")

#====[ Add staff βββ ]
                        
            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["addstaff"]==True:
                    if msg.contentMetadata["mid"] in org["staff"]:
                        cl.sendMessage(msg.to, "π°ππ¬ π¬π­πππ")
                        wait["addstaff"]=False
                    else:
                        org["staff"][msg.contentMetadata["mid"]] = True
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to, "π¬π­πππ πππππ")
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
                        cl.sendMessage(msg.to,"π¬π­πππ πππ₯ππ­ππ")
                        wait["delstaff"]=False
                    else:
                        cl.sendMessage(msg.to,"ππ­πππ π§π¨π­ ππ¨π?π§π")
                        wait["delstaff"]=False
                else:
                    pass
                    
#========[ BLACKLIST ]============#

            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["ablacklist"]==True:
                    if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        cl.sendMessage(to, "β πππ¬ ππ ππ¨π¬π¬")
                        wait["ablacklist"]=False
                    else:
                        wait2["blacklist"][msg.contentMetadata["mid"]] = True
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "β ππ₯πππ€π₯π’π¬π­ πππ―ππ")
                        wait["ablacklist"]=False

            if msg.contentType == 13:
              if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                if wait["dblacklist"]==True:
                    if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        del wait2["blacklist"][msg.contentMetadata["mid"]]
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "β ππ₯πππ€π₯π’π¬π­ πππ¦π¨π―ππ")
                        wait["dblacklist"]=False
                    else:
                        cl.sendMessage(to,"β π­ππ«π ππ­ π§π¨π­ ππ¨π?π§π")
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
                            cl.sendMessage(msg.to,"ππ¨π§π ππ§π―π’π­π : \nβ‘" + _name)
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
                            ka.sendMessage(msg.to,"ππ¨π§π ππ§π―π’π­π : \nβ‘" + _name)
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
                            kb.sendMessage(msg.to,"ππ¨π§π ππ§π―π’π­π : \nβ‘" + _name)
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
                            kc.sendMessage(msg.to,"ππ¨π§π ππ§π―π’π­π : \nβ‘" + _name)
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
                            kd.sendMessage(msg.to,"ππ¨π§π ππ§π―π’π­π : \nβ‘" + _name)
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
                            ke.sendMessage(msg.to,"ππ¨π§π ππ§π―π’π­π : \nβ‘" + _name)
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
                            kf.sendMessage(msg.to,"ππ¨π§π ππ§??π’π­π : \nβ‘" + _name)
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
                            cl.sendMessage(msg.to,"πͺπ« π§π²π ππ’ ππ§π? ππ?π₯π? π¨π¦")
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
                        cl.sendMessage(msg.to,"πͺπ« π°ππ¬ π¨π©ππ§")
                    else:
                        X.preventedJoinByTicket = False
                        cl.updateGroup(X)
                        cl.sendMessage(msg.to,"ππ π¨π©ππ§")

                elif msg.text in ["curl"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    X = cl.getGroup(msg.to)
                    if X.preventedJoinByTicket == True:
                        cl.sendMessage(msg.to,"πͺπ« π°ππ¬ π¨π©ππ§")
                    else:
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        cl.sendMessage(msg.to,"ππ«π₯ π’π§πππ­π’π―π")

                elif "bcgrup: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"]:
                    bc = msg.text.replace("bcgrup: ","")
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                            cl.sendMessage(i,bc+"\n\nβ€πππππ’π₯π₯ππ«β€")
                            cl.sendMessage(msg.to,"ππ?ππππ¬π¬ ππ ππ¨π¬π")

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
                            cl.sendMessage(msg.to,"πππ¬π­ππ«π­π’π§π ...")
                            restart_program()
                        except:
                            cl.sendMessage(msg.to,"ππ₯πππ¬π π°ππ’π­")
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
                      cl.sendMessage(msg.to, "πππ¦π’ π¬π’ππ© π¦ππ§ππ«π’π¦π π©ππ«π’π§π­ππ‘ ππ¨π¬π¬πͺπ?π‘...")
                      ka.sendMessage(msg.to, "πππ¦π’ π¬π’ππ© π¦ππ§ππ«π’π¦π π©ππ«π’π§π­ππ‘ ππ¨π¬π¬πͺπ?π‘...")
                      kb.sendMessage(msg.to, "πππ¦π’ π¬π’ππ© π¦ππ§ππ«π’π¦π π©ππ«π’π§π­ππ‘ ππ¨π¬π¬πͺπ?π‘...")
                      kc.sendMessage(msg.to, "πππ¦π’ π¬π’ππ© π¦ππ§ππ«π’π¦π π©ππ«π’π§π­ππ‘ ππ¨π¬π¬πͺπ?π‘...")
                      kd.sendMessage(msg.to, "πππ¦π’ π¬π’ππ© π¦ππ§ππ«π’π¦π π©ππ«π’π§π­ππ‘ ππ¨π¬π¬πͺπ?π‘...")
                      ke.sendMessage(msg.to, "πππ¦π’ π¬π’ππ© π¦ππ§ππ«π’π¦π π©ππ«π’π§π­ππ‘ ππ¨π¬π¬πͺπ?π‘...")
                      kf.sendMessage(msg.to, "πππ¦π’ π¬π’ππ© π¦ππ§ππ«π’π¦π π©ππ«π’π§π­ππ‘ ππ¨π¬π¬πͺπ?π‘...")

                elif msg.text in ["bot:restart"]:
                    if msg._from in creator:
                        cl.sendMessage(msg.to, "ππ¨π­ π‘ππ¬ ππππ§ π«ππ¬π­ππ«π­ππ")
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
                        cl.sendMessage(op.message.to, "βββββββββββββββ\nβ β π§π¨ π¨π§π π’π¬ π’π§π―π’π­π’π§π \nβββββββββββββββ")
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
                        random.choice(K2C).sendMessage(op.message.to, "βββββββββββββββ\nβ β π§π¨ π¨π§π π’π¬ π’π§π―π’π­π’π§π \nβββββββββββββββ")
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
                        cl.sendMessage(msg.to,"ππ’π π‘ ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ ππ§")
                        ka.sendMessage(msg.to,"ππ’π π‘ ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ ππ§")
                        kb.sendMessage(msg.to,"ππ’π π‘ ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ ππ§")
                        kc.sendMessage(msg.to,"ππ’π π‘ ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ ππ§")
                        kd.sendMessage(msg.to,"ππ’π π‘ ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ ππ§")
                        ke.sendMessage(msg.to,"ππ’π π‘ ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ ππ§")
                        kf.sendMessage(msg.to,"ππ’π π‘ ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ ππ§")

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
                    cl.sendMessage(msg.to,"ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ πππ")
                    ka.sendMessage(msg.to,"ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ πππ")
                    kb.sendMessage(msg.to,"ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ πππ")
                    kc.sendMessage(msg.to,"ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ πππ")
                    kd.sendMessage(msg.to,"ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ πππ")
                    ke.sendMessage(msg.to,"ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ πππ")
                    kf.sendMessage(msg.to,"ππ₯π₯ ππ«π¨π­πππ­π’π¨π§ πππ")
#---------------------------------------------------------
                elif msg.text in ["proinvite on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    pro["Protectinvite"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"ππ§π―π’π­π π¨π§ ππ«π¨π­πππ­π’π¨π§")

                elif msg.text in ["proinvite off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    del pro["Protectinvite"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"ππ§π―π’π­π π?π§π©π«π¨π­πππ­π’π¨π§")

#--------------------------------------------------------
                elif msg.text in ["proqr on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    pro["Protectgr"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"ππ« π’π§ π©π«π¨π­πππ­")

                elif msg.text in ["proqr off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    del pro["Protectgr"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"ππ« π?π§π©π«π¨π­πππ­")

                elif msg.text in ["procancel on"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    pro["Protectcancl"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to," ππ«π¨π­πππ­π’π¨π§ πππ§π??π₯ π¨π§")

                elif msg.text in ["procancel off"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    del pro["Protectcancl"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"ππ«π¨π­πππ­π’π¨π§ πππ§πππ₯ π¨ππ")

                elif msg.text in ["prokick on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    pro["Autokick"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"ππ?π­π¨ ππ’ππ€ π’π§ πππ­π’π―ππ­ππ")

                elif msg.text in ["prokick off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    pro["Autokick"][msg.to]=False
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"ππ?π­π¨ ππ’ππ€ π§π¨π­ πππ­π’π―π")

                elif msg.text in ["autojoin on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["autoJoin"]=True
                    cl.sendMessage(msg.to,"ππ?π­π¨ π£π¨π’π§ π’π§ πππ­π’π―ππ­ππ")

                elif msg.text in ["autojoin off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["autoJoin"]=False
                    cl.sendMessage(msg.to,"ππ?π­π¨ π£π¨π’π§ π§π¨π­ πππ­π’π―π")

                elif msg.text in ["autoleft on"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["autoLeave"]=True
                    cl.sendMessage(msg.to,"ππ?π­π¨ ππππ―π π’π§ πππ­π’π―ππ­ππ")

                elif msg.text in ["autoleft off"]:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["autoLeave"]=False
                    cl.sendMessage(msg.to,"ππ?π­π¨ ππππ―π π§π¨π­ πππ­π’π―π")

                elif msg.text in ["left on"]:
                    pro["bymsg"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "βββββββββββββ\nβ β π¦π¬π  π₯πππ­ π¨π§\nβββββββββββββ")

                elif msg.text in ["left off"]:
                    del pro["bymsg"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "βββββββββββββ\nβ β π¦π¬π  π₯πππ­ π¨ππ\nβββββββββββββ")

                elif msg.text in ["welcome on"]:
                    pro["wellcome"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "βββββββββββββ\nβ β π¬ππ¦ππ?π­ππ§ π¨π§\nβββββββββββββ")

                elif msg.text in ["welcome off"]:
                    del pro["wellcome"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "βββββββββββββ\nβ β π¬ππ¦ππ?π­ππ§ π¨ππ\nβββββββββββββ")

                elif msg.text in ["rechat"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    try:
                        cl.removeAllMessages(op.param2)
                        cl.sendMessage(to,"π©ππ¬ππ§ π­ππ₯ππ‘ ππ’π‘ππ©π?π¬ ππ¨π¬π¬πͺπ?π‘...")
                        ka.removeAllMessages(op.param2)
                        ka.sendMessage(to,"π©ππ¬ππ§ π­ππ₯ππ‘ ππ’π‘ππ©π?π¬ ππ¨π¬π¬πͺπ?π‘...")
                        kb.removeAllMessages(op.param2)
                        kb.sendMessage(to,"π©ππ¬ππ§ π­ππ₯ππ‘ ππ’π‘ππ©π?π¬ ππ¨π¬π¬πͺπ?π‘...")
                        kc.removeAllMessages(op.param2)
                        kc.sendMessage(to,"π©ππ¬ππ§ π­ππ₯ππ‘ ππ’π‘ππ©π?π¬ ππ¨π¬π¬πͺπ?π‘...")
                        kd.removeAllMessages(op.param2)
                        kd.sendMessage(to,"π©ππ¬ππ§ π­ππ₯ππ‘ ππ’π‘ππ©π?π¬ ππ¨π¬π¬πͺπ?π‘...")
                        ke.removeAllMessages(op.param2)
                        ke.sendMessage(to,"π©ππ¬ππ§ π­ππ₯ππ‘ ππ’π‘ππ©π?π¬ ππ¨π¬π¬πͺπ?π‘...")
                        kf.removeAllMessages(op.param2)
                        kf.sendMessage(to,"π©ππ¬ππ§ π­ππ₯ππ‘ ππ’π‘ππ©π?π¬ ππ¨π¬π¬πͺπ?π‘...")
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
                    cl.sendMessage(msg.to,"ππ¨π§π")

                elif msg.text in ["grup set"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    md = ""
                    if msg.to in pro["Protectgr"]: md+="β  β½ ππ«π¨π­πππ­ π π«π?π© : β\n"
                    else: md +="β  β½ ππ«π¨π­πππ­ π π«π?π© : β\n"
                    if msg.to in pro["Protectcancl"]: md+="β  β½ ππ«π¨π­πππ­ πππ§πππ₯ : β\n"
                    else: md+= "β  β½ ππ«π¨π­πππ­ πππ§πππ₯ : β\n"
                    if msg.to in pro["Protectinvite"]: md+="β  β½ ππ«π¨π­πππ­ π’π§π―π’π­π : β\n"
                    else: md+= "β  β½ ππ«π¨π­πππ­ π’π§π―π’π­π : β\n"
                    if msg.to in pro["Autokick"]: md+="β  β½ ππ?π­π¨ π€π’ππ€ : β\n"
                    else:md+="β  β½ ππ?π­π¨ π€π’ππ€ : β\n"
                    if msg.to in pro["wellcome"]: md+="β  β½ π°ππ₯π₯ππ¨π¦π π­ππ€π¬ : β\n"
                    else:md+="β  β½ π°ππ₯π₯ππ¨π¦π π­ππ€π¬ : β\n"
                    if msg.to in pro["bymsg"]: md+="β  β½ π₯πππ­ π­ππ€π¬ : β\n"
                    else:md+="β  β½ π₯πππ­ π­ππ€π¬ : β\n"
                    cl.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ ππ«π?π© π¬ππ­ π?π© β§\nβββββββββββββββ\n"+ md +"βββββββββββββββ")

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
                    if wait["midct"] == True: md+="β  β½ π¦π’πππ­ : β\n"
                    else:md+="β  β½ π¦π’πππ­ : β\n"
                    if wait["spamr"] == True: md+="β  β½ π¬π©ππ¦ ππ¨π§π­πππ­ : β\n"
                    else:md+="β  β½ π¬π©ππ¦ ππ¨π§π­πππ­ : β\n"
                    if wait["Invi"] == True: md+="β  β½ π’π§π―π’ : β\n"
                    else:md+="β  β½ π’π§π―π’ : β\n"
                    if wait["LikeOn"] == True: md+="β  β½ ππ’π€π : β\n"
                    else:md+="β  β½ ππ’π€π : β\n"
                    if wait["Timeline"] == True: md+="β  β½ πππ­ π©π¨π¬π­ : β\n"
                    else:md+="β  β½ πππ­ π©π¨π¬π­ : β\n"
                    cl.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ πππ₯π π¬π­ππ­π?π¬ β§\nβββββββββββββββ\n"+ md +"βββββββββββββββ")

                elif msg.text in ["add owner"]:
                    if msg._from in creator:
                        wait["addowner"]=True
                        cl.sendMessage(msg.to, "π¬ππ§π ππ¨π§π­πππ­")

                elif msg.text in ["del owner"]:
                    if msg._from in creator:
                        wait["delowner"]=True
                        cl.sendMessage(msg.to, "π¬ππ§π ππ¨π§π­πππ­")

                elif msg.text in ["clear owner"]:
                  if msg._from in creator:
                    org["owner"] = {}
                    with open('org.json', 'w') as fp:
                        json.dump(org, fp, sort_keys=True, indent=4)
                    cl.sendMessage(msg.to,"ππ?ππππ¬ ππ₯πππ«")

                elif msg.text in ["owner list"]:
                  if msg._from in creator:
                    if org["owner"] == {}:
                        cl.sendMessage(msg.to,"ππ¦π©π­π² ππ₯π’π¬π­")
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
                        jo = "\nβ  β½ ".join(str(i) for i in nban)
                        cl.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ ππ°π§ππ« ππ’π¬π­ β§\nβββββββββββββββ\nβ  β½ %s\nβββββββββββββββ\nβ β¦ Total: %s β§\n"%(jo,str(len(cban)))+"βββββββββββββββ")

                elif msg.text in ["add owner "]:
                    if msg._from in creator:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:    
                            if target in org["owner"]:
                                cl.sendMessage(msg.to,"π°ππ¬ π¨π°π§ππ«")
                                pass
                            else:
                                try:
                                    org["owner"][target] = True
                                    with open('org.json','w') as fp:
                                        json.dump(org, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(msg.to,"π¬π?ππππ¬ πππππ π¨π°π§ππ«")
                                except Exception as e:
                                    cl.sendMessage(msg.to,"ππ«π¨π«π«.....")

                elif msg.text in ["add admin"]:
                    if msg._from in creator or msg._from in org["owner"]:
                        wait["addadmin"]=True
                        cl.sendMessage(msg.to, "π¬ππ§π ππ¨π§π­πππ­")
                elif msg.text in ["Del admin"]:
                    if msg._from in creator or msg._from in org["owner"]:
                        wait["deladmin"]=True
                        cl.sendMessage(msg.to, "π¬ππ§π ππ¨π§π­πππ­")

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
                        jo = "\nβ  β½ ".join(str(i) for i in nban)
                        cl.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ Admin List β§\nβββββββββββββββ\nβ  β½ %s\nβββββββββββββββ\nβ β¦ Total: %s β§\n"%(jo,str(len(cban)))+"βββββββββββββββ")

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
                        cl.sendMessage(to,"βββββββββββββββ\nβ β empty list\nβββββββββββββββ")
                    else:
                        mc = "βββββββββββββββ\nβ β β² Friend List β³β\nβ ββββββββββββββ"
                        for mi_d in org["staff"]:
                            mc += "\nβ β "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\nβββββββββββββββ")

#=======[ ADD BLACKLIST ]=======#
                elif msg.text in ["cban"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    wait2['blacklist'] = {}
                    with open('wait2.json', 'w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"Β°done boss")
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
                        cl.sendMessage(to,"β empty list")
                    else:
                        mc = "βββββββββββββββ\nβ β β² BanList β³β\nβ ββββββββββββββ"
                        for mi_d in wait2["blacklist"]:
                            mc += "\nβ β "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\nβββββββββββββββ")

                elif msg.text in ["list member"]:   
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    kontak = cl.getGroup(msg.to)
                    group = kontak.members
                    msgs="βββββββββββββββ\nβ ββ² Member List β³β\nβ ββββββββββββββ"
                    for ids in group:
                        msgs+="\nβ β %s" % (ids.displayName)
                    msgs+="\nβ ββββββββββββββ\nβ ββ² Total Members : %i β³β\n" % len(group)+"βββββββββββββββ"
                    cl.sendMessage(to, msgs)

                elif msg.text in ["gift"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    cl.sendMessage(to, "ππ.For UΒ°Β°Β°Β°")
                    cl.sendMessage(to, None, contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
#=================================#
                elif "sider: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    wait["cctvteks"] = msg.text.replace("sider: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"βββββββββββββββ\nβ β succses\nβββββββββββββββ")  

                elif msg.text in ["check msg"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    cl.sendMessage(to,"msg add: \nββββββββββββββ\n" + wait["message"] + "\nββββββββββββββ")
                    cl.sendMessage(to,"msg sider: \nββββββββββββββ\n" + wait["cctvteks"] + "\nββββββββββββββ")
                    cl.sendMessage(to,"msg leave: \nββββββββββββββ\n" + wait["leftmsg"] + "\nββββββββββββββ")
                    cl.sendMessage(to,"msg welcome: \nββββββββββββββ\n" + wait["welmsg"] + "\nββββββββββββββ")
#===================#
                elif "left: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    wait["leftmsg"] = msg.text.replace("left: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"βββββββββββββββ\nβ β succses\nβββββββββββββββ")   

                elif "welcome: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    wait["welmsg"] = msg.text.replace("welcome: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"βββββββββββββββ\nβ β succses\nβββββββββββββββ")   
#=================#
                elif "add: " in msg.text:
                  if msg._from in creator or msg._from in org["owner"]:
                    wait["message"] = msg.text.replace("add: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"βββββββββββββββ\nβ β succses\nβββββββββββββββ")   

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
                               cl.sendMessage(msg.to, "Β°no siderβ’β’β’")
                       else:
                           cl.sendMessage(msg.to, "please create lurk on")

                elif msg.text in ["sider on"]:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                      try:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          cl.sendMessage(msg.to, "βββββββββββββββ\nβ β starting cek sider\nβββββββββββββββ\nβββββββββββββββ\nβ β date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nβ β hour "+ datetime.strftime(timeNow,'%H:%M:%S')+"\nβββββββββββββββ")
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
                           cl.sendMessage(msg.to, "βββββββββββββββ\nβ β sider off mode\nβββββββββββββββ")
                       else:
                           cl.sendMessage(msg.to, "done offΒ°")

                elif msg.text in ["grup"]:
                    if msg._from in creator:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = cl.getGroup(i).name
                            h += "β  β½ %s\n" % (gn)
                        cl.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ My grup β§\nβββββββββββββββ\n"+ h +"βββββββββββββββ")
                elif msg.text in ["L1grup"]:
                    if msg._from in creator:
                        gid = ka.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = ka.getGroup(i).name
                            h += "β  β½ %s\n" % (gn)
                        ka.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ My grup β§\nβββββββββββββββ\n"+ h +"βββββββββββββββ")

                elif msg.text in ["l2grup"]:
                    if msg._from in creator:
                        gid = kb.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kb.getGroup(i).name
                            h += "β  β½ %s\n" % (gn)
                        kb.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ My grup β§\nβββββββββββββββ\n"+ h +"βββββββββββββββ")
                elif msg.text in ["l3grup"]:
                    if msg._from in creator:
                        gid = kc.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kc.getGroup(i).name
                            h += "β  β½ %s\n" % (gn)
                        kc.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ My grup β§\nβββββββββββββββ\n"+ h +"βββββββββββββββ")

                elif msg.text in ["l4grup"]:
                    if msg._from in creator:
                        gid = kd.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kd.getGroup(i).name
                            h += "β  β½ %s\n" % (gn)
                        kd.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ My grup β§\nβββββββββββββββ\n"+ h +"βββββββββββββββ")
                elif msg.text in ["l5grup"]:
                    if msg._from in creator:
                        gid = ke.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = ke.getGroup(i).name
                            h += "β  β½ %s\n" % (gn)
                        ke.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ My grup β§\nβββββββββββββββ\n"+ h +"βββββββββββββββ")
                elif msg.text in ["l6grup"]:
                    if msg._from in creator:
                        gid = kf.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kf.getGroup(i).name
                            h += "β  β½ %s\n" % (gn)
                        kf.sendMessage(msg.to,"βββββββββββββββ\nβ β¦ My grup β§\nβββββββββββββββ\n"+ h +"βββββββββββββββ")

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

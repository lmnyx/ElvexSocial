import time
import os
from enum import Enum
from time import gmtime, strftime
from colorama import Fore, Back, init
import random
import sys
import math
import json
import sqlite3
import platform
import hmac
import hashlib
import base64
import string
import binascii
import re
import traceback
import threading
import elvex_module
import inspect
from socket import gethostname
import psutil
import prompt_toolkit
from time import gmtime, mktime
try:
    import readline
except ImportError:
    import pyreadline as readline
import npyscreen
try:
	import subprocess
except:
	subprocessUndefined = True
	# that's fine.
db_AdditionalsVer = 2
db_usersVer = 1
version = 4

oprint = print
oopen = open
PromoteFromWeb = True

def TempErrHook(exctype, val, tb):
	print('[{}] {} ({})'.format(exctype, val, tb))

sys.excepthook = TempErrHook # TEMP UNTIL MODULE FINISHED LOADING

def open(fn, t = "r"):
	global oopen
	Openned = False
	while not(Openned):
		try:
			fl = oopen(fn, t)
			Openned = True
		except IOError:
			Logger("Open of "+fn+" was failed. Trying again.", CT.ERROR)
			continue
	return fl



def Void():
	return
try:
	ohelp = help
except Exception:
	Void()

def clear():
	"""Clear the output."""
	if(platform.system() == "Windows"): os.system("cls")
	else: os.system("clear")

NotList = ["is_valid_command", "CompleterLoad","Void","Enum", "gmtime", "strftime", "init", "ohelp", "CT", "oprint", "round50", "create_self_signed_cert","completer","v", "dbgSwitchErrorDisplay", "dbgNoDebug"]
def help():
	"""List of all functions."""
	global NotList
	if not(isDebugger):
		return
	cmds = 0
	for name, val in elvex_module.__dict__.items():
		if callable(val) and name not in NotList:
			try:
				args = inspect.getfullargspec(val)[0]
			except Exception:
				continue
			args = ', '.join(args)
			if(name.startswith("nolist_")):
				continue
			if(name.startswith("dbg")):
				name = Fore.CYAN + name + Fore.RESET
			cmds += 1
			if(str(val.__doc__) == "None"):
				print(name + "(" + args + ") - No description.", CT.INFO)
			else:
				print(name + "(" + args + ") - " + val.__doc__, CT.INFO)
	if(cmds > 0):
		print("There is "+Fore.GREEN+str(cmds)+Fore.RESET + " functions in total.")
	else:
		print("There is "+Fore.RED+str(cmds)+Fore.RESET + " functions in total.")

StartTime = time.time()

isDebugger = False

true = True
false = False

def synchronized(func):
	
    func.__lock__ = threading.Lock()
		
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func

def round50(n):
    return round(n * 2, -2)

init(autoreset=true)

if not(os.path.isfile("current.log")):
	with open("current.log", "w") as w:
		w.write("")

with open("current.log", "w") as w:
	w.write("")

try:
	os.mkdir("log")
except FileExistsError:
	idc = "i dont care"
	del idc

if not(os.path.isfile("log/unix"+str(StartTime)+".log")):
	with open("log/unix"+str(StartTime)+".log", "w") as w:
		w.write("")

with open("log/unix"+str(StartTime)+".log", "w") as w:
	w.write("")

class CT(Enum):
	WARN = 1
	INFO = 2
	ERROR = 3
	NONE = 4

def EncodedString(stri):
	"""Encodes string."""
	return str.encode(stri)

def eprint(t):
	"""Prints with newline."""
	sys.stdout.write(t+'\n')



def Logger(stri,type = CT.NONE):
	"""Add message to log."""
	global StartTime
	if(type == CT.NONE):
		with open("current.log", "a") as w:
			w.write("[NONE]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		with open("log/unix"+str(StartTime)+".log", "a") as w:
			w.write("[NONE]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		return
	if(type == CT.WARN):
		with open("current.log", "a") as w:
			w.write("[WARN]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		with open("log/unix"+str(StartTime)+".log", "a") as w:
			w.write("[WARN]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		return
	if(type == CT.INFO):
		with open("current.log", "a") as w:
			w.write("[INFO]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		with open("log/unix"+str(StartTime)+".log", "a") as w:
			w.write("[INFO]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		return
	if(type == CT.ERROR):
		with open("current.log", "a") as w:
			w.write("[ERROR]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		with open("log/unix"+str(StartTime)+".log", "a") as w:
			w.write("[ERROR]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		return

# "unix"+str(StartTime)+".log"

def is_json(myjson):
  """Check if string is json."""
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

def LogPrint(stri,type = CT.NONE):
	"""Print and add to log."""
	global StartTime
	stri = str(stri)
	if(type == CT.NONE):
		eprint("[NONE]" + Back.WHITE+Fore.BLACK + "["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]"+Back.RESET+Fore.RESET+" "+stri)
		with open("current.log", "a") as w:
			w.write("[NONE]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		with open("log/unix"+str(StartTime)+".log", "a") as w:
			w.write("[NONE]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		return
	if(type == CT.WARN):
		eprint(Fore.YELLOW+"[WARN]"+Back.WHITE+Fore.BLACK+"["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]"+Back.RESET+Fore.RESET+" "+stri)
		with open("current.log", "a") as w:
			w.write("[WARN]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		with open("log/unix"+str(StartTime)+".log", "a") as w:
			w.write("[WARN]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		return
	if(type == CT.INFO):
		eprint(Fore.CYAN+"[INFO]"+Back.WHITE+Fore.BLACK+"["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]"+Back.RESET+Fore.RESET+" "+stri)
		with open("current.log", "a") as w:
			w.write("[INFO]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		with open("log/unix"+str(StartTime)+".log", "a") as w:
			w.write("[INFO]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		return
	if(type == CT.ERROR):
		eprint(Fore.RED+"[ERROR]"+Back.WHITE+Fore.BLACK+"["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]"+Back.RESET+Fore.RESET+" "+stri)
		with open("current.log", "a") as w:
			w.write("[ERROR]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		with open("log/unix"+str(StartTime)+".log", "a") as w:
			w.write("[ERROR]["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] "+stri+"\n")
		return

class print():
	"""Print a message."""
	def __init__(self,msg,typeo = CT.NONE):
		LogPrint(msg,typeo)

def IsUserExists(login):
	"""Is user exists in Elvex DB?"""
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	r = c.execute("SELECT * FROM users WHERE lower(username) = '{}'".format(login.lower()))
	if(r.fetchone()):
		return True
	else:
		return False

def EStr(stre):
	"""Encode string to password."""
	a = hmac.new(b'_EaLEoELXoELWoXLOWQlWA_1+-2#)LC<E!!!(!0CC@@@@A', stre.encode(), hashlib.sha256)
	return str(a.hexdigest())

def AddUser(login, pswd, avatar = 0, electricity = 0, ppcount = 0.0, inventory = "[]", customization = '{"droidColor": "blue", "lampColor": "blue","hat": "none", "body": "none", "hands": "none", "legs": "none"}', bio = "Not specified.", stats = "{}", banned = False, regip = "0.0.0.0", accessible = True, ban_reason = -1, badges = "[]"):
	"""Create user in Elvex DB."""
	if(IsUserExists(login)):
		print("Creation user with username "+login+" failed. User already exists.", CT.ERROR)
		return "USER_EXISTS"
	if(len(login) < 4):
		return "USER_LEN"
	if(len(pswd) < 6):
		return "PSWD_LEN"
	if(login.isspace() or login == ""):
		return "USER_SPACE"
	pswd = EStr(pswd)
	if(re.search('[^a-zA-Z0-9_]', login) is not None):
		return "USER_CHARACTERS"
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	r = c.execute("SELECT * FROM bannednames WHERE lower(name) = '{}'".format(login.lower()))
	if(r.fetchone()):
		return "NAME_BANNED"
	#        TEXT, TEXT, INT, FLOAT, TEXT, TEXT, TEXT, TEXT, BOOL, TEXT
	c.execute("INSERT INTO users VALUES ('{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}', {}, '{}', {}, {}, '{}')".format(login, pswd, str(avatar), str(electricity), str(ppcount),inventory, customization,bio, stats, int(banned), regip, int(accessible), str(ban_reason), badges))
	conn.commit()
	conn.close()
	return "OK"


def RemoveUser(login):
	"""Remove user from Elvex DB."""
	if not (IsUserExists(login)):
		print("Removal failed. User doesn't exists. ("+login+")", CT.ERROR)
		return "USER_GONE"
	if(login.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("UPDATE users SET accessible = false WHERE lower(username) = '{}'".format(login.lower()))
	conn.commit()
	conn.close()
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("INSERT INTO bannednames VALUES ('{}')".format(login.lower()))
	conn.commit()
	conn.close()
	return "OK"

def RestoreUser(login):
	"""Restores user profile."""
	if not (IsUserExists(login)):
		print("Restoring failed. User doesn't exists. ("+login+")", CT.ERROR)
		return "USER_GONE"
	if(login.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("UPDATE users SET accessible = true WHERE lower(username) = '{}'".format(login.lower()))
	conn.commit()
	conn.close()
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("DELETE FROM bannednames WHERE name = '{}'".format(login.lower()))
	conn.commit()
	conn.close()
	return "OK"
def IsAccessibleUser(username):
	"""Is user profile accessible?"""
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	r = c.execute("SELECT accessible FROM users WHERE lower(username) = '{}'".format(username.lower()))
	r = r.fetchone()
	return bool(r[0])

def ListUsers():
	"""List all users."""
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	a = c.execute("SELECT * FROM users")
	for b in a:
		print("- "+b[0])
	conn.close()

def BanUser(login,reason = -1):
	"""Ban player from Elvex."""
	if not (IsUserExists(login)):
		print("Ban failed. User doesn't exists. ("+login+")", CT.ERROR)
		return "USER_GONE"
	if(login.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("UPDATE users SET banned = true WHERE lower(username) = '{}'".format(login.lower()))
	c.execute("UPDATE users SET ban_reason = {} WHERE lower(username) = '{}'".format(reason,login.lower()))
	conn.commit()
	conn.close()
	return "OK"

def UnbanUser(login):
	"""Pardon a player."""
	if not (IsUserExists(login)):
		print("Ban failed. User doesn't exists. ("+login+")", CT.ERROR)
		return "USER_GONE"
	if(login.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("UPDATE users SET banned = false WHERE lower(username) = '{}'".format(login.lower()))
	conn.commit()
	conn.close()
	return "OK"

flushing = False
flushingTried = 0

def FlushUsers():
	"""(WARNING) Delete all users."""
	global flushing
	global flushingTried
	if(flushing == False):
		print("To flush all users use FlushUsers() again.",CT.WARN)
		flushing = True
		flushingTried = time.time()
		return
	if(flushing == True and flushingTried+30 < time.time()):
		print("To flush all users use FlushUsers() again.",CT.WARN)
		flushing = True
		flushingTried = time.time()
		return
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute("DELETE FROM users")
	c.execute("DELETE FROM bannednames")
	c.execute('''INSERT INTO users VALUES ('act8', '', 0, 1000000, 0, '[]', '\{\}', '', '\{\}', false, '', true, -1, '["badge_bot"]')''')
	conn.commit()
	conn.close()
	print("Users were flushed.", CT.INFO)
	flushing = False

def IsUserBanned(username):
	"""Check if user is banned or no."""
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	a = c.execute("SELECT banned FROM users WHERE lower(username) = '{}'".format(username.lower()))
	a = bool(a.fetchone()[0])
	conn.close()
	return a

def GetBanReason(username):
	"""Get reason of ban for user."""
	if not IsUserExists(username):
		return "USER_GONE"
	if not IsUserBanned(username):
		return "USER_LAW"
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	a = c.execute("SELECT ban_reason FROM users WHERE lower(username) = '{}'".format(username.lower()))
	a = a.fetchone()[0]
	conn.close()
	return a

def GetUser(username, safe = True):
	"""Get user by name."""
	global isDebugger
	username = username.lower()
	if not (IsUserExists(username)):
		print("Tried to get user, but user with that name doesn't exists. ("+username+")", CT.ERROR)
		return "USER_GONE"
	elif IsUserBanned(username) and not isDebugger:
		return "USER_BANNED"
	elif not IsAccessibleUser(username) and not isDebugger:
		return "USER_GONE"
	if(username.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	if(safe):
		a = c.execute("SELECT username, electricity,avatar, ppcount, inventory, customization, bio, stats, banned, badges FROM users WHERE lower(username) = '{}'".format(username.lower()))
		a = a.fetchone()
	else:
		a = c.execute("SELECT username, passhash, electricity,avatar,ppcount, inventory, customization, bio, stats, banned, regip, badges FROM users WHERE lower(username) = '{}'".format(username.lower()))
		a = a.fetchone()
	return a

def AddRedeemKey(key, type_reedem, code):
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	c.execute('INSERT INTO item_keys VALUES ("'+str(key)+'", "'+str(type_reedem)+'", "'+str(code)+'")')
	conn.commit()
	conn.close()
	return True

def isRedeemKey(key):
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	r = c.execute('SELECT * FROM item_keys WHERE key = "'+key+'"')
	if(r.fetchone()):
		conn.close()
		return True
	else:
		conn.close()
		return False

def RemoveReedemKey(key):
	if not isRedeemKey(key): return False
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	r = c.execute('DELETE FROM item_keys WHERE key = "'+key+'"')
	conn.commit()
	conn.close()
	return True

def UseRedeemKey(user,key):
	if not isRedeemKey(key): return False
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	r = c.execute('SELECT * FROM item_keys WHERE key = "'+key+'"')
	r = r.fetchone()
	if(r[1] == "item"):
		AddInvUser(user, r[2])
	elif(r[1] == "badge"):
		triedOK = GiveUserBadge(user, r[2])
		if(type(triedOK) == str):
			return False, triedOK
	else:
		RemoveReedemKey(key)
		return False, "WRONG_KEYTYPE"
	RemoveReedemKey(key)
	return True, r[1], r[2]

def rndstr(stringLength=4):
	letters = string.ascii_uppercase + string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))
def rndostr(stringLength=4):
	letters = string.ascii_uppercase
	return ''.join(random.choice(letters) for i in range(stringLength))

def GenerateRedeemKey(typer, code):
	key = rndstr()+"-"+rndstr(3)+"-"+rndstr()+"-"+rndostr()
	AddRedeemKey(key, typer, code)
	return key

# print(GetUserBalance("test"))

def GetUserBalance(username):
	"""Get user's balance."""
	s = GetUser(username)
	if(type(s) == str):
		return s
	return int(s[1])

def AddInvUser(username,item_code):
	"""Add item to player's inventory."""
	if not (IsUserExists(username)):
		print("Tried to add item to user's inventory, but user with that name doesn't exists. ("+username+")", CT.ERROR)
		return "USER_GONE"
	if(username.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	a = c.execute("SELECT inventory FROM users WHERE lower(username) = '{}'".format(username.lower()))
	a = json.loads(a.fetchone()[0])
	a.append(item_code)
	a = json.dumps(a)
	c.execute("UPDATE users SET inventory = '{}' WHERE lower(username) = '{}'".format(a,username))
	conn.commit()
	conn.close()
	return "OK"

def RemInvUser(username,index):
	"""Take item from player's inventory."""
	if not (IsUserExists(username)):
		print("Tried to take item from user's inventory, but user with that name doesn't exists. ("+username+")", CT.ERROR)
		return "USER_GONE"
	if(username.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	a = c.execute("SELECT inventory FROM users WHERE lower(username) = '{}'".format(username.lower()))
	a = json.loads(a.fetchone()[0])
	del a[index]
	a = json.dumps(a)
	c.execute("UPDATE users SET inventory = '{}' WHERE lower(username) = '{}'".format(a,username))
	conn.commit()
	conn.close()
	return "OK"

def SetCustomizationUser(username, n, h):
	"""Set item to customization slot of player."""
	if not (IsUserExists(username)):
		print("Tried to change user's customization, but user with that name doesn't exists. ("+username+")", CT.ERROR)
		return "USER_GONE"
	if(username.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	a = c.execute("SELECT customization FROM users WHERE lower(username) = '{}'".format(username.lower()))
	a = json.loads(a.fetchone()[0])
	a[n] = h
	a = json.dumps(a)
	c.execute("UPDATE users SET customization = '{}' WHERE lower(username) = '{}'".format(a,username))
	conn.commit()
	conn.close()
	return "OK"

def EditUserPassword(username, currentPass, newPass):
	"""Edit password of user (needs old)."""
	global isDebugger
	if not (IsUserExists(username)):
		print("Tried to change user's password, but user with that name doesn't exists. ("+username+")", CT.ERROR)
		return "USER_GONE"
	elif IsUserBanned(username) and not isDebugger:
		return "USER_BANNED"
	if(username.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	a = c.execute("SELECT passhash FROM users WHERE lower(username) = '{}'".format(username.lower()))
	a = str(a.fetchone()[0])
	if not(EStr(currentPass) == a):
		return "USER_WRONG_HASH"
	newPass = EStr(newPass)
	c.execute("UPDATE users SET passhash = '{}' WHERE lower(username) = '{}'".format(newPass, username))
	conn.commit()
	conn.close()
	return "OK"

def UnsafeEditUserPassword(username, newPass):
	"""Edit password of user."""
	if not (IsUserExists(username)):
		print("Tried to change user's password, but user with that name doesn't exists. ("+username+")", CT.ERROR)
		return "USER_GONE"
	if(username.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	a = c.execute("SELECT passhash FROM users WHERE lower(username) = '{}'".format(username.lower()))
	a = str(a.fetchone()[0])
	newPass = EStr(newPass)
	c.execute("UPDATE users SET passhash = '{}' WHERE lower(username) = '{}'".format(newPass, username))
	conn.commit()
	conn.close()
	return "OK"

def ChangeUserStat(username,stat,to):
	"""Change user's statistic."""
	if not (IsUserExists(username)):
		print("Tried to change user's stat, but user with that name doesn't exists. ("+username+")", CT.ERROR)
		return "USER_GONE"
	if(username.isspace()):
		return "USER_SPACE"
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	a = c.execute("SELECT stats FROM users WHERE lower(username) = '{}'".format(username.lower()))
	a = json.loads(a.fetchone()[0])
	a[stat] = to
	a = json.dumps(a)
	c.execute("UPDATE users SET stats = '{}' WHERE lower(username) = '{}'".format(a,username))
	conn.commit()
	conn.close()
	return "OK"

def EditUser(username, what, how):
	"""Edit user account."""
	global isDebugger
	if not (IsUserExists(username)):
		print("Tried to edit user, but user with that name doesn't exists. ("+username+")", CT.ERROR)
		return "USER_GONE"
	elif IsUserBanned(username) and not isDebugger:
		return "USER_BANNED"
	if(username.isspace()):
		return "USER_SPACE"
	stringlets = ["username", "bio"]
	warners = ["username"]
	if(what == "inventory"):
		print("To change inventory use: AddInvUser() or RemInvUser()")
		return "BAD_REQUEST"
	if(what == "customization"):
		print("To change customization use: SetCustomizationUser()")
		return "BAD_REQUEST"
	if(what == "passhash"):
		print("To change user's password use: EditUserPassword()")
		return "BAD_REQUEST"
	if(what == "stats"):
		print("To change stats use: ChangeUserStat()")
		return "BAD_REQUEST"
	if(what == "banned"):
		print("To change banned state use: BanUser() or UnbanUser()")
		return "BAD_REQUEST"
	if(what == "regip"):
		print("Regip cannot be changed.")
		return "BAD_REQUEST"
	
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	if(what in stringlets):
		c.execute("UPDATE users SET {} = '{}' WHERE lower(username) = '{}'".format(what,how,username))
	else:
		c.execute("UPDATE users SET {} = {} WHERE lower(username) = '{}'".format(what,how,username))
	if(what in warners):
		print(username+" just changed "+what+" to "+how,CT.WARN)
	conn.commit()
	conn.close()
	return "OK"

def CreateCrate(item_code, loot_table):
	"""Creates a new crate."""
	conn = sqlite3.connect('additional.db')
	c = conn.cursor()
	if not (is_json(loot_table)):
		return "LOOTTABLE_NOT_JSON"
	c.execute("INSERT INTO crates VALUES ('{}', '{}')".format(item_code,loot_table))
	conn.commit()
	conn.close()
	return "OK"

def isCrate(item_code):
	"""Checks if item is a crate or no."""
	conn = sqlite3.connect('additional.db')
	c = conn.cursor()
	a = c.execute("SELECT * FROM crates WHERE item_code = '{}'".format(item_code))

	if(a.fetchone()):
		conn.commit()
		conn.close()
		return True
	else:
		conn.commit()
		conn.close()
		return False


def About():
	"""Get information about ELVEX SOCIAL"""
	global isDebugger
	global version
	if not isDebugger:
		return "FAILED"
	print('Elvex SOCIAL v'+str(version))

def GetRandomPoolItem():
	"""Select random item out of shop pool."""
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	a = c.execute("SELECT * FROM shop_pool").fetchall()
	a = a
	conn.close()
	return random.choice(a)

def ForceUpdateStore():
	"""Force shop to update its containment."""
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	c.execute("DELETE FROM shop_current")
	item = GetRandomPoolItem()
	price = round50(random.randint(item[1], item[2]))
	c.execute("INSERT INTO shop_current VALUES ('{}', {})".format(item[0],str(price)))
	item = GetRandomPoolItem()
	price = round50(random.randint(item[1], item[2]))
	c.execute("INSERT INTO shop_current VALUES ('{}', {})".format(item[0],str(price)))
	item = GetRandomPoolItem()
	price = round50(random.randint(item[1], item[2]))
	c.execute("INSERT INTO shop_current VALUES ('{}', {})".format(item[0],str(price)))
	a = c.execute("SELECT * FROM time_storage WHERE sett = 'store_update';").fetchone()[1]
	c.execute("UPDATE time_storage SET unix = {} WHERE sett = 'store_update'".format(str(int(time.time()))))
	conn.commit()
	conn.close()
	return "SHOP_UPDATED"

def LogStoreItems():
	"""Log current store items."""
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	a = c.execute("SELECT * FROM shop_current").fetchall()
	for t in a:
		print(t[0] + " -- " + str(t[1]) +" electricity")
def GetStoreItems():
	"""Get current store items."""
	UpdateStore()
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	a = c.execute("SELECT * FROM shop_current").fetchall()
	return a
def UpdateStore():
	"""Update store containment."""
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	a = c.execute("SELECT * FROM time_storage WHERE sett = 'store_update';").fetchone()[1]
	if(a+3600 > int(time.time())):
		conn.close()
		return "TIMER_CONTINUES"
	else:
		c.execute("DELETE FROM shop_current")
		item = GetRandomPoolItem()
		price = round50(random.randint(item[1], item[2]))
		c.execute("INSERT INTO shop_current VALUES ('{}', {})".format(item[0],str(price)))
		item = GetRandomPoolItem()
		price = round50(random.randint(item[1], item[2]))
		c.execute("INSERT INTO shop_current VALUES ('{}', {})".format(item[0],str(price)))
		item = GetRandomPoolItem()
		price = round50(random.randint(item[1], item[2]))
		c.execute("INSERT INTO shop_current VALUES ('{}', {})".format(item[0],str(price)))
		c.execute("UPDATE time_storage SET unix = {} WHERE sett = 'store_update'".format(str(int(time.time()))))
		conn.commit()
		conn.close()
		return "SHOP_UPDATED"


def GetStoreTimer():
	"""Get amount of seconds before store updates."""
	UpdateStore()
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	a = c.execute("SELECT * FROM time_storage WHERE sett = 'store_update';").fetchone()[1]
	conn.close()
	return 3600-(int(time.time())-a)

def AddItemPool(item_code, min_price, max_price):
	"""Adds item to store pool"""
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	c.execute("INSERT INTO shop_pool VALUES ('{}', {}, {})".format(item_code, str(min_price), str(max_price)))
	conn.commit()
	conn.close()
	return "OK"

def GetStoreItem(index):
	"""Get store item by index."""
	items = GetStoreItems()
	if(index >= len(items)):
		return "NO_SUCH_INDEX"
	return items[index]

def ChanceTry(chance):
	"""Try the percentage chance."""
	return random.randrange(0,100) < chance

def GetCrateItem(crate_code):
	"""Get random item of crate."""
	conn = sqlite3.connect("additional.db")
	c = conn.cursor()
	cr = c.execute("SELECT items_in FROM crates WHERE item_code = '{}'".format(crate_code))
	cr = cr.fetchone()[0]
	cr = json.loads(cr)
	cr = sorted(cr.items(), key=lambda x: x[1])
	ItemCode_Result = ""
	while ItemCode_Result == "":
		for i in cr:
			a = ChanceTry(i[1])
			if(a):
				ItemCode_Result = i[0]
	conn.close()
	return ItemCode_Result

def haveUserBadge(user, badge):
	if not IsUserExists(user): return "USER_GONE"
	try:
		uinv = json.loads(GetUser(user)[9])
	except Exception:
		return False
	if(badge in uinv): return True
	else: return False

def GiveUserBadge(user, badge):
	if(haveUserBadge(user, badge)): return "BADGE_ALREADY"
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	cr = c.execute("SELECT badges FROM users WHERE lower(username) = '{}'".format(user)).fetchone()[0]
	cr = json.loads(cr)
	cr.append(badge)
	cr = json.dumps(cr)
	cr = c.execute("UPDATE users SET badges=\'{}\' WHERE lower(username) = '{}'".format(cr,user))
	conn.commit()
	conn.close()
	return True
BannedMethods = []
class VariableHandler(object):
	def __init__(self):
		self.Variables = {}
		self.DefaultsSet()
	def _set(self, varname, varcontent):
		self.Variables[varname] = varcontent
	def get(self, varname):
		if(varname in self.Variables):
			return self.Variables[varname]
		return False
	def DefaultsSet(self):
		self._set("TechWorkID", -1)
		self._set("MessageDelay", 0)

if(__name__ == "elvex_module"):
	vh = VariableHandler()

class CommandHandler(object):
	def __init__(self):
		self.currentCmd = ""
		# "": {"run": lambda: self.callFunc(""), "desc": "", "singleArg": False}
		self.Commands = {
			"help": {"run": lambda: self.callFunc("help"), "desc": "List of all commands.", "singleArg": False},
			"stop": {"run": lambda: self.callFunc("stop"), "desc": "Stop the server.", "singleArg": False},
			"togglemethod": {"run": lambda m: self.callFunc("togglemethod", m), "desc": "Toggles API method.", "singleArg": True},
			"yee": {"run": lambda: self.callFunc("yee"), "desc": "yee haw", "singleArg": False, "unlisted": True},
			"vhlist": {"run": lambda: self.callFunc("vhlist"), "desc": "list all variables of variablehandler", "singleArg": False, "unlisted": True},
			"fakedelay": {"run": lambda i: self.callFunc("fakedelay", i), "desc": "Adds fake delay before answering.", "singleArg": False},
			"maintenance": {"run": lambda i: self.callFunc("maintenance", i), "desc": "Set maintenance mode to specific.", "singleArg": False}
		}
		return
	def callFunc(self, cmd, *args):
		global vh
		if(cmd == "help"):
			print("Currently there is "+Fore.CYAN+str(len(self.Commands))+Fore.RESET+" total commands.")
			for cmd in self.Commands:
				if not ("unlisted" in self.Commands[cmd] and self.Commands[cmd]['unlisted']):
					print(Fore.CYAN+cmd+Fore.RESET+" - "+self.Commands[cmd]['desc'])
		elif(cmd == "stop"):
			print("Server is shutting down...", CT.INFO)
			os._exit(1)
		elif(cmd == "maintenance"):
			mid = int(args[0])
			if(mid < -1 or mid > 2):
				print("Wrong maintenance id.", CT.WARN)
				return
			vh._set("TechWorkID", mid)
			ReasonNames = ["Disabled", "Maintenance", "Update", "Not Listed"]
			CurrentReason = ReasonNames[mid+1]
			print("Switched current maintenance state to "+Fore.CYAN+CurrentReason+Fore.RESET+".", CT.INFO)
		elif(cmd == "fakedelay"):
			try:
				int(args[0])
			except Exception as e:
				print("Argument must be integer-type.", CT.ERROR)
				return
			
			vh._set("MessageDelay", int(args[0]))
			print("Set fake delay to "+Fore.CYAN+str(vh.get("MessageDelay"))+Fore.RESET+" seconds.")
		elif(cmd == "togglemethod"):
			global BannedMethods
			if(args[0] in BannedMethods):
				BannedMethods.remove(args[0])
				print("You enabled "+Fore.CYAN+args[0]+Fore.RESET+" method!", CT.INFO)
			else:
				BannedMethods.append(args[0])
				print("You disabled "+Fore.CYAN+args[0]+Fore.RESET+" method!", CT.INFO)
		elif(cmd == "yee"):
			print("haw")
		elif(cmd == "vhlist"):
			for v in vh.Variables:
				print(str(v)+" = "+str(vh.Variables[v]))
		return
	def Run(self, fullcmd):
		args = fullcmd.split(' ')
		args.pop(0)
		singlearg = ' '.join(args)
		cmd = fullcmd.split(' ', 1)[0]
		args = filter(None, args)
		self.currentCmd = cmd
		if(cmd in self.Commands):
			try:
				if(self.Commands[cmd]['singleArg']):
					self.Commands[cmd]['run'](singlearg)
				else:
					self.Commands[cmd]['run'](*args)
			except Exception as e:
				print(str(e), CT.ERROR)
		else:
			print("No command named "+Fore.RED+cmd+Fore.RESET+" found. Use `help` to list all commands.")

if(__name__ == "elvex_module"):
	cmdhand = CommandHandler()

# -- Debugger-only tools

def fprint(msg):
	print(fstr(msg))

def fstr(msg):
	Regex = r'[{]\w+[}]'
	retMsg = msg
	vars = re.findall(Regex, msg)
	for var in vars:
		varR = var[1:]
		varR = varR[:-1]
		if(varR in locals()):
			varR = str(locals()[varR])
		elif(varR in globals()):
			varR = str(globals()[varR])
		else:
			varR = "(Null)"
		retMsg = retMsg.replace(str(var), varR)
	return (retMsg)

class ESP(object):
	def __init__(self):
		self.inited = True
	def print(self, msg, mtype = CT.NONE):
		print(Fore.YELLOW+"[ESP] "+Fore.RESET+msg, mtype)
	class ErrorClassification(Enum):
		Unknown = -1,
		Unassigned = 0,
		Safe = 1,
		Unsafe = 2,
		Euclid = 3,
		Keter = 4,
		Thaumiel = 5,
		Neutralized = 6,
		Apocalypse = 7
	def GetClassClassification(self, classname):
		ClassifiedErrors = {
			"BaseException": [self.ErrorClassification.Safe, Fore.GREEN],
			"Exception": [self.ErrorClassification.Unknown, Fore.RED],
			"ArithmeticError": [self.ErrorClassification.Unsafe, Fore.YELLOW],
			"BufferError": [self.ErrorClassification.Euclid, Fore.RED],
			"LookupError": [self.ErrorClassification.Euclid, Fore.RED],
			"AssertionError": [self.ErrorClassification.Unsafe, Fore.YELLOW],
			"AttributeError": [self.ErrorClassification.Unsafe, Fore.YELLOW],
			"EOFError": [self.ErrorClassification.Thaumiel, Fore.CYAN],
			"FloatingPointError": [self.ErrorClassification.Neutralized,Fore.RESET],
			"ImportError": [self.ErrorClassification.Apocalypse,Fore.MAGENTA],
			"ModuleNotFound": [self.ErrorClassification.Apocalypse,Fore.MAGENTA],
			"IndexError": [self.ErrorClassification.Euclid, Fore.RED],
			"KeyError": [self.ErrorClassification.Euclid, Fore.RED],
			"MemoryError": [self.ErrorClassification.Apocalypse,Fore.MAGENTA],
			"NameError": [self.ErrorClassification.Euclid, Fore.RED],
			"NotImplementedError": [self.ErrorClassification.Euclid, Fore.RED],
			"OSError": [self.ErrorClassification.Keter,Fore.RED],
			"OverflowError": [self.ErrorClassification.Thaumiel,Fore.CYAN],
			"RecursionError": [self.ErrorClassification.Keter,Fore.RED],
			"ReferenceError": [self.ErrorClassification.Keter,Fore.RED],
			"RuntimeError": [self.ErrorClassification.Keter,Fore.RED],
			"StopInteration": [self.ErrorClassification.Unsafe, Fore.YELLOW],
			"StopAsyncIteration": [self.ErrorClassification.Unsafe, Fore.YELLOW],
			"SyntaxError": [self.ErrorClassification.Keter,Fore.RED],
			"IndentationError": [self.ErrorClassification.Unknown,Fore.RESET],
			"TabError": [self.ErrorClassification.Apocalypse,Fore.MAGENTA],
			"SystemError": [self.ErrorClassification.Keter,Fore.RED],
			"SystemExit": [self.ErrorClassification.Unknown,Fore.RESET],
			"TypeError": [self.ErrorClassification.Euclid, Fore.RED],
			"UnbondLocalError": [self.ErrorClassification.Keter,Fore.RED],
			"UnicodeError": [self.ErrorClassification.Keter,Fore.RED],
			"ValueError": [self.ErrorClassification.Thaumiel, Fore.CYAN],
			"ZeroDivisionError": [self.ErrorClassification.Apocalypse,Fore.MAGENTA],
			"EnvironmentError": [self.ErrorClassification.Thaumiel, Fore.CYAN],
			"IOError": [self.ErrorClassification.Thaumiel, Fore.CYAN],
			"WindowsError": [self.ErrorClassification.Thaumiel, Fore.CYAN]
		}
		if not classname in ClassifiedErrors:
			return [self.ErrorClassification.Unassigned, Fore.CYAN]
		else:
			return ClassifiedErrors[classname]
	def TracebackHook(self, e, v, t):
		self.print('Error just raised with errortype: '+str(e.__name__)+'.', CT.ERROR)
		esp_error = self.GetClassClassification(str(e.__name__))
		self.print('We classified this error as '+esp_error[1]+str(esp_error[0])+Fore.RESET+'.', CT.ERROR)
		self.print("ErrorValue: "+str(v), CT.ERROR)
		self.print("Traceback: "+str(traceback.extract_tb(t)), CT.ERROR)
		self.print("Server will be closed, because this error may broke something.", CT.INFO)
		self.print("// To-Do: In future wanted to keep working after error handled (sys module doesn't give to do that.)", CT.INFO)

esp = ESP()

sys.excepthook = esp.TracebackHook

class nolist_createUser(npyscreen.Form):
	def create(self):
		self.username = self.add(npyscreen.TitleText, name='Username')
		self.pswd = self.add(npyscreen.TitlePassword, name='Password')
		self.avatar = self.add(npyscreen.TitleSlider, name='Avatar', out_of=20,step=1,lowest=0)
		self.elec = self.add(npyscreen.TitleSlider, name='Electricity',step=10000,out_of=1000000000,lowest=0)
		self.pps = self.add(npyscreen.TitleSlider, name='PP', out_of=7450,step=50,lowest=0)
		self.banned = self.add(npyscreen.CheckBox, name='Is banned?')
		self.access = self.add(npyscreen.CheckBox, name='Is removed?')
	def realCreate(*args):
		f = nolist_createUser(name="New User")
		f.edit()
		return f

def dbgCreateUser():
	"""Shows form to create user from debugger."""
	if not(isDebugger): return
	curses.initscr()
	storeData = npyscreen.wrapper_basic(nolist_createUser.realCreate)
	a = AddUser(storeData.username.value, EStr(storeData.pswd.value), int(storeData.avatar.value), int(storeData.elec.value), float(storeData.pps.value), "[]", "\{\}", "", "\{\}", bool(storeData.banned.value), "0.0.0.0", bool(storeData.access.value), -1, '[]')
	if(a != "OK"):
		print("There was an error while creating user account ("+a+")", CT.ERROR)
	else:
		print("User "+Fore.CYAN+storeData.username.value+Fore.RESET+" was created successfully!", CT.INFO)


def CalculatePPv2(dmgDealt, dmgTaken, supportPoints):
	"""Perfomance Points calculator"""
	if(supportPoints == 0): bonus = -5
	elif(supportPoints > 0):
		bonus = math.fabs(round(math.atan2(supportPoints, -supportPoints)))+math.tan(supportPoints*11.3777)+(supportPoints/0.5*0.25)
	else:
		supportPoints = math.fabs(supportPoints)
		bonus = math.fabs(round(math.atan2(supportPoints, -supportPoints)))+math.tan(supportPoints*11.3777)+(supportPoints/0.5*0.25)+supportPoints * 2.5
		bonus = -(bonus)
	return -3 + (dmgDealt ** 1.25 - dmgTaken ** 1.2589)/10.5+bonus

# Checking dbs

if not (os.path.isfile("users.db")):
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE users
             (username text, passhash text, avatar int, electricity int, ppcount float, inventory text, customization text, bio text, stats text, banned boolean, regip text, accessible boolean,ban_reason int, badges text)''')
	c.execute('''INSERT INTO users VALUES ('act8', '', 0, 1000000, 0, '[]', '\{\}', '', '\{\}', false, '', true, -1, '["badge_bot"]')''')
	c.execute('''CREATE TABLE bannednames
		(name text)''')
	c.execute('''CREATE TABLE db_info
             (st text, data int)''')
	c.execute('''INSERT INTO db_info VALUES ('ver', {})'''.format(str(db_usersVer)))
	conn.commit()
	conn.close()
	Logger("Created new user database, because users.db was missing.", CT.INFO)

if not (os.path.isfile("additional.db")):
	conn = sqlite3.connect('additional.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE crates
             (item_code text, items_in text)''')
	c.execute('''CREATE TABLE shop_pool
             (item_code text, min_price int, max_price int)''')
	c.execute('''CREATE TABLE shop_current
             (item_code text, price int)''')
	c.execute('''CREATE TABLE item_keys (key text, type text, code text)''')
	c.execute('''CREATE TABLE time_storage
             (sett text, unix int)''')
	c.execute('''CREATE TABLE db_info
             (st text, data int)''')
	c.execute('''INSERT INTO time_storage VALUES ('store_update', 0)''')
	c.execute('''INSERT INTO db_info VALUES ('ver', {})'''.format(str(db_AdditionalsVer)))
	conn.commit()
	conn.close()
	Logger("Created new additionals database, because additional.db was missing.", CT.INFO)



if(platform.system() == "Windows"):
	subprocess.check_call(["attrib","+H","users.db"])
	subprocess.check_call(["attrib","+H","additional.db"])

# Logging information about run

Logger("-----------------------")
Logger("Python: "+sys.version)
try:
	import pip
	Logger("Pip: "+pip.__version__)
except ImportError:
	Logger("Pip: Not found.")
foundProc = False
if(platform.system() == "Windows"):
	foundProc = True
	Logger("Processor: "+platform.processor())
elif platform.system() == "Darwin":
	foundProc = True
	os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
	command ="sysctl -n machdep.cpu.brand_string"
	Logger("Processor: "+str(subprocess.check_output(command).strip()))
elif platform.system() == "Linux":
	foundProc = True
	command = "cat /proc/cpuinfo"
	try:
		all_info = subprocess.check_output(command, shell=True).strip()
		for line in all_info.split("\n"):
			if "model name" in line:
				Logger("Processor: "+str(re.sub( ".*model name.*:", "", line,1)))
	except Exception:
		foundProc = False

if not foundProc:
	Logger("Processor: Unknown")

Logger("RAM: "+str(psutil.virtual_memory().total/1024/1024)+" MB")
partitions = psutil.disk_partitions()
Logger('Disks:')
diskCount = 0
for p in partitions:
	diskCount += 1
	Logger('[Disk '+str(diskCount)+'] '+p.device+"(mnt: {} / fstype: {})".format(p.mountpoint, p.fstype))

Logger("Users: ")
uCount = 0
for u in psutil.users():
	uCount += 1
	Logger("[User {}] {}".format(str(uCount), u.name))
try:
	pidarray = psutil.pids()
	npid = {}
	for p in pidarray:
		npid[p] = psutil.Process(p).name
	Logger("Current processes: ")
	for k,v in npid.items():
		Logger("[PID {}]: {}".format(str(k), v))
except Exception as ex:
	print("Error while storing debug information was raised. Check log file for more information.", CT.WARN)
	Logger("Error code: "+str(ex), CT.ERROR)
Logger("-----------------------")

def dbgSwitchErrorDisplay():
	global isFormattedError
	global isDebugger
	if not(isDebugger): return
	isFormattedError = not isFormattedError
	if(isFormattedError): print("Set formatting to "+Fore.CYAN+"PRETTY"+Fore.RESET+".")
	else: print("Set formatting to "+Fore.CYAN+"INFORMATIVE"+Fore.RESET+".")

def dbgNoDebug():
	global isDebugger
	if not isDebugger:
		print("You can only LEAVE debugger, not ENTER.")
		return
	isDebugger = False
	print("You are now moron.")
	return

conn = sqlite3.connect('users.db')
c = conn.cursor()
try:
	dInfo = c.execute("SELECT data FROM db_info WHERE st = 'ver'")
	dInfo = dInfo.fetchone()[0]
except Exception:
	print("Your version of users.db is very out of date. Please"+Fore.RED+" recreate "+Fore.RESET+"it ASAP.", CT.ERROR)
	dInfo = db_usersVer
if(dInfo < db_usersVer):
	print("Your version of users.db is out of date. Please be sure to recreate it or update.", CT.WARN)
elif(dInfo > db_usersVer):
	print("Your version of users.db is newer than this ELVEX SOCIAL version requires. Something may be broken.", CT.WARN)
conn.close()
conn = sqlite3.connect('additional.db')
c = conn.cursor()
try:
	dInfo = c.execute("SELECT data FROM db_info WHERE st = 'ver'")
	dInfo = dInfo.fetchone()[0]
except Exception:
	print("Your version of additional.db is very out of date. Please"+Fore.RED+" recreate "+Fore.RESET+"it ASAP.", CT.ERROR)
	dInfo = db_AdditionalsVer

if(dInfo < db_AdditionalsVer):
	print("Your version of additional.db is out of date. Please be sure to recreate it or update.", CT.WARN)
elif(dInfo > db_AdditionalsVer):
	print("Your version of additional.db is newer than this ELVEX SOCIAL version requires. Something may be broken.", CT.WARN)
conn.close()

def CompleterLoad():
	global history
	for name, val in elvex_module.__dict__.items():
		if callable(val) and name not in NotList:
			try:
				args = inspect.getfullargspec(val)[0]
			except Exception:
				continue
			if(name.startswith("nolist_")):
				continue
			history.append_string(name+"()")

def is_valid_command(v):
	return re.match(r"\b[^()]+\((.*)\)$", v) is not None

NotAScriptMessage = Fore.RESET + '''
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢛⣉⣩⣤⣬⣉⣉⣉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠋⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣈⠻⢿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⢁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡙⠿⣿⣿⣿
⣿⣿⠏⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠙⢻⣷⡆⠹⣿⣿
⣿⡇⢠⣿⣿⣿⣿⣿⣿⡟⠋⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⣴⣿⣿⡄⢹⣿
⡟⢀⣿⣿⣿⣿⣿⣿⣿⣧⣀⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢻
⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⢛⣋⣉⣉⣉⠙⢿⣿⣿⣿⣿⣿⡇⢸
⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣡⣴⣶⣿⣿⣿⣿⣿⣿⣧⠄⢿⣿⣿⣿⣿⡇⢸
⣇⠈⣿⣿⣿⣿⣿⣿⣿⡟⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢸⣿⣿⣿⣿⠃⣼
⣿⣆⠘⣿⣿⣿⣿⣿⣿⡇⣴⣤⣤⣬⣉⡛⠻⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠃⢸⣿
⣿⣿⣆⠘⢿⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⠿⠷⠌⠛⢛⣋⣉⣁⣸⣿⡿⠋⣠⣿⣿
⣿⣿⣿⣶⡈⠙⢿⣿⣟⣈⣉⣩⣥⣤⣶⣶⣶⣾⣿⣿⣿⣿⣿⡿⠟⢁⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⣉⣤⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣈⡉⠉⠛⣋⣉⣉⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿'''+Fore.RESET+'''
This is not a script. This is library.
You cannot run it s/c.
'''

if(len(sys.argv) > 1 and sys.argv[1] == "debugger"):
	Logger("Debugger initialized.", CT.WARN)
	oprint("Debugger for Elvex SOCIAL v"+str(version)+", act8team.\nVisit act8team.com for more information.")
	import curses
	isFormattedError = True
	isDebugger = True
	history = prompt_toolkit.history.InMemoryHistory()
	CompleterLoad()
	session = prompt_toolkit.PromptSession(
        history=history,
        auto_suggest=prompt_toolkit.auto_suggest.AutoSuggestFromHistory(),
        enable_history_search=True)
	validator = prompt_toolkit.validation.Validator.from_callable(is_valid_command, error_message='Not a valid function. (Cannot be executed)', move_cursor_to_end=True)
	while(True):
		oprint(Fore.CYAN+ '> '+Fore.RESET,end='')
		if(isFormattedError):
			a = session.prompt('  ', validator=validator, validate_while_typing=True)
			try:
				eval(a)
			except Exception as e:
				print(str(e), CT.ERROR)
		else:
			a = input()
			eval(a)
elif(__name__ == "__main__"):
	try:
		print(NotAScriptMessage)
	except Exception:
		os._exit(-1)
	time.sleep(10)
	os._exit(-1)
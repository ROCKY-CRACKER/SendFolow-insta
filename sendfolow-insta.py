import os

if os.name=="nt":exit()
else:pass
try:
	import  os , sys , random, requests , time , json , secrets,uuid,re,wget,user_agent
	import subprocess # 01011010 01100101 01100100
	from bs4 import BeautifulSoup 
	from uuid import uuid4
	from time import sleep 
except:
	os.system('pip install requests')
	os.system('pip install bs4')
	os.system("pip install user_agent")
	os.system("pip install wget")
	import  os , sys , random, requests , time , json , secrets,uuid,re,wget,user_agent
	import subprocess # 01011010 01100101 01100100
	from bs4 import BeautifulSoup 
	from uuid import uuid4
	from time import sleep 
else:pass

mmm= """

  ______    _ _                 _____ _____ 
 |  ____|  | | |               |_   _/ ____|
 | |__ ___ | | | _____      __   | || |  __ 
 |  __/ _ \| | |/ _ \ \ /\ / /   | || | |_ |
 | | | (_) | | | (_) \ V  V /   _| || |__| |
 |_|  \___/|_|_|\___/ \_/\_/   |_____\_____|
                                            
                                            
                  
                                             

""" 
Tk = """


  ______    _ _                 _____ _____ 
 |  ____|  | | |               |_   _/ ____|
 | |__ ___ | | | _____      __   | || |  __ 
 |  __/ _ \| | |/ _ \ \ /\ / /   | || | |_ |
 | | | (_) | | | (_) \ V  V /   _| || |__| |
 |_|  \___/|_|_|\___/ \_/\_/   |_____\_____|
                                            
                                            
                                

""" 



#------------------------------------------------------------------------------------------------------------------------
def zz():
	os.system('clear')
	global comb,mmm,Tk
	print(mmm)
	print("-"*50)
	r = requests.session()
	print("\n Welcome\n")
	combi=input(' Acc FILE: ')
	file=open(combi,"r").read().splitlines()
	txx = str(input("\n username target : "))
	print("-"*50)
	don=0
	for io in file:
		Email=io.split(':')[0]
		pas=io.split(':')[1]
		r = requests.session()
		tt=time.asctime()
		usus=user_agent.generate_user_agent()
		url = 'https://www.instagram.com/accounts/login/ajax/'
		urCOm = f'https://www.instagram.com/web/comments/2669921265571135668/add/'
		head = {'accept':'*/*','accept-encoding':'gzip,deflate,br','accept-language':'en-US,en;q=0.9,ar;q=0.8','content-length':'269','content-type':'application/x-www-form-urlencoded','cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'8a8118fa7d40','x-requested-with':'XMLHttpRequest', 'user-agent': usus}
		data = {'username': Email,'enc_password': "#PWD_INSTAGRAM_BROWSER:0:&:"+str(pas),'queryParams': {},'optIntoOneTap': 'false',}
		login = requests.post(url,headers=head,data=data,allow_redirects=True)
		time.sleep(2.9)
		if 'userId' in login.text:
			cook = login.cookies['sessionid']
			hedCOM = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/x-www-form-urlencoded','cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid=' + cook,'origin': 'https://www.instagram.com','referer': f'https://www.instagram.com/p/CUNdz7EoQC0/','sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': usus,'x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq','x-instagram-ajax': '753ce878cd6d','x-requested-with': 'XMLHttpRequest'}
			fffs=[":)"]
			tx=random.choice(fffs)
			daCOM = {'comment_text': tx,'replied_to_comment_id': ''}
			for i in range(1):
				requests.post(urCOm, headers=hedCOM, data=daCOM)
			url=f"https://www.instagram.com/{txx}/?__a=1"
			headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','cookie': f'mid=YR2RKQALAAHrCbQwbS5NFzTCStuh; ig_did=424344B5-DCDF-4888-BD13-C56BE8BFF561; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=dq4i5qyC7mjFnr731RllWR0mvBf6w9nE; ds_user_id=44727257007; sessionid={cook}; shbid="8034\05444727257007\0541662125439:01f7c6e350cdd9d116745fbd697cadba8c1f58890de93e610ad53149cc44919876d79d91"; shbts="1630589439\05444727257007\0541662125439:01f718500f57b83260e7e22f8dd8c956a44d5dc5e8d0320a672aa6c651455f1570febc62"; rur="ASH\05444727257007\0541662129376:01f731bcc2afd2169af0bc7d969665be3b30ac3eaaa6603311276a0b02950003791bf2a0"','referer': 'https://codeofaninja.com/','sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'cross-site','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2757.56 Safari/537.36'}
			pr={'__a': '1'}
			inin=requests.get(url,headers=headers,data=pr)
			idf=inin.json()['graphql']['user']['id']
			url1=f'https://www.instagram.com/web/friendships/{idf}/follow/'
			hedo={
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '0',
'content-type': 'application/x-www-form-urlencoded',
'cookie': f'mid=YWgkwQALAAHfxbRoGBDx5qlzlEoA; ig_did=65BBE0EC-0C6D-4628-A279-39471F60597D; ig_nrcb=1; csrftoken=fmocWjn1wziD47REoYeE9Qe1NlT170jU; ds_user_id=44727257007; sessionid={cook}; shbid="8034\05444727257007\0541667139955:01f7089c64330226086e42ca0d2ecbd6519cf00ee399c0ef1f81ae7ce70cfc3e82a33d08"; shbts="1635603955\05444727257007\0541667139955:01f7915ce7b0663aca3810ba35343fa72a7cc15412db893b4302893debfc368b2d503706"; rur="RVA\05444727257007\0541667139972:01f7400785fbaedaaa1fbb007e11efc483f71f271397e6980d025d5cda353017be101477"',
'origin': 'https://www.instagram.com',
'referer': f'https://www.instagram.com/{txx}/',
'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': usus,
'x-asbd-id': '198387',
'x-csrftoken': 'fmocWjn1wziD47REoYeE9Qe1NlT170jU',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': 'hmac.AR2XkrvPf1pO8XwCk4oQBcCZR0vBiCp4lhGswsNbBF0RoJCW',
'x-instagram-ajax': '1f6b15d613c7',
'x-requested-with': 'XMLHttpRequest'
			}
			requests.post(url1,headers=hedo)
			don+=1
			print(f'sent {don}')
		else:
			print('error')

zz()


from selenium.webdriver.common.by import By


class SignInPageLocator(object):
    email = (By.XPATH, '//*[@id="email"]')
    password = (By.XPATH, '//*[@id="pass"]')
    signInBtn = (By.XPATH, '//button[@data-testid="royal_login_button"]')


class PostingLocators(object):
    imageInput = (By.XPATH, '//input[@type="file"]')
    postbox = (By.XPATH,
               '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')
    postbutton = (By.CSS_SELECTOR,
                  "body._6s5d._71pn._-kb.segoe:nth-child(2) div.rq0escxv.l9j0dhe7.du4w35lb div.__fb-light-mode.l9j0dhe7.tkr6xdv7 div.rq0escxv.l9j0dhe7.du4w35lb:nth-child(1) div.j83agx80.cbu4d94t.h3gjbzrl.l9j0dhe7 div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p:nth-child(2) div.gs1a9yip.rq0escxv.j83agx80.cbu4d94t.kb5gq1qc.taijpn5t.h3gjbzrl div.ll8tlv6m.rq0escxv.j83agx80.taijpn5t.pnzxbu4t.hpfvmrgz.hzruof5a.dflh9lhu.scb9dxdr.q5pvgw0d.l7iv3u6u.f59ohtjy.aw1xchsf div.cjfnh4rs.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.lzcic4wl.ni8dbmo4.stjgntxs.oqq733wu.cwj9ozl2.io0zqebd.m5lcvass.fbipl8qg.nwvqtn77.nwpbqux9.iy3k6uwz.e9a99x49.g8p4j16d.bv25afu3.d2edcug0 div.idiwt2bm.lzcic4wl.ni8dbmo4.stjgntxs.l9j0dhe7.dbpd2lw6 div.rq0escxv.pmk7jnqg.du4w35lb.pedkr2u6.oqq733wu.ms05siws.pnx7fd3z.b7h9ocf4.j9ispegn.kr520xx4:nth-child(1) div.idiwt2bm.lzcic4wl.ni8dbmo4.stjgntxs.l9j0dhe7.dbpd2lw6:nth-child(1) div.rq0escxv.pmk7jnqg.du4w35lb.pedkr2u6.oqq733wu.ms05siws.pnx7fd3z.b7h9ocf4.j9ispegn.kr520xx4:nth-child(1) div.k4urcfbm.l9j0dhe7.datstx6m.rq0escxv div.l9j0dhe7 div.j83agx80.btwxx1t3 div.j83agx80.cbu4d94t.f0kvp8a6.mfofr4af.l9j0dhe7.ij1vhnid.smbo3krw.oh7imozk div.ihqw7lf3.discj3wi.l9j0dhe7:nth-child(3) div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.hv4rvrfc.dati1w0a.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.p8fzw8mz.pcp91wgn.iuny7tx3.ipjc6fyt > div.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.pq6dq46d.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.l9j0dhe7.abiwlrkh.p8dawk7l.cbu4d94t.taijpn5t.k4urcfbm")


class PeopleList(object):
    searchField = (By.XPATH, '//input[@role="combobox"]')
    people_menu = (By.XPATH, "//span[contains(text(),'People')]")
    allpeople = (By.XPATH, '//div[@class="ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi a8c37x1j"]')
    end_of_result = (By.XPATH, "//span[contains(text(),'End of results')]")
    name = (By.XPATH, './/a[@role="presentation"]')
    id_link = (By.XPATH, './/a[@role="presentation"]')
    friend_button = ""


class SendingFriendRequest(object):
    friend_request = (By.XPATH,
                      "//span[contains(text(),'Add Friend')]")
    send_message = (By.XPATH, "//span[contains(text(),'Cancel Request')]")

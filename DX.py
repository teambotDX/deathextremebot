# - * - coding: utf-8 - * -
dari LineAlpha impor LineClient
dari LineAlpha.LineApi impor LineTracer
dari LineAlpha.LineThrift.ttypes import Message
dari LineAlpha.LineThrift.TalkService mengimpor Klien
waktu impor , datetime, acak, sys, re, string, os, json

memuat ulang (sys)
sys.setdefaultencoding ( ' utf-8 ' )

client = LineClient ()
client._qrLogin ( " line: // au / q / " )

profil, pengaturan, pelacak = client.getProfile (), client.getSettings (), LineTracer (klien)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult ()

tunggu = {
    ' readPoint ' : {},
    ' readMember ' : {},
    ' setTime ' : {},
    ' ROM ' : {}
   }

setTime = {}
setTime = menunggu [ " setTime " ]

def  sendMessage ( ke , teks , contentMetadata = {}, contentType = 0 ):
    mes = Message ()
    mes.to, mes.from_ = to, profile.mid
    mes.text = teks

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    jika untuk tidak  di messageReq:
        messageReq [to] =  - 1
    messageReq [to] + =  1
    client._client.sendMessage (messageReq [to], mes)

def  NOTIFIED_ADD_CONTACT ( op ):
    coba :
        sendMessage (op.param1, client.getContact (op.param1) .displayName +  " Terima kasih telah menambahkan " )
    kecuali  Exception  sebagai e:
        cetak e
        print ( " \ n \ n NOTIFIED_ADD_CONTACT \ n \ n " )
        kembali

tracer.addOpInterrupt ( 5 , NOTIFIED_ADD_CONTACT )

def  NOTIFIED_ACCEPT_GROUP_INVITATION ( op ):
    # cetak op
    coba :
        sendMessage (op.param1, client.getContact (op.param2) .displayName +  " WELCOME to "  + group.name)
    kecuali  Exception  sebagai e:
        cetak e
        print ( " \ n \ n NOTIFIED_ACCEPT_GROUP_INVITATION \ n \ n " )
        kembali

tracer.addOpInterrupt ( 17 , NOTIFIED_ACCEPT_GROUP_INVITATION )

def  NOTIFIED_KICKOUT_FROM_GROUP ( op ):
    coba :
        sendMessage (op.param1, client.getContact (op.param3) .displayName +  " Good Bye \ n (* ´ ･ ω ･ *) " )
    kecuali  Exception  sebagai e:
        cetak e
        print ( " \ n \ n NOTIFIED_KICKOUT_FROM_GROUP \ n \ n " )
        kembali

tracer.addOpInterrupt ( 19 , NOTIFIED_KICKOUT_FROM_GROUP )

def  NOTIFIED_LEAVE_GROUP ( op ):
    coba :
        sendMessage (op.param1, client.getContact (op.param2) .displayName +  " Good Bye \ n (* ´ ･ ω ･ *) " )
    kecuali  Exception  sebagai e:
        cetak e
        print ( " \ n \ n NOTIFIED_LEAVE_GROUP \ n \ n " )
        kembali

tracer.addOpInterrupt ( 15 , NOTIFIED_LEAVE_GROUP )

def  NOTIFIED_READ_MESSAGE ( op ):
    # cetak op
    coba :
        jika op.param1 di menunggu [ ' readPoint ' ]:
            Nama = client.getContact (op.param2) .displayName
            jika Nama di tunggu [ ' readMember ' ] [op.param1]:
                lulus
            lain :
                tunggu [ ' readMember ' ] [op.param1] + =  " \ n・"  + Nama
                tunggu [ ' ROM ' ] [op.param1] [op.param2] =  "・"  + Nama
        lain :
            lulus
    kecuali :
        lulus

tracer.addOpInterrupt ( 55 , NOTIFIED_READ_MESSAGE )

def  RECEIVE_MESSAGE ( op ):
    msg = op.message
    coba :
        jika msg.contentType ==  0 :
            coba :
                jika msg.to di menunggu [ ' readPoint ' ]:
                    jika msg.from_ di menunggu [ " ROM " ] [msg.to]:
                        del wait [ " ROM " ] [msg.to] [msg.from_]
                lain :
                    lulus
            kecuali :
                lulus
        lain :
            lulus
    kecuali  KeyboardInterrupt :
	       sys.exit ( 0 )
    kecuali  Exception  sebagai kesalahan:
        kesalahan cetak
        print ( " \ n \ n RECEIVE_MESSAGE \ n \ n " )
        kembali

tracer.addOpInterrupt ( 26 , RECEIVE_MESSAGE )

def  SEND_MESSAGE ( op ):
    msg = op.message
    coba :
        jika msg.toType ==  0 :
            jika msg.contentType ==  0 :
                jika msg.text ==  " mid " :
                    sendMessage (msg.to, msg.to)
                jika msg.text ==  " saya " :
                    sendMessage (msg.to, text = Tidak Ada , contentMetadata = { ' mid ' : msg.from_}, contentType = 13 )
                jika msg.text ==  " hadiah " :
                    sendMessage (msg.to, text = " hadiah terkirim " , contentMetadata = Tidak ada , contentType = 9 )
                lain :
                    lulus
            lain :
                lulus
        jika msg.toType ==  2 :
            jika msg.contentType ==  0 :
                jika msg.text ==  " mid " :
                    sendMessage (msg.to, msg.from_)
                jika msg.text ==  " gid " :
                    sendMessage (msg.to, msg.to)
                jika msg.text ==  " ginfo " :
                    group = client.getGroup (msg.to)
                    md =  " [Nama Grup] \ n "  + group.name +  " \ n \ n [gid] \ n "  + group.id +  " \ n \ n [Gambar Grup] \ n http: //dl.profile. line-cdn.net/ "  + group.pictureStatus
                    jika group.preventJoinByTicket adalah  False : md + =  " \ n \ n InvitationURL: Diizinkan \ n "
                    else : md + =  " \ n \ n InvitationURL: Menolak \ n "
                    jika group.invitee is  None : md + =  " \ n Anggota: "  +  str ( len (group.members)) +  "人\ n \ n Mengundang: 0Orang "
                    else : md + =  " \ n Anggota: "  +  str ( len (group.members)) +  " Orang \ n Diundang: "  +  str ( len (group.invitee)) +  " Orang "
                    sendMessage (msg.to, md)
                jika  " gname: "  di msg.text:
                    key = msg.text [ 22 :]
                    group = client.getGroup (msg.to)
                    group.name = kunci
                    client.updateGroup (grup)
                    sendMessage (msg.to, " Nama Grup " + kunci + " Canged to " )
                jika msg.text ==  " url " :
                    sendMessage (msg.to, " line: // ti / g / "  + client._client.reissueGroupTicket (msg.to))
                jika msg.text ==  " terbuka " :
                    group = client.getGroup (msg.to)
                    if group.preventJoinByTicket ==  Salah :
                        sendMessage (msg.to, " sudah terbuka " )
                    lain :
                        group.preventJoinByTicket =  Salah
                        client.updateGroup (grup)
                        sendMessage (msg.to, " URL Open " )
                jika msg.text ==  " tutup " :
                    group = client.getGroup (msg.to)
                    if group.preventJoinByTicket ==  Benar :
                        sendMessage (msg.to, " sudah dekat " )
                    lain :
                        group.preventJoinByTicket =  Benar
                        client.updateGroup (grup)
                        sendMessage (msg.to, " URL close " )
                jika  " menendang: "  dalam msg.teks:
                    key = msg.text [ 5 :]
                    client.kickoutFromGroup (msg.to, [key])
                    contact = client.getContact (kunci)
                    sendMessage (msg.to, " " + contact.displayName + " sorry " )
                jika  " nk: "  di msg.text:
                    key = msg.text [ 3 :]
                    group = client.getGroup (msg.to)
                    Nama = [contact.displayName untuk kontak dalam group.members]
                    Mids = [contact.mid untuk kontak dalam group.members]
                    jika kunci dalam Nama:
                        kazu = Names.index (key)
                        sendMessage (msg.to, " Bye " )
                        client.kickoutFromGroup (msg.to, [ " " + Mids [kazu] + " " ])
                        contact = client.getContact (Mids [kazu])
                        sendMessage (msg.to, " " + contact.displayName + " Maaf " )
                    lain :
                        sendMessage (msg.to, " wtf? " )
                jika msg.text ==  " membatalkan " :
                    group = client.getGroup (msg.to)
                    jika group.invitee is  None :
                        sendMessage (op.message.to, " Tidak ada yang mengundang. " )
                    lain :
                        gInviMids = [contact.mid untuk kontak dalam group.invitee]
                        client.cancelGroupInvitation (msg.to, gInviMids)
                        sendMessage (msg.to, str ( len (group.invitee)) +  " Done " )
                jika  " undang: "  dalam msg.teks:
                    key = msg.text [ - 33 :]
                    client.findAndAddContactsByMid (kunci)
                    client.inviteIntoGroup (msg.to, [key])
                    contact = client.getContact (kunci)
                    sendMessage (msg.to, " " + contact.displayName + " Saya mengundang Anda " )
                jika msg.text ==  " saya " :
                    M = Pesan ()
                    M.to = msg.to
                    M.contentType =  13
                    M.contentMetadata = { ' mid ' : msg.from_}
                    client.sendMessage (M)
                jika  " show: "  di msg.text:
                    key = msg.text [ - 33 :]
                    sendMessage (msg.to, text = Tidak ada , contentMetadata = { ' mid ' : key}, contentType = 13 )
                    contact = client.getContact (kunci)
                    SendMessage (msg.to, " " + contact.displayName + " kontak 's " )
                jika msg.text ==  " time " :
                    sendMessage (msg.to, " Waktu sekarang adalah "  + datetime.datetime.today (). strftime ( ' % Y 年% m 月% d日% H:% M:% S ' ) +  " is " )
                jika msg.text ==  " hadiah " :
                    sendMessage (msg.to, text = " hadiah terkirim " , contentMetadata = Tidak ada , contentType = 9 )
                jika msg.text ==  " set " :
                    sendMessage (msg.to, " Saya telah menetapkan titik baca ♪ \ n「 tes 」Saya akan menunjukkan kepada Anda siapa yang saya baca ♪ " )
                    coba :
                        del wait [ ' readPoint ' ] [msg.to]
                        del wait [ ' readMember ' ] [msg.to]
                    kecuali :
                        lulus
                    tunggu [ ' readPoint ' ] [msg.to] = msg.id
                    tunggu [ ' readMember ' ] [msg.to] =  " "
                    tunggu [ ' setTime ' ] [msg.to] = datetime.datetime.today (). strftime ( ' % Y-% m- % d % H:% M:% S ' )
                    tunggu [ ' ROM ' ] [msg.to] = {}
                    cetak tunggu
                jika msg.text ==  " tes " :
                    jika msg.to di menunggu [ ' readPoint ' ]:
                        jika menunggu [ " ROM " ] [msg.to] .items () == []:
                            chiya =  " "
                        lain :
                            chiya =  " "
                            untuk rom dalam menunggu [ " ROM " ] [msg.to] .items ():
                                cetak rom
                                chiya + = rom [ 1 ] +  " \ n "

                        sendMessage (msg.to, " Orang yang membaca % s \ n hanya itu \ n \ n Orang yang telah mengabaikan pembacaan \ n % s Tidak normal ♪ \ n \ n Membaca tanggal pembuatan poin n kali: \ n [ % s ] "   % (tunggu [ ' readMember ' ] [msg.to], chiya, setTime [msg.to]))
                    lain :
                        sendMessage (msg.to, " Titik yang sudah dibaca belum ditetapkan. \ n「 set 」Anda dapat mengirim ♪ titik baca akan dibuat ♪ " )
                lain :
                    lulus
        lain :
            lulus

    kecuali  Exception  sebagai e:
        cetak e
        print ( " \ n \ n SEND_MESSAGE \ n \ n " )
        kembali

tracer.addOpInterrupt ( 25 , SEND_MESSAGE )

sementara  True :
    tracer.execute ()
